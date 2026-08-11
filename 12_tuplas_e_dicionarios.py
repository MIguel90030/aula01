"""
MODULO 4 - Funcoes, tuplas, dicionarios e tratamento de excecoes
Topico: Tuplas e dicionarios

------------------------------------------------------------
TEORIA: TUPLAS
------------------------------------------------------------
Uma TUPLA é parecida com uma lista - é uma coleção ORDENADA de
valores - mas é IMUTAVEL: depois de criada, não é possível
adicionar, remover ou alterar seus itens. Tuplas são escritas
entre parênteses ().

Use tuplas quando os dados não devem mudar (ex: coordenadas,
dias da semana, um registro fixo).
"""

coordenada = (10, 20)
print("Tupla:", coordenada)
print("Primeiro valor:", coordenada[0])
print("Segundo valor:", coordenada[1])

# Descomente para ver o erro - tuplas nao podem ser alteradas:
# coordenada[0] = 99   -> TypeError: 'tuple' object does not support item assignment

# "Desempacotar" uma tupla em variáveis separadas:
x, y = coordenada
print(f"x = {x}, y = {y}")

"""
------------------------------------------------------------
TEORIA: DICIONARIOS
------------------------------------------------------------
Um DICIONARIO guarda dados como pares CHAVE: VALOR, em vez de
posições numéricas. Isso torna a busca por um dado muito mais
direta - em vez de lembrar a posição, você usa um nome (chave).
Dicionários são escritos entre chaves {}.
"""

aluno = {
    "nome": "Ana",
    "idade": 20,
    "curso": "Fundamentos do Python 1",
}

print("\nDicionario completo:", aluno)
print("Nome do aluno:", aluno["nome"])
print("Idade do aluno:", aluno["idade"])

# Adicionando ou alterando uma chave:
aluno["nota_final"] = 8.5
print("Depois de adicionar nota_final:", aluno)

aluno["idade"] = 21   # alterando um valor existente
print("Depois de atualizar a idade:", aluno)

# Removendo uma chave:
del aluno["curso"]
print("Depois de remover 'curso':", aluno)

print("\n--- Percorrendo um dicionario ---")
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")

print("\n'nome' existe no dicionario?", "nome" in aluno)
print("'curso' existe no dicionario?", "curso" in aluno)

# .get() busca uma chave sem gerar erro caso ela não exista:
print("Buscando 'telefone' com get():", aluno.get("telefone", "nao informado"))

"""
EXERCICIO SUGERIDO
------------------------------------------------------------
1. Crie uma tupla com os 4 módulos deste curso e imprima cada
   um usando um laço for.
"""

modulos = ("Fundamentos do Python 1", "Fundamentos do Python 2", "Fundamentos do Python 3", "Fundamentos do Python 4")
for modulo in modulos:
    print(modulo)

"""
2. Crie um dicionário representando um produto (nome, preço,
   quantidade em estoque) e calcule o valor total em estoque
   (preço * quantidade).
   """


"""
3. Qual a principal diferença prática entre usar uma lista de
   tuplas e um dicionário para guardar vários alunos e notas?
"""
