"""
MODULO 2 - Tipos de dados, variaveis, operadores e I/O
Topico: Tipos de dados e literais

------------------------------------------------------------
TEORIA
------------------------------------------------------------
Todo valor em Python tem um TIPO, que define o que pode ser
feito com ele. Os tipos basicos (primitivos) mais usados sao:

    int    -> numeros inteiros           10, -3, 2024
    float  -> numeros decimais           3.14, -0.5
    str    -> texto (string)             "Python", 'ola'
    bool   -> valor logico               True, False

Além disso, existem tipos de COLECAO, que guardam varios
valores, como a list (lista) 

Um LITERAL é a forma como escrevemos um valor diretamente no
código - por exemplo, 10, "Python" e True sao literais dos
tipos int, str e bool.

A função type() mostra o tipo de um valor.
"""

print('2') # -> posso fazer concatenação
print(2) # -> posso fazer soma 



print("Valor:", 10, "-> tipo:", type(10))
print("Valor:", 3.14, "-> tipo:", type(3.14))
print("Valor:", "Python", "-> tipo:", type("Python"))
print("Valor:", True, "-> tipo:", type(True))


"""
NÚMEROS INTEIROS EM DIFERENTES BASES

"""
print("Valor em binário:", bin(10))
print("Valor em binário - > decimal:", 0b1010) # -> 20 em binário
print("Valor em octal:", oct(20))
print("Valor em octal -> decimal:", 0o24) # -> 20 em octal
print("Valor em hexadecimal (sem prefixo):", hex(25)) # -> 25 em hexadecimal
print("Valor em hexadecimal -> decimal:", 0x19) # -> 25 em hexadecimal

help(bin) # -> ajuda sobre a função bin()

"""
FLOAT EM DIFERENTES FORMAS DE ESCRITA 

"""
print("\n--- Float em diferentes formas de escrita ---")

print(0.0000000000000000000001)
print(f"{0.0000000000000000000001:.22f}")

print(f'{0.256:.1%}') # formatando como porcentagem (multiplica por 100 e adiciona %)

print(f'{-5.1:+}') # colocando sinal no valor
print(f'{5.1:+}') # colocando sinal no valor 


"""
STRING COM FORMATACAO (f-string)

"""
print("\n--- String com formatacao (f-string) ---")
print(f"{'texto alinhado a direita':>50}")
print(f"{'texto alinhado a esquerda':<50}")
print(f'{"texto centralizado":^50}\n')

# Métodos string - propriedades e funções que podem ser aplicadas a strings
print('nome'.upper()) # -> deixa todas as letras maiúsculas
print('nome'.lower()) # -> deixa todas as letras minúsculas
print('nome'.capitalize()) # -> deixa a primeira letra maiúscula e o resto minúsculo
print('nome composto'.title()) # -> deixa a primeira letra de cada palavra maiúscula e o resto minúsculo
print('nOmE'.swapcase()) # -> inverte o caso de todas as letras
print('nome'.replace('o', 'a')) # -> substitui todas as ocorrências de 'o' por 'a'
print('nome'.replace('o', 'a').upper()) # -> substitui e deixa todas as letras maiúsculas

"""
REPRESENTAÇÃO DE BOOLEANOS

O tipo bool só tem dois valores possíveis: True e False. Eles
representam "verdadeiro" e "falso", e são o resultado de
comparações e expressões lógicas.
"""
print("\n--- Booleanos ---")
print(10 > 5)          # True  -> 10 é maior que 5
print(10 == 5)         # False -> 10 não é igual a 5
print(bool(0))         # False -> 0 é considerado "falso"
print(bool("Python"))  # True  -> qualquer string não-vazia é "verdadeira"


"""
------------------------------------------------------------
CONVERSAO ENTRE TIPOS (TYPE CASTING)
------------------------------------------------------------
Às vezes precisamos converter um valor de um tipo para outro.
Usamos as funções int(), float(), str() e bool() para isso.
"""

print("\n--- Conversao de tipos ---")
print("42", "->", type("42"))
print(int("42"), "->", type(int("42")))

# Cuidado: nem toda conversão é possível!
# int("banana") geraria um erro (ValueError) - veja o arquivo


print(float(10))     # 10 -> 10.0
print(str(3.14))     # 3.14 (agora como texto)
print(bool(0))        # False (0 é considerado "falso")
print(bool(1))        # True  (qualquer numero != 0 é "verdadeiro")

