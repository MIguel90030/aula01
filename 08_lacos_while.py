"""
MODULO 3 - Estruturas de dados, listas e valores booleanos
Topico: Laco de repeticao (while)

------------------------------------------------------------
TEORIA: WHILE
------------------------------------------------------------
O laço while repete um bloco de código ENQUANTO uma condição
for verdadeira. É útil quando não sabemos de antemão quantas
vezes o laço vai rodar.

CUIDADO: se a condição nunca se tornar falsa, o laço nunca
para - isso é chamado de "loop infinito". Sempre garanta que
algo dentro do laço eventualmente torne a condição False.
"""

print("--- while ---")
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1   # equivalente a: contador = contador + 1


# cuidado para não gerar um loop infinito!
# while True:
#     print('Estou preso em um loop infinito! (Ctrl+C para sair)')

"""
------------------------------------------------------------
BREAK E CONTINUE (também funcionam no while)
------------------------------------------------------------
break    -> interrompe o laço imediatamente
continue -> pula para a proxima repeticao do laço
"""

print("\n--- break no while ---")
numero = 0
while numero < 10:
    if numero == 4:
        break          # para o laço assim que numero chega a 4
    print("numero =", numero)
    numero += 1

print("\n--- continue no while ---")
numero = 0
while numero < 5:
    numero += 1
    if numero == 3:
        continue        # pula o print quando numero é 3
    print("numero =", numero)


# P[0]Y[1]T[2]H[3]O[4]N[5] - cada letra tem um índice, começando do 0
print('Python'[1])

# percorrendo uma string com while
print("\n--- percorrendo uma string com while ---")
texto = "Python"
tamanho = len(texto) # explicar a função len()
print(tamanho)

index =0
while index < tamanho:
    print(texto[index])
    index += 1

# percorrendo a mesma string de trás para frente
print("\n--- percorrendo uma string de trás para frente ---")
texto = "Python"
tamanho = len(texto) # explicar a função len()
index = tamanho - 1   # último índice válido é tamanho - 1, não tamanho
while index >= 0:
    print(texto[index])
    index -= 1   # decrementa até chegar em 0

# a mesma travessia de trás para frente, mas usando índice NEGATIVO
# -1 já é o último caractere, -2 o penúltimo, e assim por diante -
# então aqui percorremos de -1 até -tamanho (não até 0)
print("\n--- percorrendo com índice negativo ---")
index = -1
while index >= -tamanho:
    print(texto[index])
    index -= 1   # vai ficando mais negativo até chegar em -tamanho

# somando valores digitados pelo usuário, combinando input(),
# casting (float), operadores aritméticos e comparação
print("\n--- Somando valores digitados pelo usuário ---")
soma = 0.0
valor = input("Digite um valor para somar (digite 0 para parar): ")
valor = float(valor)

while valor != 0:
    soma += valor   # equivalente a: soma = soma + valor
    valor = input("Digite outro valor (digite 0 para parar): ")
    valor = float(valor)

print(f"Soma total: {soma:.2f}")

# validação de senha com número limitado de tentativas, combinando
# while, contador, comparação e break
print("\n--- Validação de senha com tentativas limitadas ---")
senha_correta = "1234"
tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    senha_digitada = input("Digite a senha: ")
    if senha_digitada == senha_correta:
        print("Senha correta! Acesso liberado.")
        break
    else:
        tentativas += 1
        print(f"Senha incorreta. Tentativas restantes: {max_tentativas - tentativas}")

if tentativas == max_tentativas:
    print("Número máximo de tentativas excedido. Acesso bloqueado.")

# Criando um menu de opções com while
while True:
    opcao = input("\nSelecione uma opção:\n[1] - Segunda Via de Fatura\n"
    "[2] - Pagamento\n[3] - Falar com atendente\n[4] - Encerrar\n")
    if opcao == '1':
        print("Entrou na opção Segunda via de fatura")
    elif opcao == '2':
        print("Entrou na opção Pagamento")
    elif opcao == '3':
        print("Entrou na opção Falar com atendente")
    elif opcao == '4':
        print("Encerrando...")
        break
    else:
        print("Opção inválida, tente novamente")
        continue

print("\nFim do programa")