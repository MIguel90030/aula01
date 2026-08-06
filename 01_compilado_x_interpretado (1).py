"""
MODULO 1 - Introducao a programacao e ao Python
Topico: Linguagens compiladas x interpretadas

------------------------------------------------------------
TEORIA
------------------------------------------------------------
Todo computador so entende instrucoes em binario (0s e 1s).
Como programamos em uma linguagem legivel para humanos (Python,
C, Java...), é preciso TRADUZIR o codigo escrito para algo que
o processador entenda. Existem duas estrategias principais:

1) LINGUAGEM COMPILADA
   - O codigo inteiro é traduzido de uma vez, ANTES de rodar,
     por um programa chamado COMPILADOR.
   - O resultado é um arquivo executavel (.exe, binario).
   - Exemplos: C, C++, Rust, Go.
   - Vantagem: roda muito rapido, pois ja esta em binario.
   - Desvantagem: precisa recompilar a cada mudanca no codigo;
     o executavel gerado costuma ser especifico para cada
     sistema operacional.

2) LINGUAGEM INTERPRETADA
   - O codigo é lido e executado LINHA A LINHA, em tempo real,
     por um programa chamado INTERPRETADOR.
   - Nao existe uma etapa separada de "compilar" antes de rodar.
   - Exemplos: Python, JavaScript, Ruby.
   - Vantagem: mais rapido para testar e depurar (roda na hora),
     o mesmo codigo roda em qualquer sistema que tenha o
     interpretador instalado.
   - Desvantagem: tende a ser mais lento que codigo compilado,
     pois a traducao acontece durante a execucao.

ONDE O PYTHON SE ENCAIXA?
   Python é uma linguagem INTERPRETADA (na pratica, um pouco
   hibrida: o codigo é primeiro convertido para um "bytecode"
   intermediario e depois interpretado pela Python Virtual
   Machine - mas para fins do curso, tratamos Python como
   interpretada). Isso explica por que voce consegue rodar um
   arquivo .py diretamente, sem precisar gerar um .exe antes.

------------------------------------------------------------
NA PRATICA
------------------------------------------------------------
Quando voce roda:

    python3 nome_do_arquivo.py

o interpretador Python le o arquivo de cima para baixo e vai
executando cada instrucao. Vamos comprovar isso abaixo.
"""

import sys

print("Este script esta rodando em Python", sys.version.split()[0])
print("Nao existe nenhum arquivo .exe sendo gerado - o Python")
print("leu este arquivo texto e executou linha por linha.")

# Prova simples de execucao sequencial: cada print roda no
# momento em que o interpretador chega naquela linha.
print("\n--- Executando em sequencia ---")
print("1. Esta linha roda primeiro")
print("2. Esta linha roda em seguida")
print("3. Esta linha roda por ultimo")


print('git')


