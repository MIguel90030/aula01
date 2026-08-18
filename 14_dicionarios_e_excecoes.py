"""
MODULO 4 - Funcoes, tuplas, dicionarios e tratamento de excecoes
Topico: Dicionarios (criar/acessar) + Tratamento de excecoes + Funcao final

"""

"""
------------------------------------------------------------
1) CRIANDO UM DICIONARIO
------------------------------------------------------------
Um dicionario guarda dados em pares CHAVE: VALOR, entre chaves {}.
"""

produto = {
    "id": 1,
    "nome": "Caneta",
    "preco": 2.5,
}
print("Dicionario criado:", produto)

"""
------------------------------------------------------------
2) ACESSANDO UM DICIONARIO
------------------------------------------------------------
"""

print("\nNome:", produto["nome"])
print("Preço:", produto["preco"])

# .get() busca uma chave sem gerar erro caso ela nao exista:
print("Chave 'estoque' (com get):", produto.get("estoque", "não informado"))

# Adicionando/alterando uma chave:
produto["estoque"] = 10
print("Depois de adicionar 'estoque':", produto)

"""
--- Acessando um dicionário PELO NOME ---
Também podemos montar um dicionário onde a própria chave é o
nome do produto - assim acessamos direto pelo nome, sem precisar
procurar posição por posição.
"""

estoque_por_nome = {
    "Caneta": 2.5,
    "Caderno": 15.0,
    "Borracha": 1.5,
}
print("\nPreço da Caneta:", estoque_por_nome["Caneta"])

nome_buscado = "Caderno"
print(f"Preço de {nome_buscado}:", estoque_por_nome[nome_buscado])

"""
--- Percorrendo TODAS as chaves e valores com FOR ---
.items() devolve cada par chave/valor do dicionário.
"""

print("\n--- Percorrendo o estoque ---")
for nome_produto, preco_produto in estoque_por_nome.items():
    print(f"{nome_produto} -> R${preco_produto:.2f}")

"""
--- Percorrendo APENAS as chaves com FOR ---
.keys() devolve somente as chaves (os nomes) do dicionário.
"""

print("\n--- Percorrendo apenas os nomes ---")
for nome_produto in estoque_por_nome.keys():
    print(nome_produto)

"""
--- Percorrendo APENAS os valores com FOR ---
.values() devolve somente os valores (os preços) do dicionário.
"""

print("\n--- Percorrendo apenas os preços ---")
for preco_produto in estoque_por_nome.values():
    print(preco_produto)

"""
------------------------------------------------------------
3) TRATAMENTO DE EXCECOES (try/except)
------------------------------------------------------------
Se tentarmos acessar uma chave que não existe com [ ], o Python
gera um erro (KeyError) e o programa para. Usamos try/except
para tratar isso.
"""

# Dicionário novo, só para este exemplo de KeyError:
cliente = {"nome": "João", "cidade": "Recife"}
try:
    print(cliente["telefone"])
except KeyError:
    print("Erro: a chave 'telefone' não existe neste dicionário.")

# Outro dicionário novo, para o exemplo de ValueError:
carrinho = {"item": "Mouse", "quantidade": 1}
try:
    carrinho["quantidade"] = int(input("\nNova quantidade: "))
    print("Carrinho atualizado:", carrinho)
except ValueError:
    print("Erro: quantidade inválida, digite apenas números.")

"""
--- Capturando QUALQUER tipo de erro com "Exception as erro" ---
Em vez de prever cada erro (KeyError, ValueError...), podemos
capturar todos com "except Exception as erro" - útil quando não
sabemos qual erro pode acontecer. "erro" guarda a mensagem
original do Python, que podemos imprimir ou personalizar.
"""

# Mais um dicionário novo, para o exemplo de Exception genérica:
"""
--- Repetindo até dar certo, com WHILE TRUE + BREAK ---
Aqui pedimos ao usuário uma chave do dicionário e usamos um
laço "while True" para repetir a pergunta enquanto a chave
digitada não existir. Assim que o try funciona sem erro,
usamos "break" para sair do laço.
"""

funcionario = {"nome": "Marcos", "cargo": "Vendedor"}
while True:
    try:
        chave = input("\nDigite uma informação do funcionário (nome/cargo): ")
        print(funcionario[chave])
        break  # só sai do laço quando a chave existir
    except Exception as erro:
        print("Erro original do Python:", erro)  # mostra a chave que não existe
        print(f"Mensagem personalizada: ocorreu um erro -> {erro}. Tente novamente.")

"""
------------------------------------------------------------
4) EXERCICIO FINAL: FUNCAO PARA CADASTRAR PRODUTOS (id + nome)
------------------------------------------------------------
Agora juntamos tudo em uma função: ela recebe o id e o nome do
produto, guarda em um dicionário e trata o erro caso o id não
seja um número.
"""

produtos = {}  # dicionário que vai guardar todos os produtos cadastrados


def cadastrar_produto(id_produto, nome_produto):
    """
    Cadastra um produto no dicionário 'produtos', usando o ID (convertido
    para número) como chave. Trata ValueError caso o ID não seja numérico.
    """
    try:
        id_produto = int(id_produto)  # tenta converter o ID de texto para número
        produtos[id_produto] = nome_produto  # usa o ID como chave e o nome como valor
        print(f"Produto cadastrado -> ID {id_produto}: {nome_produto}")
    except ValueError:
        print("Erro: o ID precisa ser um número.")


def main():
    """Menu principal: repete até o usuário escolher "s" (break) para sair."""
    while True:  # repete o menu indefinidamente, até um break
        opcao = input("\n[a] Adicionar produto  |  [s] Sair\nEscolha: ").lower()

        if opcao == "a":
            id_produto = input("ID do produto: ")
            nome_produto = input("Nome do produto: ")
            cadastrar_produto(id_produto, nome_produto)  # delega o cadastro para a função
        elif opcao == "s":
            print("Encerrando...")
            break  # sai do while True e segue para o print final
        else:
            print("Opção inválida.")

    print("\nProdutos cadastrados:", produtos)


main()

