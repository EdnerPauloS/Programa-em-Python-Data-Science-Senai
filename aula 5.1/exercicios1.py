# -*- coding: utf-8 -*-

def solicitar_notas():
    """
    Solicita ao usuário a quantidade de notas e cada nota individualmente.
    Retorna uma lista contendo as notas inseridas.
    """
    notas = []
    while True:
        try:
            # Pergunta quantas notas serão inseridas
            num_notas = int(input("Quantas notas você deseja inserir? "))
            if num_notas > 0:
                break
            else:
                print("Por favor, insira um número positivo de notas.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    print("-" * 30) # Linha separadora para clareza

    # Loop para pedir cada nota
    for i in range(num_notas):
        while True:
            try:
                # Solicita a nota, permitindo vírgula como separador decimal
                nota_str = input(f"Digite a nota {i + 1}: ").replace(',', '.')
                nota = float(nota_str)
                # Opcional: Validar se a nota está em um intervalo (ex: 0 a 10)
                # if 0 <= nota <= 10:
                #     notas.append(nota)
                #     break
                # else:
                #     print("Nota inválida. Insira um valor entre 0 e 10.")
                notas.append(nota) # Adiciona a nota válida à lista
                break # Sai do loop interno (while True) após receber uma nota válida
            except ValueError:
                print("Entrada inválida. Por favor, digite um número (ex: 7.5 ou 8).")
    return notas

def calcular_media(lista_de_notas):
    """
    Calcula a média de uma lista de números (notas).
    Retorna o valor da média ou 0 se a lista estiver vazia.
    """
    if not lista_de_notas:  # Verifica se a lista não está vazia
        print("A lista de notas está vazia. Não é possível calcular a média.")
        return 0.0

    soma_das_notas = sum(lista_de_notas)
    quantidade_de_notas = len(lista_de_notas)
    media = soma_das_notas / quantidade_de_notas
    return media

def exibir_resultado(lista_de_notas, media_calculada):
    """
    Exibe as notas que foram inseridas e a média final calculada.
    """
    print("\n--- Resultado ---")
    print("Notas inseridas:", end=" ")
    # Imprime as notas formatadas
    print(*[f"{nota:.2f}" for nota in lista_de_notas], sep='; ')

    print(f"A média das notas é: {media_calculada:.2f}") # Formata a média com 2 casas decimais

# --- Função Principal (organiza a execução) ---
def main():
    """
    Função principal que coordena a execução do sistema de médias.
    """
    print("--- Sistema de Cálculo de Médias ---")

    # 1. Obter as notas do usuário
    minhas_notas = solicitar_notas()

    # 2. Calcular a média (apenas se houver notas)
    if minhas_notas:
        media_final = calcular_media(minhas_notas)

        # 3. Exibir o resultado
        exibir_resultado(minhas_notas, media_final)
    else:
        # Caso a função solicitar_notas retorne uma lista vazia (embora
        # a lógica atual peça o número de notas > 0, é uma boa prática verificar)
        print("\nNenhuma nota foi inserida para calcular a média.")

# --- Ponto de Entrada do Script ---
# Garante que a função main() seja chamada apenas quando o script é executado diretamente
if __name__ == "__main__":
    main()