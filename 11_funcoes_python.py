"""
MODULO 4 - Funcoes, tuplas, dicionarios e tratamento de excecoes
Topico: Funcoes, parametros, retorno e escopo de variaveis

------------------------------------------------------------
TEORIA
------------------------------------------------------------
Uma FUNÇÃO é um bloco de código nomeado que agrupa uma lógica
para ser REUTILIZADA - em vez de repetir o mesmo código várias
vezes, você escreve uma vez e "chama" a função sempre que
precisar.

    def nome_da_funcao(parametros):
        # bloco de codigo
        return valor   # opcional

- PARAMETROS são os valores que a função recebe como entrada.
- RETURN devolve um valor para quem chamou a função; uma
  função sem return devolve None.
"""

def saudacao(nome):
    """Recebe um nome e imprime uma saudacao personalizada."""
    print(f"Ola, {nome}! Bem-vindo ao curso de Python.")

saudacao("Carlos")
saudacao("Mariana")

"""
------------------------------------------------------------
FUNCOES QUE RETORNAM VALOR
------------------------------------------------------------
"""

def media(a, b):
    """Recebe dois numeros e retorna a media entre eles."""
    return (a + b) / 2

resultado = media(7, 9)
print("\nMedia entre 7 e 9:", resultado)

# Como a função retorna um valor, podemos usá-lo em expressões:
print("Media + 1:", media(7, 9) + 1)

"""
------------------------------------------------------------
NUMERO VARIAVEL DE ARGUMENTOS (*args)
------------------------------------------------------------
Às vezes não sabemos de antemão quantos valores vão ser
passados - por exemplo, cadastrar vários produtos de uma vez,
sem saber se serão 2 ou 10. Nesse caso usamos * (UM asterisco)
antes do nome do parâmetro. Dentro da função, esse parâmetro
vira uma TUPLA com todos os valores recebidos.

"""

def cadastrar_produtos(*produtos):
    """Recebe uma quantidade qualquer de nomes e devolve como lista."""
    return list(produtos)

lista_produtos = cadastrar_produtos("Caneta", "Caderno", "Borracha", "Lápis")
print("\nProdutos cadastrados:", lista_produtos)

# Mesma função, mas agora coletando os nomes digitados pelo usuário
# até ele digitar "exit":
nomes_digitados = []
while True:
    nome_produto = input("\nDigite um produto (ou 'exit' para parar): ")
    if nome_produto.lower() == "exit":
        break
    nomes_digitados.append(nome_produto)

print("Produtos cadastrados:", cadastrar_produtos(*nomes_digitados))
print("teste: ",*nomes_digitados)  # imprime os nomes sem colchetes, separados por espaço

"""
------------------------------------------------------------
PARAMETROS COM VALOR PADRAO
------------------------------------------------------------
Você pode definir um valor padrão para um parâmetro - se quem
chamar a função não informar esse argumento, o padrão é usado.
"""

def calcular_total(preco, quantidade=1):
    return preco * quantidade

print("\nTotal (quantidade padrao=1):", calcular_total(10))
print("Total (quantidade=3):", calcular_total(10, 3))

"""
------------------------------------------------------------
ESCOPO DE VARIAVEIS
------------------------------------------------------------
Uma variável criada DENTRO de uma função só existe ali dentro
- é o chamado ESCOPO LOCAL. Fora da função, ela não existe.
Uma variável criada fora de qualquer função tem ESCOPO GLOBAL
e pode ser lida (mas não alterada diretamente) de dentro de
funções.
"""

x_global = 100

def exemplo_de_escopo():
    x_local = 5   # só existe dentro desta funcao
    print("\nDentro da funcao - x_local:", x_local)
    print("Dentro da funcao - x_global (leitura):", x_global)

    global y   # avisa o Python que "y" aqui é a variável global, não uma local nova
    y = 999
    print("Dentro da funcao - y alterado para:", y)

exemplo_de_escopo()
print("Fora da funcao - x_global:", x_global)
print("Fora da funcao - y:", y)   # também mudou, porque usamos "global y"

# Descomente a linha abaixo para ver o erro: x_local não existe
#ora da função onde foi criada.
#print(x_local)

"""
------------------------------------------------------------
EXEMPLO PRATICO - QUEBRANDO UM PROGRAMA EM FUNCOES
------------------------------------------------------------
Um programa com um menu geralmente cresce muito se tudo fica
dentro do mesmo "while True". A solução é dar um nome a cada
operação e transformá-la em função - o menu só decide QUAL
função chamar.

O que o programa faz:
- Exibe um menu com 5 opções e lê a escolha do usuário.
- Opção 1: registra uma movimentação (valor positivo = entrada,
  negativo = saída) na lista "historico".
- Opção 2: soma tudo e mostra o saldo total.
- Opção 3: mostra a maior entrada (max) e a maior saída (min).
- Opção 4: mostra a lista completa de movimentações registradas.
- Opção 5: encerra o programa.
- Enquanto nenhuma dessas opções é escolhida, o menu continua
  se repetindo (loop "while True" dentro de main()).

"""

def exibir_menu():
    print("\n--- Menu de Movimentações ---")
    print("1 - Registrar movimentação")
    print("2 - Ver saldo total")
    print("3 - Ver maior entrada e maior saída")
    print("4 - Ver histórico completo")
    print("5 - Sair")
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
        else:
            print("Opção inválida, tente novamente")

main()


