import json
import os

diretorio_raiz = os.path.dirname(__file__)
caminho_ufpe = os.path.join(diretorio_raiz, 'dados', 'ufpe_cursos.json')
caminho_ufrpe = os.path.join(diretorio_raiz, 'dados', 'ufrpe_cursos.json')

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def carregar_dados(universidade):
    if universidade == 'ufpe':
        caminho = caminho_ufpe
    else:
        caminho = caminho_ufrpe

    if not os.path.exists(caminho):
        print("Arquivo de dados não encontrado!")
        return {}

    with open(caminho, 'r') as f:
        return json.load(f)

def calcular_nota_final(notas, pesos):
    total_peso = sum(pesos.values())
    nota = (
        notas['redacao'] * pesos['redacao'] +
        notas['linguagens'] * pesos['linguagens'] +
        notas['humanas'] * pesos['humanas'] +
        notas['natureza'] * pesos['natureza'] +
        notas['matematica'] * pesos['matematica']
    ) / total_peso
    return nota

def escolher_universidade():
    limpar_terminal()
    print("\n=== Universidades ===")
    print("1. UFPE")
    print("2. UFRPE")
    opcao = input("Escolha a universidade (1 ou 2): ")
    if opcao == "1":
        return "ufpe"
    elif opcao == "2":
        return "ufrpe"
    else:
        print("Opção inválida.")
        input("Pressione qualquer tecla para tentar novamente...")
        return escolher_universidade()

def escolher_curso(cursos):
    limpar_terminal()
    print("\n=== Cursos Disponíveis ===")
    for i, curso in enumerate(cursos.keys(), start=1):
        print(f"{i}. {curso}")
    try:
        escolha = int(input("Digite o número do curso desejado: ")) - 1
        curso_nome = list(cursos.keys())[escolha]
        return curso_nome
    except (ValueError, IndexError):
        print("Opção inválida.")
        input("Pressione qualquer tecla para tentar novamente...")
        return escolher_curso(cursos)

def escolher_cota(cotas_disponiveis):
    limpar_terminal()
    print("\n=== Cotas Disponíveis ===")
    for i, cota in enumerate(cotas_disponiveis, start=1):
        print(f"{i}. {cota.replace('_', ' ').capitalize()}")
    try:
        escolha = int(input("Digite o número da cota desejada: ")) - 1
        return cotas_disponiveis[escolha]
    except (ValueError, IndexError):
        print("Opção inválida.")
        input("Pressione qualquer tecla para tentar novamente...")
        return escolher_cota(cotas_disponiveis)

def obter_notas():
    limpar_terminal()
    print("\nDigite suas notas (0 a 1000):")
    notas = {}
    notas['redacao'] = float(input("Nota de Redação: "))
    notas['linguagens'] = float(input("Nota de Linguagens: "))
    notas['humanas'] = float(input("Nota de Humanas: "))
    notas['natureza'] = float(input("Nota de Natureza: "))
    notas['matematica'] = float(input("Nota de Matemática: "))
    return notas

def main():
    limpar_terminal()
    universidade = escolher_universidade()
    cursos = carregar_dados(universidade)

    if not cursos:
        print("Nenhum curso encontrado para esta universidade.")
        input("Pressione qualquer tecla para sair...")
        return

    curso_nome = escolher_curso(cursos)
    curso = cursos[curso_nome]

    notas = obter_notas()
    media_final = calcular_nota_final(notas, curso['pesos'])

    limpar_terminal()
    print(f"\nSua nota final para {curso_nome}: {media_final:.2f}")

    cota = escolher_cota(list(curso['nota_corte'].keys()))
    nota_corte = curso['nota_corte'][cota]

    print(f"\nNota de corte para {curso_nome} ({cota.replace('_', ' ').capitalize()}): {nota_corte}")
    print(f"\nSua nota final: {media_final:.2f}")

    if media_final >= nota_corte:
        print("✅ Você tem chance de ser aprovado!")
    else:
        print("❌ Sua nota ainda não atinge a nota de corte.")

    input("Pressione qualquer tecla para continuar...")
    limpar_terminal()

main()
