# -*- coding: utf-8 -*-
# 1. Importando o módulo 'statistics'
# Este módulo fornece funções para calcular estatísticas matemáticas de dados numéricos.
# Precisamos dele para calcular a média, mediana e moda de forma fácil.
import statistics

# 2. Definindo as listas de dados (frequências)
# Estas são as listas que você forneceu, armazenadas em variáveis para fácil acesso.
dados1 = [1, 2, 3, 6, 4]
dados2 = [1.5, 6.8, 9.7, 10.6]
dados3 = [200, 300, 500, 700, 900, 400, 600]

# 3. Criando uma função para calcular e exibir as estatísticas
# Definir uma função torna o código reutilizável e organizado.
# Esta função recebe uma lista de números (lista_dados) e um nome descritivo (nome_lista)
# e imprime a média, mediana e moda para essa lista.
def calcular_e_exibir_estatisticas(lista_dados, nome_lista):
    """
    Calcula e exibe a média, mediana e moda para uma dada lista de números.

    Args:
        lista_dados (list): A lista de números para análise.
        nome_lista (str): Um nome para identificar a lista na saída.
    """
    print(f"\n--- Análise da {nome_lista} ---")
    print(f"Dados Originais: {lista_dados}")

    # Verifica se a lista não está vazia antes de calcular
    if not lista_dados:
        print("A lista está vazia, não é possível calcular estatísticas.")
        return # Sai da função se a lista for vazia

    # --- Cálculo da Média ---
    # A média é a soma de todos os valores dividida pelo número de valores.
    # A função statistics.mean() faz isso diretamente.
    media = statistics.mean(lista_dados)
    # Usamos f-string formatada (: .2f) para exibir a média com 2 casas decimais.
    print(f"Média: {media:.2f}")

    # --- Cálculo da Mediana ---
    # A mediana é o valor central de um conjunto de dados ordenado.
    # Se o número de dados for ímpar, é o valor do meio.
    # Se for par, é a média dos dois valores centrais.
    # A função statistics.median() ordena os dados e encontra a mediana.
    # Vamos ordenar a lista também para visualização (embora median() faça isso internamente)
    dados_ordenados = sorted(lista_dados)
    print(f"Dados Ordenados: {dados_ordenados}")
    mediana = statistics.median(lista_dados)
    print(f"Mediana: {mediana}")

    # --- Cálculo da Moda ---
    # A moda é o valor que aparece com maior frequência na lista.
    # Pode haver uma moda (unimodal), mais de uma (multimodal) ou nenhuma (amodal).
    # A função statistics.mode() retorna a moda *única*.
    # Se não houver uma moda única (todos os valores aparecem 1 vez, ou há empate),
    # ela gera um erro do tipo StatisticsError.
    # Por isso, usamos um bloco 'try...except' para tratar esse caso.
    try:
        moda = statistics.mode(lista_dados)
        print(f"Moda: {moda}")
    except statistics.StatisticsError:
        # Esta mensagem é exibida se statistics.mode() falhar.
        print("Moda: Não há uma moda única (amodal ou multimodal com mesma frequência máxima).")

    print("-" * 30) # Linha separadora para clareza

# 4. Chamando a função para cada lista de dados
# Agora, executamos a função que criamos para cada uma das nossas listas.
calcular_e_exibir_estatisticas(dados1, "Lista 1")
calcular_e_exibir_estatisticas(dados2, "Lista 2")
calcular_e_exibir_estatisticas(dados3, "Lista 3")
