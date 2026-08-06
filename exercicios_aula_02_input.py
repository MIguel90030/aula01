"""
MODULO 2 - Tipos de dados, variaveis, operadores e I/O
Lista de exercicios com foco em input() (assuntos dos arquivos
03, 04, 05 e 06)

Escreva o codigo de cada exercicio num script separado.

------------------------------------------------------------
1. (Input + casting) Posto de combustível: use input() para
   perguntar o preço do litro e a quantidade de litros
   abastecidos. Converta os dois valores para float, calcule o
   valor total e imprima formatado com 2 casas decimais.
   """
# valor_gasolina = input('valor da gasolina')
# valor = input('qual o preço?')
# litro = input('quantos litros?')
# print(type(valor))
# valor = float(valor)
# print(type(valor))
# print(type(litro))
# valor = float(litro)
# print(type(litro))



"""
2. (Input + operadores aritméticos) Estacionamento: use input()
   para pedir a quantidade de horas que o carro ficou estacionado
   e o valor cobrado por hora. Converta para float, calcule o
   valor total (horas x valor por hora) e some uma taxa fixa de
   serviço de R$ 2,00. Imprima o valor final formatado.
   """
# valor_hora = input('qual valor da hora ?')
# tempo = input('quantas horas ficou ?')
# valor_hora_f = float(valor_hora)
# tempo_f = float(tempo)
# toal = (valor_hora_f * tempo_f) + 2.50




"""
3. (Input + comparação) Loja: use input() para pedir o valor
   total de um carrinho de compras e o limite disponível no
   cartão do cliente. Converta ambos para float e verifique, com
   um operador de comparação, se o valor do carrinho ultrapassa
   o limite disponível. Imprima o resultado da comparação.
   """
# limite_disponivel = input('Seu limite')
# limite_disponivel_f = float('limite_disponivel')

"""
4. (Input + lógicos) Cinema: use input() para perguntar a idade
   do espectador e se ele está acompanhado de um adulto
   (respondendo "sim" ou "nao"). Verifique, usando and, se a
   idade é menor que 12 E a resposta sobre estar acompanhado foi
   "nao" - isso indicaria que ele não pode entrar sozinho.
   """
idade = int(input('Qual sua idade?'))
acompanhado_de_adulto = input('Voce esta acompanhado de um adulto?')
condicao = (idade > 12) and (acompanhado_de_adulto == 'nao') 
print(condicao)


"""
5. (DESAFIO - tudo junto) Livraria: use input() para pedir o
   nome do livro, o preço unitário e a quantidade de exemplares
   comprados. Converta os valores numéricos, calcule o subtotal,
   aplique 15% de desconto, e imprima um resumo completo e
   formatado da compra, usando comentários para documentar cada
   etapa do cálculo.
------------------------------------------------------------
"""


