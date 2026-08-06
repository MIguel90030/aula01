"""
MODULO 2 - Tipos de dados, variaveis, operadores e I/O
Topico: Entrada e saida (I/O)

------------------------------------------------------------
TEORIA: ENTRADA E SAIDA (I/O)
------------------------------------------------------------
- SAIDA (output): a função print() exibe informações na tela.
- ENTRADA (input): a função input() lê o que o usuário digita
  no teclado. Ela SEMPRE retorna uma string - se você precisa
  de um número, é preciso converter (veja o arquivo
  03_tipos_de_dados_e_literais.py).

Como este script roda sem interação manual, deixamos o input()
comentado - descomente as linhas abaixo para testar no seu
terminal.
"""

nome = input("Qual é o seu nome? ")
idade_texto = input("Qual é a sua idade? ")
idade = int(idade_texto)
print(f"Ola, {nome}! Ano que vem voce tera {idade + 1} anos.")

# Simulando o mesmo resultado sem input(), para o script rodar
# sozinho:
nome = "Ana"
idade = 20
print(f"\nOla, {nome}! Ano que vem voce tera {idade + 1} anos.")

"""
------------------------------------------------------------
CUIDADO: O QUE VEM DO input() É SEMPRE STRING
------------------------------------------------------------
Quando você guarda o retorno de input() numa variável, essa
variável é do tipo str - mesmo que o usuário digite só números.
Usar esse valor direto, sem converter, causa problemas quando
você espera um comportamento numérico.
"""

idade_texto = input("Qual é a sua idade? ")
print("\ntipo do valor vindo do input:", type(idade_texto))

# PROBLEMA 1: "soma" na verdade concatena, porque ainda é string
print(idade_texto + idade_texto)   # ex: "2020" (concatenação, não 40)

# PROBLEMA 2: comparar como string usa ordem alfabética, não numérica
numero1_texto = input("Digite um número (ex: 9): ")
numero2_texto = input("Digite outro número (ex: 10): ")
print(numero1_texto > numero2_texto)             # True -> compara caractere a caractere ("9" > "1")
print(int(numero1_texto) > int(numero2_texto))   # False -> comparação numérica correta, depois de converter

# PROBLEMA 3: operações aritméticas quebram, pois str não soma com int
# print(idade_texto + 1)   # TypeError: can only concatenate str (not "int") to str

# SOLUCAO: converter para o tipo certo antes de usar
idade = int(idade_texto)
print(idade + idade)   # 40 (soma numérica de verdade, agora que é int)

