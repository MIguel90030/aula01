"""
MODULO 3 - Estruturas de dados, listas e valores booleanos
Topico: Estruturas de decisao (if, elif, else)

------------------------------------------------------------
TEORIA
------------------------------------------------------------
Um programa muitas vezes precisa tomar decisões: "se tal coisa
acontecer, faça isso; senão, faça aquilo". Em Python isso começa
com a palavra-chave if:

    if condicao:
        # roda se a condicao for True
    else:
        # roda se a condicao for False (o "else" é opcional)

Para escrever a "condicao", vamos usar bastante os operadores de
comparação (==, !=, >, <, >=, <=) e os operadores lógicos
(and, or, not) que já vimos antes - aqui é onde eles realmente
ganham utilidade, decidindo qual caminho o programa vai seguir.

RELEMBRANDO:
    OPERADORES DE COMPARACAO (comparam dois valores e resultam
    num bool - True ou False):
        ==  -> igual a
        !=  -> diferente de
        >   -> maior que
        <   -> menor que
        >=  -> maior ou igual a
        <=  -> menor ou igual a

    OPERADORES LOGICOS (combinam ou invertem valores booleanos):
        and -> True somente se AMBOS os lados forem True
        or  -> True se PELO MENOS UM dos lados for True
        not -> inverte o valor (True vira False e vice-versa)

IMPORTANTE: em Python, os blocos são definidos por INDENTAÇÃO
(4 espaços é o padrão), não por chaves {} como em outras
linguagens. Isso torna o código mais legível, mas exige atenção.
"""

a = 10
b = 3


print("--- Cada operador de comparação usado com if ---")
if a == 10:
    print("a == 10  -> a é igual a 10")

if a != b:
    print("a != b   -> a é diferente de b")

if a > b:
    print("a > b    -> a é maior que b")

if b < a:
    print("b < a    -> b é menor que a")

if a >= 10:
    print("a >= 10  -> a é maior ou igual a 10")

if b <= 3:
    print("b <= 3   -> b é menor ou igual a 3")

print("\n--- Cada operador lógico usado com if ---")
if a > 5 and b > 0:
    print("and -> a é maior que 5 E b é maior que 0")

if a > 100 or b > 0:
    print("or  -> a é maior que 100 OU b é maior que 0")

if not (a > 100):
    print("not -> a NAO é maior que 100")

"""
------------------------------------------------------------
PROGRAMA COM IF / ELSE (MAIS DE UM IF)
------------------------------------------------------------
Podemos usar vários blocos if/else no mesmo programa, um atrás
do outro, quando as condições são independentes entre si (não
uma alternativa da outra).
"""

nota = 7.5
frequencia = 85

print("\n--- Programa com mais de um if/else ---")
if nota >= 6:
    print("Aprovado na nota")
else:
    print("Reprovado na nota")

# else:                   # else nunca pode estar sozinho 
#     print('teste')

if frequencia >= 75:
    print("Frequência OK")
else:
    print("Reprovado por falta")

"""
------------------------------------------------------------
TEORIA: ELIF
------------------------------------------------------------
Quando existem VÁRIAS condições que se excluem (só uma pode ser
verdadeira por vez), em vez de vários if/else separados, usamos
elif ("else if") para encadear as opções:

    if condicao:
        # roda se a condicao for True
    elif outra_condicao:
        # roda se a primeira for False e esta for True
    else:
        # roda se nenhuma condicao anterior foi True

Diferente de vários if soltos, o Python testa as condições do
elif NA ORDEM, e para no primeiro bloco que for True - os
demais nem são avaliados.
"""

print("\n--- Exemplo com elif ---")
if nota >= 9:
    conceito = "A"
elif nota >= 7:
    conceito = "B"
elif nota >= 6:
    conceito = "C"
else:
    conceito = "D"
print("Conceito final:", conceito)


print("\n--- Elif com condição composta (and) ---")
idade = 16
tem_documento = True

if idade >= 18 and tem_documento:
    print("Pode entrar no evento")
elif idade >= 16 and tem_documento:
    print("Pode entrar acompanhado de um responsavel")
else:
    print("Nao pode entrar")

# Menu de opções com elif
print('\n---Menu de opções com if/elif/else---')
opcao = input('Informe a operação desejada:\n[1]-Segunda Via de fatura\n'
'[2]-pagamento\n[3]-Falar com atendente\n[4]-Encerrar\n ')

if opcao == '1':
    print('Entrou na opção Segunda via de fatura')
elif opcao == '2':
    print('Entrou na opção Pagamento')
elif opcao == '3':
    print('Entrou na opção Falar com atendente')
elif opcao == '4':
    print('Entrou na opção Encerrar')
else:
    print('Opção inválida')