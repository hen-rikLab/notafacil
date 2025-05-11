from flask import Flask, render_template, request, redirect, url_for
import os
import json

app = Flask(__name__)

diretorio_raiz = os.path.dirname(__file__)
caminho_ufpe = os.path.join(diretorio_raiz, 'dados', 'ufpe_cursos.json')
caminho_ufrpe = os.path.join(diretorio_raiz, 'dados', 'ufrpe_cursos.json')

def carregar_dados(universidade):
    caminho = caminho_ufpe if universidade == 'ufpe' else caminho_ufrpe
    if not os.path.exists(caminho):
        return {}
    with open(caminho, 'r', encoding='utf-8') as f:
        return json.load(f)

def calcular_nota_final(notas, pesos):
    total_peso = sum(pesos.values())
    return sum(notas[materia] * pesos[materia] for materia in pesos) / total_peso

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        universidade = request.form.get('universidade')
        return redirect(f'/cursos/{universidade}')
    return render_template('home.html')

@app.route('/cursos/<universidade>', methods=['GET', 'POST'])
def cursos(universidade):
    cursos = carregar_dados(universidade)
    if request.method == 'POST':
        curso = request.form.get('curso')
        return redirect(f'/notas/{universidade}/{curso}')
    return render_template('cursos.html', universidade=universidade, cursos=cursos)

@app.route('/notas/<universidade>/<curso>', methods=['GET', 'POST'])
def notas(universidade, curso):
    cursos = carregar_dados(universidade)
    curso_data = cursos.get(curso)

    if not curso_data:
        return redirect('/')

    if request.method == 'POST':
        notas = {
            'redacao': float(request.form.get('redacao')),
            'linguagens': float(request.form.get('linguagens')),
            'humanas': float(request.form.get('humanas')),
            'natureza': float(request.form.get('natureza')),
            'matematica': float(request.form.get('matematica'))
        }
        cota = request.form.get('cota')
        return redirect(f'/resultado/{universidade}/{curso}/{cota}/{notas["redacao"]}/{notas["linguagens"]}/{notas["humanas"]}/{notas["natureza"]}/{notas["matematica"]}')

    return render_template('notas.html', universidade=universidade, curso=curso, curso_data=curso_data)

@app.route('/resultado/<universidade>/<curso>/<cota>/<redacao>/<linguagens>/<humanas>/<natureza>/<matematica>')
def resultado(universidade, curso, cota, redacao, linguagens, humanas, natureza, matematica):
    cursos = carregar_dados(universidade)
    curso_data = cursos.get(curso)
    
    if not curso_data:
        return redirect('/')

    notas = {
        'redacao': float(redacao),
        'linguagens': float(linguagens),
        'humanas': float(humanas),
        'natureza': float(natureza),
        'matematica': float(matematica)
    }

    nota_final = calcular_nota_final(notas, curso_data['pesos'])
    nota_corte = curso_data['nota_corte'].get(cota, 0)
    aprovado = nota_final >= nota_corte

    return render_template(
        'resultado.html',
        universidade=universidade.upper(),
        curso=curso,
        nota_final=round(nota_final, 2),
        nota_corte=nota_corte,
        cota=cota.replace('_', ' ').capitalize(),
        aprovado=aprovado
    )

if __name__ == '__main__':
    app.run(debug=True)