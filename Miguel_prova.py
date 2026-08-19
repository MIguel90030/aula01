"""

Voce foi contratado(a) como Lider de Projetos de TI na empresa
DataFlex Sistemas. A empresa fechou contrato com um banco parceiro
para desenvolver, de forma progressiva, um simulador de caixa
eletronico (ATM) completo, usado no treinamento de novos
funcionarios. Ao longo da situacao de aprendizagem, o programa
evolui passo a passo - dos tipos de dados e operacoes basicas as
estruturas de decisao, lacos, funcoes, dicionarios e tratamento de
excecoes - ate a entrega da versao final completa (com login por
PIN, menu em loop, funcoes com retorno e extrato formatado).

Esta prova retoma cada uma dessas etapas: os exercicios 1 a 7
praticam isoladamente os conceitos usados na construcao do
simulador, e os exercicios 8, 9 e 10 sao encadeados, reproduzindo
em miniatura a evolucao pedida no projeto - construa o exercicio 8
e depois evolua o MESMO codigo nos exercicios 9 e 10.

Escreva o codigo de cada exercicio logo abaixo do enunciado dele.
"""

# ----------------------------------------------------------------
# EXERCICIO 1 - Variaveis e tipos de dados
# ----------------------------------------------------------------
# Crie 2 variaveis: numero_conta (int) e saldo (float), simulando
# os dados de uma conta consultada no caixa eletronico.
# Imprima cada uma junto com seu tipo, usando type().
# ----------------------------------------------------------------
numero_conta = 123456
saldo = 1500.75
print(f"Numero da conta: {numero_conta} (tipo: {type(numero_conta)})")
print(f"Saldo: {saldo} (tipo: {type(saldo)})")




# ----------------------------------------------------------------
# EXERCICIO 2 - Operadores
# ----------------------------------------------------------------
# Crie tres variaveis: saldo_atual, valor_saque e valor_deposito
# (numeros).
# Imprima: o saldo apos o saque (saldo_atual - valor_saque),
# o saldo apos o deposito (saldo_atual + valor_deposito)
# e se ha saldo suficiente para o saque, imprimindo o resultado
# da comparacao saldo_atual > valor_saque (um valor booleano,
# True ou False).
# ----------------------------------------------------------------
saldo_atual = 1500.75
valor_saque = 200.00
valor_deposito = 500.00

print(f"Saldo apos o saque: {saldo_atual - valor_saque}")
print(f"Saldo apos o deposito: {saldo_atual + valor_deposito}")
print(f"Ha saldo suficiente para o saque: {saldo_atual > valor_saque}")

# ----------------------------------------------------------------
# EXERCICIO 3 - Estruturas de decisao (if/elif/else)
# ----------------------------------------------------------------
# Peça ao usuario o valor do saque com input() e classifique a
# operacao de acordo com as regras do caixa eletronico:
#   valor <= 600           -> "Saque liberado"
#   valor > 600 e <= 1000   -> "Saque liberado, mas com tarifa extra"
#   valor > 1000            -> "Saque nao permitido nesse caixa"
# ----------------------------------------------------------------
valor_saque_usuario = float(input("Digite o valor do saque: "))

if valor_saque_usuario <= 600:
    print('saque liberado')
elif valor_saque_usuario <= 1000:
    print('saque liberado, mas com tarifa extra')
else:
    print('saque nao permitido nesse caixa')

# ----------------------------------------------------------------
# EXERCICIO 4 - Laco for
# ----------------------------------------------------------------
# O caixa eletronico vai dispensar as notas abaixo em um saque.
# Use um for para imprimir cada nota entregue e, ao final, o
# valor total sacado (soma de todas as notas).
#
# notas = [100, 100, 50, 20, 10]
# ----------------------------------------------------------------
for nota in [100, 100, 50, 20, 10]:
    print(f'nota: {nota}')
    print(f'valor total sacado: {sum([100, 100, 50, 20, 10])}')



# ----------------------------------------------------------------
# EXERCICIO 5 - Laco while
# ----------------------------------------------------------------
# Use um "while" para simular varios depositos: peça um valor de
# deposito ao usuario ate que ele digite o numero 0 (para encerrar
# o atendimento). A cada valor digitado, imprima o dobro dele,
# simulando uma promocao de "deposito em dobro".
# ----------------------------------------------------------------
while True: 
    valor_deposito_usuario = float(input('digite o valor do deposito (0 para encerrar):'))
    if valor_deposito_usuario == 0:
        break
    print(f'o dobro do valor depositado é: {valor_deposito_usuario * 2}')


# ----------------------------------------------------------------
# EXERCICIO 6 - Listas
# ----------------------------------------------------------------
# Parta da lista "fila = ["Ana", "Bruno", "Carla"]", que representa
# os clientes aguardando para usar o caixa eletronico. Adicione
# "Diego" ao final da fila (append) e imprima a fila completa e o
# nome do proximo cliente a ser atendido (primeiro da fila).
# ----------------------------------------------------------------
fila = ['ana', 'bruno', 'carla']
fila.append('diego')
print(f'Fila completa: {fila}')
print(f'Proximo cliente a ser atendido: {fila[0]}')


# ----------------------------------------------------------------
# EXERCICIO 7 - Funcoes
# ----------------------------------------------------------------
# Crie uma funcao "calcular_media(lista)" que receba uma lista com
# os valores dos saques feitos no caixa eletronico durante o dia e
# retorne a media desses saques. Teste a funcao com uma lista de
# sua escolha e imprima o resultado.
# ----------------------------------------------------------------
def calcular_media(lista):
    if lista:
        return sum(lista) / len(lista)
    else:
        return 0 
    print(f'media dos saques: {calcular_meddia}')


# ================================================================
# EXERCICIOS 8, 9 e 10 - CAIXA ELETRONICO (aplicado, igual a aula)
# Estes 3 exercicios sao encadeados: construa o exercicio 8,
# depois evolua o MESMO codigo nos exercicios 9 e 10.
# ================================================================

# ----------------------------------------------------------------
# EXERCICIO 8 - Menu basico (while + if, sem funcoes)
# ----------------------------------------------------------------
# Construa do zero um simulador de caixa eletronico usando
# "while True" e uma variavel "saldo" comecando em 0
# (sem usar funcoes ainda):
#   1 - Depositar (pede o valor e soma ao saldo)
#   2 - Sacar (pede o valor; so permite se houver saldo suficiente)
#   3 - Consultar saldo
#   4 - Sair (break)
# Trate a opcao invalida com um "else".
# ----------------------------------------------------------------
while True:
    print('\n1 - depositar')
    print('2 - sacar')
    print('3 - consultar saldo')
    print('4 - sair')
    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        valor = float(input("Valor do deposito: "))
        saldo += valor
    elif opcao == "2":
        valor = float(input("Valor do saque: "))
        if valor <= saldo:
            saldo -= valor
        else:
            print("Saldo insuficiente.")
    elif opcao == "3":
        print(f"Saldo atual: {saldo}")
    elif opcao == "4":
        break
    else:
        print("Opcao invalida.")

# ----------------------------------------------------------------
# EXERCICIO 9 - Refatorando em funcoes
# ----------------------------------------------------------------
# Pegue a logica de deposito e saque do exercicio 8 e REFATORE:
# crie uma funcao "depositar(saldo, valor)" e uma funcao
# "sacar(saldo, valor)", cada uma retornando o novo saldo. Teste
# as duas funcoes chamando-as diretamente com valores de sua
# escolha e imprima o saldo resultante de cada chamada.
# ----------------------------------------------------------------
def depositar(saldo, valor):
    return saldo + valor

def sacar(saldo, valor):
    return saldo - valor
print(f'saldo apos o deposito: {depositar(1500.75, 500.00)}')
print(f'saldo apos o saque: {sacar(1500.75, 200.00)}')


# ----------------------------------------------------------------
# EXERCICIO 10 - Tratamento de excecao
# ----------------------------------------------------------------
# Abaixo esta pronto o menu do caixa, que ja CHAMA as funcoes
# "depositar" e "sacar", alem de mais duas funcoes auxiliares:
# "exibir_menu" e "consultar_saldo". Porem as funcoes "depositar"
# e "sacar" NAO estao definidas aqui: primeiro copie (ou reescreva)
# para este arquivo as funcoes "depositar(saldo, valor)" e
# "sacar(saldo, valor)" que voce criou no exercicio 9, antes da
# funcao "main()".
# Depois, sua tarefa e acrescentar o tratamento de excecao: use
# try/except ao pedir o valor de deposito ou saque nos pontos
# marcados com "TODO". Se o usuario digitar algo que nao seja um
# numero, capture o ValueError, mostre uma mensagem de erro e volte
# para o menu normalmente, sem quebrar o programa.
# ----------------------------------------------------------------

def exibir_menu():
    print("\n1 - Depositar")
    print("2 - Sacar")
    print("3 - Consultar saldo")
    print("4 - Sair")


def consultar_saldo(saldo):
    print(f"Saldo atual: {saldo}")


def main():
    saldo = 0
    def depositar(saldo, valor):return saldo + valor

def sacar(saldo, valor):
    return saldo - valor
print(f'saldo apos o deposito: {depositar(1500.75, 500.00)}')
print(f'saldo apos o saque: {sacar(1500.75, 200.00)}')

while True:
        exibir_menu()
        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            # TODO: use try/except para capturar ValueError caso o
            # usuario digite um valor que nao seja numero
            try:
                valor = float(input("Valor do deposito: "))
            except ValueError:
                print("Valor invalido. Por favor, digite um numero.")
                continue
            # TODO: chame a funcao depositar aqui
            saldo = depositar(saldo, valor)
        elif opcao == "2":
            # TODO: use try/except para capturar ValueError caso o
            # usuario digite um valor que nao seja numero
            try:
                valor = float(input("Valor do saque: "))
            except ValueError:
                print("Valor invalido. Por favor, digite um numero.")
                continue
            # TODO: chame a funcao sacar aqui
            saldo = sacar(saldo, valor)

        elif opcao == "3":
            consultar_saldo(saldo)

        elif opcao == "4":
            break

        else:
            print("Opcao invalida.")


main()
