# 🧮 Nota Fácil

**Nota Fácil** é uma aplicação web feita com **Python (Flask)** que simula a nota final de candidatos a cursos da **UFPE** e **UFRPE** com base nas notas do ENEM, pesos por curso e cotas. O sistema calcula automaticamente se o candidato tem chances reais de aprovação com base na nota de corte.

---

## 🚀 Funcionalidades

- Seleção de universidade (UFPE ou UFRPE)
- Escolha do curso desejado
- Inserção das notas do ENEM
- Escolha do tipo de cota
- Cálculo da nota final ponderada
- Comparação com a nota de corte por cota
- Resultado com aprovação ou reprovação
- Interface moderna e responsiva com Bootstrap 5

---

## ⚙️ Tecnologias utilizadas

- Python 3
- Flask
- HTML5 + Jinja2
- Bootstrap 5 + Bootstrap Icons
- JSON (para os dados dos cursos)

---

## 🛠️ Como rodar localmente

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/nome-do-repo.git
cd nome-do-repo
```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**

```bash
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/macOS:
source venv/bin/activate
```

3. **Instale as dependências:**

```bash
pip install flask
```

4. **Estrutura de pastas esperada:**
```
.
├── app.py
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── cursos.html
│   ├── notas.html
│   └── resultado.html
├── dados/
│   ├── ufpe_cursos.json
│   └── ufrpe_cursos.json
└── static/
    └── style.css (opcional)
```

5. **Execute o servidor Flask:**

```bash
python app.py
```

6. **Acesse no navegador:**

```
http://127.0.0.1:5000/
```

---

## 📁 Dados dos cursos

Os dados de pesos e notas de corte dos cursos estão nos arquivos JSON:
- `ufpe_cursos.json`
- `ufrpe_cursos.json`

Você pode atualizá-los conforme novas edições do SISU.

---

## 📌 Melhorias futuras (ideias)

- Upload automático de notas ENEM
- Suporte a mais universidades e cursos
- Gráfico comparativo da nota
- Histórico de simulações

---

## 🧑‍💻 Autor e colaboradores

Desenvolvido por **Carlos Henrique**  
💼 GitHub: [@hen-rikLab](https://github.com/hen-rikLab)  
📧 Email: c.henrique.silva1103@outlook.com

**Com colaboração de:**
- Cauã Pereira — [@CauaOliveira7737](https://github.com/CauaOliveira7737)  
- Davi Miranda — [@dav1zeraa](https://github.com/dav1zeraa)
