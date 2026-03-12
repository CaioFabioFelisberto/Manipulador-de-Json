import json
import os


def salvar_dados(dados):
    with open('meu_banco.json', 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def carregar_dados():
    if not os.path.exists('meu_banco.json'):
        return []
    with open('meu_banco.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def criar_registro(lista_atual,numero_registro):
    ultimo_id = lista_atual[-1]['id'] if lista_atual else 0
    for i in range(numero_registro):
        nome = input('Digite o teu nome: ')
        idade = input('Digite a tua idade: ')
        novo_id = ultimo_id + i + 1

        novo_item = {
            'nome': nome,
            'idade': idade,
            'id' : novo_id
        }
        lista_atual.append(novo_item)
    salvar_dados(lista_atual)
    print(f'{numero_registro} registros cadastrados com sucesso!')

def listar_todos(lista_atual):
    if not lista_atual:
        print("\nO banco de dados está vazio! 📭")
        return
    print("\n--- LISTA DE REGISTROS ---")
    for item in lista_atual:
        print(f"ID: {item['id']} | Nome: {item['nome']} | Idade: {item['idade']}")

def buscar_registro(valor, lista_atual):
    encontrado = False
    for item in lista_atual:
        if item['nome'] == valor or item['id'] == valor:
            print(f"✅ Achado: {item['nome']}, {item['idade']} anos, ID {item['id']}")
            encontrado = True
    if not encontrado:
        print(f"❌ Valor '{valor}' não encontrado.")

def deletar_registro(lista_atual,*args):
    removidos = 0
    for item in lista_atual[:]:
        if item['nome'] in args or item['id'] in args:
            lista_atual.remove(item)
            print(f"🗑️ Registro {args} removido!")
            removidos += 1

    salvar_dados(lista_atual)
    print(f'{removidos} registros removidos.')

banco_de_dados = carregar_dados()

deletar_registro(banco_de_dados,3,4)
