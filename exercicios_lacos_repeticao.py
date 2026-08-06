"""
MODULO 3 - Estruturas de dados, listas e valores booleanos
Lista de exercicios (lacos de repeticao - while e for)

Escreva o codigo de cada exercicio abaixo do comentário
correspondente. As respostas ficam em
exercicios_lacos_repeticao_respostas.py.
"""

# ================================================================
# WHILE
# ================================================================

# ================================================================
# EXERCICIO 1 - while: números de 1 a 10
# ================================================================
# Use while para imprimir os números de 1 a 10.
print("--- while ---")
contador = 0
while contador < 11:
    print("Contador:", contador)
    contador += 1   # equivalente a: contador = contador + 1




# ================================================================
# EXERCICIO 2 - while True + break
# ================================================================
# Use while True junto com break para parar a repetição assim
# que um contador, que começa em 0 e aumenta 1 a cada volta,
# atingir o valor 7.
print("\n--- break no while ---")
numero = 0
while numero < 10:
    if numero == 7:
        break          # para o laço assim que numero chega a 7
    print("numero =", numero)
    numero += 1



# ================================================================
# EXERCICIO 3 - while: soma até digitar negativo
# ================================================================
# Peça valores numéricos ao usuário, um de cada vez, somando
# todos eles. O laço deve parar quando o usuário digitar um
# número negativo (use while, input(), conversão para float e
# comparação).
valor =  input ('digite seu valor')
valor = float(valor)
soma = 0 
while valor >=0:
    soma += valor
    valor = input('digite seu valor')
    valor = float(valor)

print('a soma dos valores digitados é:')




# ================================================================
# EXERCICIO 4 - while: senha com tentativas limitadas
# ================================================================
# Peça uma senha ao usuário, permitindo no máximo 3 tentativas.
# Se a senha digitada bater com uma senha correta guardada numa
# variável, mostre "Acesso liberado" e pare o laço; se as 3
# tentativas acabarem sem acertar, mostre "Acesso bloqueado".
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



# ================================================================
# EXERCICIO 5 - DESAFIO: menu de estoque com while True
# ================================================================
# Crie um menu de estoque com while True: 1 para Adicionar
# produto, 2 para Remover produto, 3 para Consultar quantidade
# em estoque, 4 para Sair. Use if/elif/else para tratar cada
# opção e break para encerrar o menu quando o usuário escolher
# "Sair". A quantidade em estoque deve ser atualizada conforme
# as opções 1 e 2 forem usadas.


# ================================================================
# FOR
# ================================================================

# ================================================================
# EXERCICIO 6 - for: números pares de 1 a 20
# ================================================================
# Use for com range() para imprimir todos os números pares de
# 1 a 20.
print("--- for com range() ---")
for numero in range(2, 20, 2):   # 2, 4, 6, 8, 10, 12, 14, 16, 18
    print("Numero:", numero)

# ================================================================
# EXERCICIO 7 - for: tabela de multiplicação
# ================================================================
# Peça um número ao usuário e use for com range() para imprimir
# a tabela de multiplicação desse número, de 1 a 10 (ex: para o
# número 5: "5 x 1 = 5", "5 x 2 = 10", etc.).


# ================================================================
# EXERCICIO 8 - for: contando ocorrências da letra "a"
# ================================================================
# Use for para percorrer uma palavra ou frase e contar quantas
# vezes a letra "a" aparece nela.


# ================================================================
# EXERCICIO 9 - for: break e continue combinados
# ================================================================
# Use for com range(1, 21) para imprimir os números de 1 a 20,
# mas pulando (continue) os múltiplos de 3 e parando (break)
# assim que chegar em 15.


# ================================================================
# EXERCICIO 10 - DESAFIO: total de compra com desconto
# ================================================================
# Peça ao usuário quantos produtos ele vai comprar (N). Use for
# com range(N) para pedir o preço de cada produto, um de cada
# vez, somando tudo num total. No final, se o total ultrapassar
# R$ 100, aplique 10% de desconto. Imprima o valor final da
# compra formatado com 2 casas decimais.
