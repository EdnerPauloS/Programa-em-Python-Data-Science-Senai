# -*- coding: utf-8 -*-
import random # Módulo necessário para gerar números aleatórios
import time   # Opcional: para pequenas pausas e dar um 'feeling' melhor

# --- Funções do Jogo ---

def definir_intervalo():
    """Define e retorna o intervalo (mínimo, máximo) para o número secreto."""
    # Você pode facilmente mudar o intervalo aqui se quiser
    minimo = 1
    maximo = 100
    print(f"--- Bem-vindo ao Jogo da Adivinhação! ---")
    print(f"Vou pensar em um número entre {minimo} e {maximo}.")
    return minimo, maximo

def gerar_numero_secreto(min_val, max_val):
    """Gera e retorna um número inteiro aleatório dentro do intervalo."""
    numero = random.randint(min_val, max_val)
    # print(f"(Psst... o número secreto é {numero})") # Linha para teste, remova ou comente depois
    return numero

def obter_palpite_jogador(num_tentativa, min_val, max_val):
    """Solicita um palpite ao jogador, valida e retorna o número inteiro."""
    while True: # Loop infinito até que uma entrada válida seja dada
        try:
            palpite_str = input(f"Tentativa #{num_tentativa}: Qual seu palpite ({min_val}-{max_val})? ")
            palpite_int = int(palpite_str)

            # Verifica se o palpite está dentro do intervalo permitido
            if min_val <= palpite_int <= max_val:
                return palpite_int # Retorna o palpite válido
            else:
                print(f"Opa! Seu palpite deve estar entre {min_val} e {max_val}.")

        except ValueError:
            # Se int() falhar, significa que não foi digitado um número
            print("Entrada inválida. Por favor, digite apenas um número inteiro.")

def verificar_palpite(palpite, numero_secreto):
    """
    Compara o palpite com o número secreto.
    Imprime a dica ("Muito alto", "Muito baixo").
    Retorna True se o jogador acertou, False caso contrário.
    """
    if palpite < numero_secreto:
        print("Muito baixo! Tente um número maior.")
        return False
    elif palpite > numero_secreto:
        print("Muito alto! Tente um número menor.")
        return False
    else:
        print(f"⭐ Parabéns! Você acertou! O número era {numero_secreto}! ⭐")
        return True

def jogar_novamente():
    """Pergunta ao jogador se ele quer jogar outra partida."""
    while True:
        resposta = input("\nDeseja jogar novamente? (s/n): ").lower().strip()
        if resposta == 's' or resposta == 'sim':
            return True
        elif resposta == 'n' or resposta == 'nao' or resposta == 'não':
            return False
        else:
            print("Resposta inválida. Por favor, digite 's' para sim ou 'n' para não.")

# --- Função Principal (Controla o fluxo do jogo) ---

def main():
    """Função principal que executa o jogo de adivinhação."""
    while True: # Loop principal para permitir jogar várias vezes
        minimo, maximo = definir_intervalo()
        numero_a_adivinhar = gerar_numero_secreto(minimo, maximo)
        tentativas = 0
        acertou = False

        # Loop para as tentativas dentro de uma partida
        while not acertou:
            tentativas += 1 # Incrementa o contador de tentativas
            palpite_atual = obter_palpite_jogador(tentativas, minimo, maximo)
            acertou = verificar_palpite(palpite_atual, numero_a_adivinhar)

        # Fim da partida
        print(f"Você precisou de {tentativas} tentativa(s).")

        # Pergunta se quer jogar novamente
        if not jogar_novamente():
            break # Sai do loop principal (while True) se a resposta for não

    # Mensagem de despedida
    print("\nObrigado por jogar! Até a próxima!")
    time.sleep(1) # Pausa por 1 segundo antes de fechar

# --- Ponto de Entrada do Script ---
# Garante que a função main() seja chamada apenas quando o script é executado diretamente
if __name__ == "__main__":
    main()