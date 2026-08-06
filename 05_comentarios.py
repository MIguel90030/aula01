"""
MODULO 2 - Tipos de dados, variaveis, operadores e I/O
Topico: Comentarios

------------------------------------------------------------
TEORIA: COMENTARIOS
------------------------------------------------------------
Comentários são trechos de texto que o Python IGNORA na hora
de executar o código. Servem só para explicar o código para
quem está lendo (inclusive você mesmo, no futuro).

# -> COMENTARIO DE UMA LINHA
Tudo que vem depois do # até o final da linha é ignorado.

''' ''' -> COMENTARIO DE VARIAS LINHAS (ou docstring)
Na verdade, três aspas duplas (ou simples) criam uma STRING
comum em Python. Quando essa string fica "solta" no código,
sem ser atribuída a nada, ela não tem efeito nenhum na
execução - funcionando na prática como um comentário de
várias linhas. Também é usada como docstring (documentação)
no topo de arquivos, funções e classes.

DIFERENCA PRINCIPAL:
    - #        -> sempre um comentário, vale só para 1 linha.
    - ''' ''' -> é uma STRING (não um comentário de verdade).
      Se estiver solta no código, é ignorada como comentário,
      mas se for atribuída a uma variável ou usada como primeira
      linha de uma função/classe, ela é a docstring e pode ser
      lida em tempo de execução (ex: minha_funcao.__doc__).
"""

# isto é um comentário de uma linha
print("ola")  # também pode vir depois de um código, na mesma linha

"""
isto é um comentário de várias linhas.
Pode ocupar quantas linhas forem necessárias,
até fechar com três aspas novamente.
"""
print("mundo")

