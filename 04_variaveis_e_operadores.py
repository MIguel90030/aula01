"""
MODULO 2 - Tipos de dados, variaveis, operadores e I/O
Topico: Variaveis e operadores

------------------------------------------------------------
TEORIA: VARIAVEIS
------------------------------------------------------------
Uma variável é um "rótulo" que guarda um valor na memória para
que possamos usá-lo depois. Em Python não é preciso declarar o
tipo - ele é inferido automaticamente a partir do valor.

Python é uma linguagem DINAMICAMENTE TIPADA. Isso significa que
o tipo de uma variavel é definido em tempo de execução, com
base no valor que ela recebe - e não precisa ser declarado
antecipadamente como em linguagens estaticamente tipadas
(ex: Java, C). Alem disso, a mesma variavel pode trocar de tipo
livremente ao longo do programa, bastando atribuir um novo valor
de outro tipo a ela:

    x = 10       # aqui x é int
    x = "dez"    # agora x é str, sem nenhum erro

Isso torna o Python mais flexivel e rapido de escrever, mas exige
mais cuidado do programador, já que erros de tipo (como somar um
numero com um texto) só aparecem quando o codigo é executado, e
não antes, como aconteceria em uma linguagem estaticamente tipada.

BOAS PRATICAS ao nomear variáveis:
    - Use nomes descritivos (preco, quantidade) em vez de
      nomes genéricos (x, y, z).
    - Use letras minúsculas e separe palavras com "_"
      (snake_case): total_de_vendas.
    - Não comece o nome com número, nem use espaços ou acentos.
"""

var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
print(var)
print(account_balance)
print(client_name)

# print = "Olá, mundo!" # quebra o código

#print(n_existe) # -> não se pode usar uma variável que não existe

print(f'variavel a impimir: {var}') # -> f-string (formatação de string ) para imprimir vairável

# atribuindo um novo valor a uma variável
var = 1
print(var)
var = 'texto'
print(var)

# atribuindo valor a mais de uma variável ao mesmo tempo
x, y, z = 10, 20, 30
print(x, y, z)

"""
------------------------------------------------------------
TEORIA: OPERADORES
------------------------------------------------------------
ARITMETICOS:  +  -  *  /  // (divisão inteira)  % (resto)  ** (potência)
COMPARACAO:   ==  !=  >  <  >=  <=
LOGICOS:      and  or  not
"""

a = 10
b = 3
print("\n--- Operadores aritméticos ---")
print("a + b  =", a + b)
print("a - b  =", a - b)
print("a * b  =", a * b)
print("a / b  =", a / b)    # divisão real (retorna float)
print("a // b =", a // b)   # divisão inteira (arredonda para baixo)
print("a % b  =", a % b)    # resto da divisão
print("a ** b =", a ** b)   # potência (a elevado a b)

"""
ORDEM DOS OPERADORES ARITMETICOS (PRECEDENCIA)
------------------------------------------------------------
Assim como na matemática, o Python segue uma ordem para decidir
qual operação executar primeiro numa expressão com vários
operadores:

    1º) ** (potência)
    2º) * / // % (multiplicação, divisão, divisão inteira, resto)
    3º) + - (soma e subtração)

Operações de mesma prioridade são resolvidas da esquerda para a
direita. Use parênteses () para forçar uma ordem diferente ou
para deixar a expressão mais clara.
"""
print("\n--- Ordem dos operadores aritméticos ---")
print("2 + 3 * 4     =", 2 + 3 * 4)      # 14 -> multiplicação antes da soma
print("(2 + 3) * 4   =", (2 + 3) * 4)    # 20 -> parênteses mudam a ordem
print("2 * 3 ** 2    =", 2 * 3 ** 2)     # 18 -> potência antes da multiplicação
print("10 - 4 / 2    =", 10 - 4 / 2)     # 8.0 -> divisão antes da subtração

print("\n--- Operadores de comparacao ---")
print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)

print("\n--- Operadores logicos ---")
print("(a > 5) and (b > 5):", (a > 5) and (b > 5))  # and -> só é True se AMBOS os lados forem True (a>5 é True, b>5 é False -> resultado False)
print("(a > 5) or  (b > 5):", (a > 5) or (b > 5))   # or  -> é True se PELO MENOS UM dos lados for True (a>5 é True -> resultado True)
print("not (a > 5):", not (a > 5))                  # not -> inverte o valor logico (a>5 é True -> not True = False)

