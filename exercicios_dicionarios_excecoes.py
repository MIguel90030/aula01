"""
DICIONÁRIOS E EXCEÇÕES - Exercícios

"""

"""
------------------------------------------------------------
EXERCICIO 1 - Criando um dicionario
------------------------------------------------------------
Crie um dicionario chamado "aluno" com as chaves "nome", "idade"
e "curso" (escolha os valores que quiser). Depois imprima o
dicionario completo com print().
"""
aluno = {
    'nome': 'Miguel',
    'idade': 20,
    'curso': 'python'

}
print(aluno)


"""
------------------------------------------------------------
EXERCICIO 2 - Percorrendo um dicionario com FOR
------------------------------------------------------------
Use o dicionario "estoque" abaixo (pode copiar) e percorra ele
com um for + .items(), imprimindo cada produto e sua quantidade
no formato: "Caneta -> 10 unidades".

estoque = {"Caneta": 10, "Caderno": 5, "Borracha": 20}
"""
estoque = {'caneta': 10, 'caderno': 5, 'borracha': 20}
for produto, quantidade in estoque.items():
    print(f'{produto} -> {quantidade} unidades')


"""
------------------------------------------------------------
EXERCICIO 3 - Try/except simples
------------------------------------------------------------
Peça ao usuário para digitar um número com input() e tente
converter o valor para int() dentro de um try. Se o usuário
digitar algo que não seja número, capture o ValueError e mostre
uma mensagem de erro (sem deixar o programa quebrar).
"""
input_numero = input('digite um numero:')

try:
    numero = int(input_numero)
    print(f"Você digitou o número: {numero}")
except ValueError:
    print("Erro: Por favor, digite um número válido.")


"""
------------------------------------------------------------
EXERCICIO 4 - Repetindo até digitar certo (while + try/except)
------------------------------------------------------------
Crie um dicionário "cliente" com as chaves "nome" e "telefone".
Dentro de um "while True", peça ao usuário para digitar uma das
chaves do dicionário e tente imprimir o valor correspondente.
Use try/except para capturar o erro quando a chave não existir
(repetindo a pergunta) e um "break" para sair do laço assim que
o usuário digitar uma chave válida.
"""
cliente = {'nome': 'João', 'telefone': '123456789'}

while True:
    chave = input("Digite uma chave (nome ou telefone): ")
    try:
        print(f"{chave}: {cliente[chave]}")
        break
    except KeyError:
        print("Chave inválida. Tente novamente.")

"""
------------------------------------------------------------
EXERCICIO 5 (APLICADO - exemplo prático)
------------------------------------------------------------
Abaixo está o mesmo exemplo do menu de movimentações visto no
módulo de funções (a lista "historico" é passada como PARÂMETRO
para cada função). Copie/rode o código como está e depois
ADICIONE uma nova opção ao menu (opção "7") que utilize um
DICIONÁRIO, por exemplo:

  "Cadastrar produto" - crie um dicionário "produtos" (fora das
  funções, igual ao "historico") e uma função que peça o id e o
  nome de um produto, guardando no dicionário com o id (convertido
  para número) como chave e o nome como valor. Trate o ValueError
  caso o id não seja um número.

Lembre-se: sua nova opção também deve virar uma FUNÇÃO nova
(chamada a partir de "main()"), igual às funções já existentes -
só que essa recebe o dicionário "produtos" como parâmetro, em vez
do "historico".
"""

def exibir_menu():
    print("\n--- Menu de Movimentações ---")
    print("1 - Registrar movimentação")
    print("2 - Ver saldo total")
    print("3 - Ver maior entrada e maior saída")
    print("4 - Ver histórico completo")
    print("5 - Sair")
    print("6 - Limpar histórico")
    print("7 - Cadastrar produto")
    opcao = input("Escolha uma opção: ")
    return opcao

def registrar_movimentacao(historico):
    valor = float(input("Valor da movimentação (positivo=entrada, negativo=saída): "))
    historico.append(valor)
    print("Movimentação registrada!")

def ver_saldo_total(historico):
    if historico:
        print(f"Saldo total: {sum(historico):.2f}")
    else:
        print("Nenhuma movimentação registrada.")

def ver_maior_entrada_saida(historico):
    if historico:
        print(f"Maior entrada: {max(historico):.2f}")
        print(f"Maior saída: {min(historico):.2f}")
    else:
        print("Nenhuma movimentação registrada.")

def ver_historico(historico):
    print("Histórico completo:", historico)

def limpar_historico(historico):
    historico.clear()
    print("Histórico esvaziado.")

def main(): # main()- função principal que organiza o fluxo do programa
    historico = []
    while True:
        opcao = exibir_menu()

        if opcao == "1":
            registrar_movimentacao(historico)
        elif opcao == "2": 
            ver_saldo_total(historico)
        elif opcao == "3":
            ver_maior_entrada_saida(historico)
        elif opcao == "4":
            ver_historico(historico)
        elif opcao == "5":
            print("Encerrando...")
            break
        elif opcao == "6":
            limpar_historico(historico)
        elif opcao == "7":
            cadastrar_produto(produtos) # type: ignore
        else:
            print("Opção inválida, tente novamente")

main()
