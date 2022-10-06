import random

def jogar():
    print("*********************************")
    print("Bem vindo no jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    numero_tentativas = 0
    pontos = 1000

    print("Níveis de dificuldade: (1) Fácil (2) Médio (3) Díficil")

    nivel = int(input("Defina o nível de dificuldade: "))

    if(nivel > 3 or nivel < 1):
        print("Comando inválido.")
    elif(nivel == 1):
        numero_tentativas = 20
    elif(nivel == 2):
        numero_tentativas = 10
    else:
        numero_tentativas = 5

    print(f"Você possui {numero_tentativas} tentativas!")

    for rodada in range(1, numero_tentativas+1):
        print(f"~*~*~*Tentativa {rodada} de {numero_tentativas}!*~*~*~")
        chute = int(input("Digite o seu numero entre 1 e 100: "))
        print("Você digitou", chute)

        if(chute < 1 or chute >100):
            print("Você deve digitar um número entre 0 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print(f"Você acertou e fez {pontos} pontos!")
            break

        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto!")
                pontos_perdidos = abs(numero_secreto - (chute))
                pontos = pontos - pontos_perdidos
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto!")
                pontos_perdidos = abs(numero_secreto - (chute))
                pontos = pontos - pontos_perdidos

    print(f"Fim de jogo! O número secreto é {numero_secreto}")

if(__name__ == "__main__"):
    jogar()