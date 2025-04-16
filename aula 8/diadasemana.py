def main():
    # Dicionário para contar as preferências
    preferencias = {
        'segunda': 0,
        'terca': 0,
        'quarta': 0,
        'quinta': 0,
        'sexta': 0
    }

    # Número de colaboradores
    num_colaboradores = 7

    # Coleta as preferências dos colaboradores
    for i in range(num_colaboradores):
        while True:
            dia = input(f"Colaborador {i + 1}, escolha um dia da semana (segunda, terca, quarta, quinta, sexta): ").strip().lower()
            if dia in preferencias:
                preferencias[dia] += 1
                break
            else:
                print("Dia inválido. Por favor, escolha um dia válido.")

    # Exibe o resultado das preferências
    print("\nResultados da votação:")
    for dia, contagem in preferencias.items():
        print(f"{dia.capitalize()}: {contagem} voto(s)")

    # Verifica o dia com mais votos
    max_votos = max(preferencias.values())
    dias_vencedores = [dia for dia, contagem in preferencias.items() if contagem == max_votos]

    # Exibe o resultado final
    if len(dias_vencedores) == 1:
        print(f"\nO dia escolhido para a live é: {dias_vencedores[0].capitalize()}")
    else:
        print(f"\nHouve um empate entre os dias: {', '.join(dias_vencedores).capitalize()}")

if __name__ == "__main__":
    main()