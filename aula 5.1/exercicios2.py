# -*- coding: utf-8 -*-

def solicitar_peso():
    """
    Solicita e valida o peso do usuário em quilogramas (kg).
    Retorna o peso como um número float.
    """
    while True:
        try:
            # Solicita o peso, permitindo vírgula ou ponto como separador decimal
            peso_str = input("Digite seu peso em kg (ex: 75,5): ").replace(',', '.')
            peso = float(peso_str)
            if peso > 0: # Valida se o peso é positivo
                return peso
            else:
                print("Peso inválido. Por favor, insira um valor positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para o peso.")

def solicitar_altura():
    """
    Solicita e valida a altura do usuário em metros (m).
    Retorna a altura como um número float.
    """
    while True:
        try:
            # Solicita a altura, permitindo vírgula ou ponto como separador decimal
            altura_str = input("Digite sua altura em metros (ex: 1,70): ").replace(',', '.')
            altura = float(altura_str)
            if altura > 0: # Valida se a altura é positiva
                return altura
            else:
                print("Altura inválida. Por favor, insira um valor positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número para a altura.")

def calcular_imc(peso_kg, altura_m):
    """
    Calcula o Índice de Massa Corporal (IMC).
    Recebe o peso em kg e a altura em metros.
    Retorna o valor do IMC calculado ou None se a altura for inválida.
    """
    if altura_m <= 0:
        print("Erro: Altura inválida (não pode ser zero ou negativa) para calcular o IMC.")
        return None # Retorna None para indicar que o cálculo não pôde ser feito

    # Fórmula do IMC: peso / (altura ao quadrado)
    imc = peso_kg / (altura_m ** 2) # Ou: peso_kg / (altura_m * altura_m)
    return imc

def classificar_imc(valor_imc):
    """
    Classifica o valor do IMC de acordo com as faixas padrão da OMS.
    Recebe o valor do IMC.
    Retorna uma string com a classificação.
    """
    if valor_imc is None: # Verifica se o IMC foi calculado corretamente
        return "Não foi possível classificar (erro no cálculo do IMC)."
    elif valor_imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= valor_imc < 25: # 18.5 até 24.9
        return "Peso normal"
    elif 25 <= valor_imc < 30: # 25 até 29.9
        return "Sobrepeso"
    elif 30 <= valor_imc < 35: # 30 até 34.9
        return "Obesidade Grau I"
    elif 35 <= valor_imc < 40: # 35 até 39.9
        return "Obesidade Grau II (severa)"
    else: # valor_imc >= 40
        return "Obesidade Grau III (mórbida)"

def exibir_resultado(peso, altura, imc_calculado, classificacao):
    """
    Exibe os dados informados, o IMC calculado e sua classificação.
    """
    print("\n--- Resultado do Cálculo de IMC ---")
    print(f"Peso informado: {peso:.1f} kg")       # Formata com 1 casa decimal
    print(f"Altura informada: {altura:.2f} m")    # Formata com 2 casas decimais
    if imc_calculado is not None:
        print(f"Seu IMC é: {imc_calculado:.1f}")  # Formata com 1 casa decimal
    print(f"Classificação: {classificacao}")
    print("-----------------------------------")
    print("Lembre-se: O IMC é apenas um indicador. Consulte um profissional de saúde.")

# --- Função Principal (organiza a execução) ---
def main():
    """
    Função principal que coordena a execução do sistema de cálculo de IMC.
    """
    print("--- Calculadora de IMC (Índice de Massa Corporal) ---")
    print("Vamos calcular seu IMC.")

    # 1. Obter peso e altura do usuário
    peso_usuario = solicitar_peso()
    altura_usuario = solicitar_altura()

    # 2. Calcular o IMC
    imc_resultado = calcular_imc(peso_usuario, altura_usuario)

    # 3. Classificar o IMC
    classificacao_resultado = classificar_imc(imc_resultado)

    # 4. Exibir os resultados
    exibir_resultado(peso_usuario, altura_usuario, imc_resultado, classificacao_resultado)

# --- Ponto de Entrada do Script ---
# Garante que a função main() seja chamada apenas quando o script é executado diretamente
if __name__ == "__main__":
    main()