# -*- coding: utf-8 -*-

# 1. Importando o módulo 'time'
# Este módulo fornece funções relacionadas ao tempo, incluindo a pausa na execução.
import time

# --------------------------------------------------------------------------
# Definição das Funções de Cálculo Estatístico (Python Puro)
# (Estas funções são as mesmas da versão anterior)
# --------------------------------------------------------------------------

def calcular_media(dados):
    """Calcula a média aritmética de uma lista de números sem usar módulos externos."""
    n = len(dados)
    if n == 0:
        # Não adicionamos sleep aqui, pois é um aviso interno da função
        # print("Aviso: Lista vazia para cálculo da média.")
        return None
    soma_total = sum(dados)
    media = soma_total / n
    return media

def calcular_mediana(dados):
    """Calcula a mediana de uma lista de números sem usar módulos externos."""
    n = len(dados)
    if n == 0:
        # print("Aviso: Lista vazia para cálculo da mediana.")
        return None
    dados_ordenados = sorted(dados)
    if n % 2 == 1:
        indice_meio = n // 2
        mediana = dados_ordenados[indice_meio]
    else:
        indice_meio_dir = n // 2
        indice_meio_esq = indice_meio_dir - 1
        valor1 = dados_ordenados[indice_meio_esq]
        valor2 = dados_ordenados[indice_meio_dir]
        mediana = (valor1 + valor2) / 2
    return mediana, dados_ordenados # Retorna também os dados ordenados para exibição

def calcular_moda(dados):
    """Calcula a(s) moda(s) de uma lista de números sem usar módulos externos."""
    n = len(dados)
    if n == 0:
        # print("Aviso: Lista vazia para cálculo da moda.")
        return None
    contagens = {}
    for item in dados:
        contagens[item] = contagens.get(item, 0) + 1
    max_frequencia = 0
    if contagens:
         # Usar um loop para evitar max() em dicionário vazio se contagens falhar por algum motivo
         for item in contagens:
             if contagens[item] > max_frequencia:
                 max_frequencia = contagens[item]
    else: # Se contagens ficou vazio (dados originais só tinham itens não-hashable?)
        return None

    if max_frequencia <= 1 and len(contagens) != 1: # Se a frequência máxima é 1 E não é uma lista de um único elemento repetido
         return None # Amodal

    modas = []
    for item, frequencia in contagens.items():
        if frequencia == max_frequencia:
            modas.append(item)
    if not modas:
       return None
    modas.sort()
    return modas

# --------------------------------------------------------------------------
# Dados de Entrada (Mesmos dados)
# --------------------------------------------------------------------------
frequencia1 = [1, 2, 3, 6, 4]
frequencia2 = [1.5, 6.8, 9.7, 10.6]
frequencia3 = [200, 300, 500, 700, 900, 400, 600]
frequencia4 = [5, 5, 6, 7, 7, 7, 8] # Exemplo com moda clara
frequencia5 = [10, 20, 10, 20, 30] # Exemplo multimodal

listas_de_dados = {
    "Frequência 1": frequencia1,
    "Frequência 2": frequencia2,
    "Frequência 3": frequencia3,
    "Frequência 4 (com moda)": frequencia4,
    "Frequência 5 (multimodal)": frequencia5
}

# --------------------------------------------------------------------------
# Execução e Exibição dos Resultados com Pausas
# --------------------------------------------------------------------------
print("Calculando Estatísticas com Funções de Python Puro (com pausas):\n")

# 2. Definindo o tempo de pausa em segundos
tempo_pausa = 0.8 # Você pode ajustar este valor (ex: 0.5, 1.0, 1.5)

time.sleep(tempo_pausa * 2) # Pausa inicial um pouco maior

for nome, dados_atuais in listas_de_dados.items():
    # Pausa antes de exibir o nome da lista
    time.sleep(tempo_pausa)
    print(f"--- Análise da {nome} ---")

    # Pausa antes de exibir os dados
    time.sleep(tempo_pausa)
    print(f"Dados: {dados_atuais}")

    # Calcular (os cálculos são rápidos, não precisam de pausa interna)
    media = calcular_media(dados_atuais)
    # Mediana agora retorna valor e lista ordenada
    mediana, dados_ordenados_para_exibir = calcular_mediana(dados_atuais) if dados_atuais else (None, [])
    moda = calcular_moda(dados_atuais)

    # Exibir os resultados formatados com pausas entre eles

    if media is not None:
        time.sleep(tempo_pausa) # Pausa ANTES de imprimir a média
        print(f"Média Calculada: {media:.2f}")
    else:
        time.sleep(tempo_pausa)
        print("Média Calculada: Não aplicável (lista vazia)")

    if mediana is not None:
        time.sleep(tempo_pausa) # Pausa ANTES de imprimir os dados ordenados
        print(f"Dados Ordenados: {dados_ordenados_para_exibir}")
        time.sleep(tempo_pausa) # Pausa ANTES de imprimir a mediana
        print(f"Mediana Calculada: {mediana}")
    else:
        time.sleep(tempo_pausa)
        print("Mediana Calculada: Não aplicável (lista vazia)")

    if moda is not None:
        time.sleep(tempo_pausa) # Pausa ANTES de imprimir a moda
        print(f"Moda(s) Calculada(s): {moda}")
    else:
        time.sleep(tempo_pausa) # Pausa ANTES de imprimir 'amodal'
        print("Moda Calculada: Nenhuma (Amodal)")

    time.sleep(tempo_pausa) # Pausa ANTES de imprimir o separador
    print("-" * 35)
    time.sleep(tempo_pausa / 2) # Uma pausa menor antes do próximo bloco

print("\nCálculos concluídos.")