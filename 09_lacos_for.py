"""
MODULO 3 - Estruturas de dados, listas e valores booleanos
Topico: Laco de repeticao (for)

------------------------------------------------------------
TEORIA: FOR
------------------------------------------------------------
O laço for repete um bloco de código um número DEFINIDO de
vezes, percorrendo os itens de uma sequência (lista, string,
intervalo de números etc).

A função range(inicio, fim, passo) gera uma sequência de
números - o "fim" NÃO é incluído.
"""

print("--- for com range() ---")
for numero in range(1, 6):   # 1, 2, 3, 4, 5  (6 fica de fora)
    print("Numero:", numero)

print("\n--- for percorrendo uma string ---")
for letra in "Python":
    print(letra, end=" ")
print()  # apenas para pular linha no final

frase = 'Python é uma linguagem de progração de alto nível interpretada'
print("\n--- for percorrendo uma lista ---")
for letra in range(len(frase)):
    print(frase[letra], end=" ")

print('\n--percorrendo a frade de trás para frente')
for letra in range(len(frase)-1, -1,-2):
    print(frase[letra], end=" ")

"""
------------------------------------------------------------
BREAK E CONTINUE (também funcionam no for)
------------------------------------------------------------
break    -> interrompe o laço imediatamente
continue -> pula para a proxima repeticao do laço
"""

print("\n--- break ---")
for n in range(1, 10):
    if n == 4:
        break          # para o laço assim que n chega a 4
    print("n =", n)

print("\n--- continue ---")
for n in range(1, 6):
    if n == 3:
        continue        # pula o print quando n é 3
    print("n =", n)


