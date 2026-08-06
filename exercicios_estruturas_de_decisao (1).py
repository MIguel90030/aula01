"""
MODULO 3 - Estruturas de dados, listas e valores booleanos
Lista de exercicios (estruturas de decisao - if, elif, else)

Escreva o codigo de cada exercicio num script separado. Use
input() para receber os dados, convertendo os tipos quando
necessário. As respostas ficam em
exercicios_estruturas_de_decisao_respostas.py.

------------------------------------------------------------
1. Peça a idade do usuário via input(), converta para int, e diga
   se ela é "Maior de idade" (>= 18) ou "Menor de idade", usando
   if/else.
   """
# idade_texto = input("Qual é a sua idade? ")
# idade = int(idade_texto)
# if idade >= 18: 
#     print("Maior de idade")
# else: 
#     print("Menor de idade")


"""""
2. Peça duas notas de um aluno via input(), converta para float,
   calcule a média entre elas e diga se o aluno está "Aprovado"
   (média >= 6) ou "Reprovado", usando if/else.
   """
Nota_P1 = input('Qual foi a nota da sua P1?')
Nota_P2 = input('Qual foi a nota da sua P2?')
Nota1 = float(Nota_P1) 
print(Nota1)
Nota2 = float(Nota_P2)
print(Nota2)
media = Nota1 + Nota2 /2
if media >=6:
    print('Acima da média')
else:
    print('reprovado')

    


"""
3. Peça a idade do usuário e se ele possui carteira de motorista
   (respondendo "sim" ou "nao") via input(). Diga se a pessoa
   "Pode dirigir" (idade >= 18 and carteira == "sim") ou "Não pode
   dirigir", usando if/else.

4. Peça a quantidade de um produto em estoque via input(),
   converta para int, e classifique usando if/elif/else em:
   "Estoque negativo" (quantidade < 0), "Estoque zerado"
   (quantidade == 0), "Estoque baixo" (0 < quantidade < 20) ou
   "Estoque normal" (quantidade >= 20).

5. Peça a quantidade atual em estoque de um produto e o valor de
   uma movimentação via input() (positivo para entrada/reposição,
   negativo para saída/venda). Converta para int, calcule o novo
   estoque (estoque + movimentação) e use if/else para avisar
   "Estoque insuficiente" caso o resultado fique negativo, ou
   mostrar o novo estoque caso contrário.

6. Peça a quantidade disponível em estoque e a quantidade que um
   cliente quer comprar via input(). Converta para int e use
   if/else para verificar se a venda é possível (quantidade
   pedida <= estoque disponível): se for, calcule e mostre o
   estoque restante; senão, mostre uma mensagem de estoque
   insuficiente.

7. Crie um menu simples para uma lanchonete. Peça ao usuário para
   digitar um número (1 para Fazer pedido, 2 para Ver cardápio, 3
   para Cancelar pedido) via input(), converta para int, e use
   if/elif/else para mostrar uma mensagem diferente de acordo com
   a opção escolhida (pode ser só uma mensagem simulando a ação,
   sem precisar de laço de repetição ainda).

8. Sistema de controle de estoque de uma loja: peça o nome do
   produto, a quantidade atual em estoque e, através de um menu
   (1 para Entrada de produtos, 2 para Venda de produtos), a
   operação desejada e a quantidade dela. Valide se a operação é
   possível (uma venda não pode deixar o estoque negativo),
   calcule o novo estoque, e imprima um resumo completo e
   formatado da operação, usando comentários para documentar cada
   etapa.
------------------------------------------------------------
"""
nome_produto = input('\nInforme o nome do produto: ')
estoque_atual = int(input('Informe a quantidade atual do estoque: '))

print('\n--MENU--')
print('1 - Entrada de produtos')
print('2 - Venda de produtos')

operacao = input('Informe a operação: ')
quantidade_operacao = int(input('Informe a quantidade: '))

if operacao == '1':
    novo_estoque = estoque_atual + quantidade_operacao
    print(f'\nProduto: {nome_produto}')
    print(f'Estoque anterior: {estoque_atual}')
    print(f'Entrada: {quantidade_operacao}')
    print(f'Novo estoque: {novo_estoque}')
elif operacao == '2':
    if estoque_atual >= quantidade_operacao:
        novo_estoque = estoque_atual - quantidade_operacao
        print(f'\nProduto: {nome_produto}')
        print(f'Estoque anterior: {estoque_atual}')
        print(f'Saída: {quantidade_operacao}')
        print(f'Novo estoque: {novo_estoque}')
    else:
        print('\nEstoque é insuficiente!')
else:
    print('\nVocê digitou uma operação inválida')     


