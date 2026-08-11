"""
MODULO 3 - Estruturas de dados, listas e valores booleanos
Lista de exercicios (listas)

Escreva o codigo de cada exercicio logo abaixo do enunciado dele.
"""

# ================================================================
# ESSENCIAIS (fazer em aula)
# ================================================================

# ----------------------------------------------------------------
# EXERCICIO 1
# Crie uma lista com 5 frutas e imprima: a primeira fruta
# (índice 0), a última fruta (índice -1) e uma fatia com as
# frutas do meio (usando [inicio:fim]).
frutas = ['maçã', 'banana', 'laranja', 'uva', 'pera']
print('primeira fruta:', frutas[0])
print('ultima fruta:', frutas[-1])
print('frutas do meio:', frutas[1:4])

# ----------------------------------------------------------------



# ----------------------------------------------------------------
# EXERCICIO 2
# Crie uma lista de compras com 3 itens. Use append() para
# adicionar um item no final e insert() para adicionar outro
# item no início. Em seguida, remova um item pelo valor (usando
# remove()) e outro pela posição (usando pop()). Imprima a lista
# após cada operação.
compras = ['arroz', 'feijao', 'macarrao']
compras.append('leite')
print('lista de compras apos append:', compras)
compras.insert(0, 'pao')
print('lista de compras apos insert:', compras)
compras.remove('feijao')
print('lista de compras apos remove:', compras)
compras.pop(1)
print('lista de compras apos pop:', compras)

 

# ----------------------------------------------------------------



# ----------------------------------------------------------------
# EXERCICIO 3
# Percorra uma lista de números usando for e imprima apenas os
# valores pares (use o operador % dentro de um if).
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    if numero % 2==0:
        print('numero par:', numero)

# ----------------------------------------------------------------



# ----------------------------------------------------------------
# EXERCICIO 4
# Crie um menu com while True para gerenciar uma lista de
# contatos: 1 para Adicionar contato, 2 para Remover contato, 3
# para Listar contatos, 4 para Sair. Use append(), remove() e um
# for para listar.
contatos = []
while True:
    print('1 - adicionar contato')
    print('2 - remover contato')
    print('3 - listar contatos')
    print('4 - sair')
    opcao = input('escolha uma opcao: ')
    if opcao == '1':
        contato = input('digite o nome do contato: ')
        contatos.append(contato)
    elif opcao == '2':
        contato = input('digite o nome do contato a ser removido: ')
        if contato in contatos:
            contatos.remove(contato)
        else:
            print('contato nao encontrado')
    elif opcao == '3':
        for contato in contatos:
            print(contato)
    elif opcao == '4':
        break
    else:
        print('opcao invalida')


# ----------------------------------------------------------------



# ----------------------------------------------------------------
# EXERCICIO 5 (DESAFIO - aplicado)
# Crie um menu com while True para controlar as movimentações de
# uma conta: 1 para Registrar movimentação (peça um valor -
# positivo para entrada, negativo para saída - e guarde numa
# lista), 2 para Ver saldo total (soma dos valores), 3 para Ver
# maior entrada e maior saída (max/min), 4 para Ver histórico
# completo, 5 para Sair.
while True:
    print('1 - registrar movimentacao')
    print('2 - ver saldo total')
    print('3 - ver maior entrada e maior saida')
    print('4 - ver historico completo')
    print('5 - sair')
    opcao = input('escolha uma opcao: ')
    if opcao == '1':
        valor = float(input('digite o valor da movimentacao: '))
        movimentacoes.append(valor) # type: ignore
    elif opcao == '2':
        print('saldo total:', sum(movimentacoes)) # type: ignore
    elif opcao == '3':
        print('maior entrada:', max(movimentacoes)) # type: ignore
        print('maior saida:', min(movimentacoes)) # type: ignore
    elif opcao == '4':
        print('historico completo:', movimentacoes) # type: ignore
    elif opcao == '5':
        break
    else:
        print('opcao invalida')
        

# ================================================================
# BÔNUS (se sobrar tempo / pra casa)
# ================================================================

# ----------------------------------------------------------------
# EXERCICIO 6
# Crie uma lista vazia e uma lista com 3 números dentro. Imprima
# as duas e o tipo de cada uma usando type().

lista_vazia = []
lista_com_3_numeros = [1, 2, 3]

print('lista vazia:', lista_vazia)
print('tipo da lista vazia:', type(lista_vazia))

print('lista com 3 números:', lista_com_3_numeros)
print('tipo da lista com 3 números:', type(lista_com_3_numeros))

# ----------------------------------------------------------------



# ----------------------------------------------------------------
# EXERCICIO 7
# Crie uma lista de números e use len(), sum(), max() e min() para
# mostrar a quantidade de itens, a soma, o maior e o menor valor
# da lista.
lista_numeros = [5, 10, 15, 20, 25]
print('quantidade de itens:', len(lista_numeros))
print('soma dos valores:', sum(lista_numeros))
print('maior valor:', max(lista_numeros))
print('menor valor:', min(lista_numeros))


# ----------------------------------------------------------------



# ----------------------------------------------------------------
# EXERCICIO 8
# Crie uma lista de números fora de ordem. Ordene ela com sort() e,
# em seguida, inverta a ordem com reverse().

numeros = [5, 2, 8, 1, 9]
print('lista original:', numeros)

numeros.sort()
print('lista ordenada:', numeros)

numeros.reverse()
print('lista invertida:', numeros)

# ----------------------------------------------------------------



# ----------------------------------------------------------------
# EXERCICIO 9
# Peça um valor ao usuário via input() e verifique se ele está
# presente numa lista de códigos válidos (usando o operador in),
# imprimindo o resultado.
input_codigo = input('digite um código: ')
codigos_validos = ['ABC123', 'XYZ789', 'DEF456']

if input_codigo in codigos_validos:
    print('código válido!')
else:
    print('código inválido!')


# ----------------------------------------------------------------



# ----------------------------------------------------------------
# EXERCICIO 10
# Crie um menu com while True para gerenciar uma playlist de
# músicas: 1 para Adicionar música, 2 para Remover música, 3 para
# Listar músicas, 4 para Sair. Use append(), remove() e um for
# para listar.
while True:
    print('1 - adicionar musica')
    print('2 - remover musica')
    print('3 - listar musicas')
    print('4 - sair')
    opcao = input('escolha uma opcao: ')

    if opcao == '1':
        musica = input('digite o nome da musica: ')
        playlist.append(musica) # type: ignore
    elif opcao == '2':
        musica = input('digite o nome da musica a ser removida: ')
        if musica in playlist: # type: ignore
            playlist.remove(musica) # type: ignore
        else:
            print('musica nao encontrada!')
    elif opcao == '3':
        print('musicas na playlist:')
        for m in playlist: # type: ignore
            print(f'- {m}')
    elif opcao == '4':
        break
    else:
        print('opcao invalida')

# ----------------------------------------------------------------


