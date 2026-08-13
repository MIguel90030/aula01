"""
MODULO 4 - Funcoes, tuplas, dicionarios e tratamento de excecoes
Lista de exercicios (funcoes)

Escreva o codigo de cada exercicio logo abaixo do enunciado dele.
"""

# ================================================================
# ESSENCIAIS (fazer em aula)
# ================================================================

# ----------------------------------------------------------------
# EXERCICIO 1
# Crie uma função "eh_par(numero)" que retorne True se o número
# for par e False caso contrário (use o operador % - resto da divisão).

def eh_par(numero):
    return numero % 2 == 0

# ----------------------------------------------------------------



# ----------------------------------------------------------------
# EXERCICIO 2
# Crie uma função "maior_de_tres(a, b, c)" que retorne o maior
# valor entre os três parâmetros (pode usar max()).

def maior_de_tres(a, b, c):
    return max(a, b, c)

# ----------------------------------------------------------------



# ----------------------------------------------------------------
# EXERCICIO 3 (APLICADO - exemplo prático)
# Abaixo está o exemplo prático de menu de movimentações visto em
# aula. Copie/rode o código como está e depois ADICIONE pelo menos
# DUAS novas opções ao menu, usando operações de lista vistas no
# módulo de listas (append, remove, pop, sort, reverse, len, sum,
# max, min, in, slicing...). Sugestões:
#   - "Remover a última movimentação" (usando historico.pop())
#   - "Ver histórico ordenado" (usando sorted(historico), sem
#     alterar a lista original)
#   - "Contar quantas movimentações foram entrada e quantas
#     foram saída" (percorrendo a lista com for e um if)
# Lembre-se: cada nova opção deve virar uma FUNÇÃO nova, chamada
# a partir de "main()", igual às funções já existentes.

# ----------------------------------------------------------------

def exibir_menu():
    print("\n--- Menu de Movimentações ---")
    print("1 - Registrar movimentação")
    print("2 - Ver saldo total")
    print("3 - Ver maior entrada e maior saída")
    print("4 - Ver histórico completo")
    print("5 - Sair")
    opcao = input("Escolha uma opção: ")
    return opcao

def registrar_movimentacao(historico):
    valor = float(input("Valor da movimentação (positivo=entrada, negativo=saída): "))
    historico.append(valor)
    print("Movimentação registrada!")

def ver_saldo_total(historico):
    if historico:
        print(f"Saldo total: {sum(historico):.2f}")
    else:
        print("Nenhuma movimentação registrada.")

def ver_maior_entrada_saida(historico):
    if historico:
        print(f"Maior entrada: {max(historico):.2f}")
        print(f"Maior saída: {min(historico):.2f}")
    else:
        print("Nenhuma movimentação registrada.")

def ver_historico(historico):
    print("Histórico completo:", historico)

def main():
    historico = []
    while True:
        opcao = exibir_menu()

        if opcao == "1":
            registrar_movimentacao(historico)
        elif opcao == "2":
            ver_saldo_total(historico)
        elif opcao == "3":
            ver_maior_entrada_saida(historico)
        elif opcao == "4":
            ver_historico(historico)
        elif opcao == "5":
            print("Encerrando...")
            break
        else:
            print("Opção inválida, tente novamente")

# Descomente a linha abaixo para rodar o menu:
main()
def exibir_menu():
    print('\n--- Menu de Movimentacoes ---')
    print('1 - Registrar movimentacao')
    print('2 - Ver saldo total')
    print('3 - Ver maior entrada e maior saída')
    print('4 - Ver histórico completo')
    print('5 - Sair')
    opcao = input('Escolha uma opção: ')
    return opcao


# ----------------------------------------------------------------
# EXERCICIO 4
# Crie uma função "calcular_desconto(preco, desconto=10)" que
# retorne o preço já com o desconto aplicado (em porcentagem).
# Chame ela uma vez sem informar o desconto (usa o padrão) e uma
# vez informando um desconto diferente.
def calcular_desconto(preco, desconto=10):
    return preco * (1 - desconto / 100)

# Teste a função
print(calcular_desconto(100))  # Usa o desconto padrão (10%)
print(calcular_desconto(100, 20))  # Usa o desconto informado (20%)

# ----------------------------------------------------------------



# ----------------------------------------------------------------
# EXERCICIO 5
# Crie uma função "media_da_lista(numeros)" que receba uma LISTA
# de números e retorne a média deles (some com sum() e divida
# pelo tamanho com len()). Teste com uma lista de notas.
def media_da_lista(numeros):
    if numeros:
        return sum(numeros) / len(numeros)
    else:
        return 0 
    
# ----------------------------------------------------------------



# ================================================================
# BÔNUS (se sobrar tempo / pra casa)
# ================================================================

# ----------------------------------------------------------------
# EXERCICIO 6
# Crie uma função "somente_pares(numeros)" que receba uma lista
# de números e retorne uma NOVA lista contendo apenas os valores
# pares (percorra com for e use append() numa lista nova).
def somente_pares(numeros):
    pares = []
    for n in numeros:
        if eh_par(n):
            pares.append(n)
    return pares

# ----------------------------------------------------------------



# ----------------------------------------------------------------
# EXERCICIO 7
# Crie uma função "maior_e_menor(numeros)" que receba uma lista
# e retorne o maior e o menor valor dela (usando max() e min()).
def maior_e_menor(numeros):
    if numeros:
        return max(numeros), min(numeros)
    else:
        return None, None
    
# ----------------------------------------------------------------



# ----------------------------------------------------------------
# EXERCICIO 8
# Crie uma função "existe_na_lista(lista, valor)" que retorne
# True se "valor" estiver dentro de "lista" e False caso
# contrário (use o operador in).
def existe_na_lista(lista, valor):
    return valor in lista

# ----------------------------------------------------------------



# ----------------------------------------------------------------
# EXERCICIO 9
# Crie uma função "ordenar_sem_alterar(lista)" que retorne uma
# CÓPIA ordenada da lista recebida, sem alterar a lista original
# (dica: use sorted(lista) em vez de lista.sort()).
def ordenar_sem_alterar(lista):
    return sorted(lista)


# ----------------------------------------------------------------



# ----------------------------------------------------------------
# EXERCICIO 10
# Crie uma função "cadastrar_nomes(*nomes)" que receba uma
# quantidade qualquer de nomes (usando *args) e retorne todos
# como uma lista. Chame ela passando 3 nomes e depois 5 nomes.
def cadastrar_nomes(*nomes):
    return list(nomes)

# ----------------------------------------------------------------


