import random

def imprime_mensagem_abertura():
    """
    Imprime a mensagem de abertura
    """
    print("*********************************")
    print("** Bem vindo no jogo de Forca! **")
    print("*********************************")

def escolhe_palavra_secreta():
    """
    Escolhe uma palavra aleatória do arquivo palavras.txt
    """
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    palavra_secreta = palavras[random.randrange(0, len(palavras))].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    return input("Insira uma letra: ").strip().upper()

def marca_chute_correto(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1

def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = escolhe_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(f"Acerte a palavra: {letras_acertadas}")

    enforcou = False
    acertou = False
    erro = 0

    #enquanto não acertou e não enforcou, continua jogando...
    #enquanto  não False  e  não false
    #enquanto     True    e    True
    #enquanto           True
    while(not acertou and not enforcou):
        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            erro += 1
            desenha_forca(erro)

        enforcou = erro == 7 #enforcou toma o valor de erro quando erro for igual a 6, deixando de ser False e se tornando True, quebrando o laço
        acertou = "_" not in letras_acertadas #underline não deveria estar nas letras acertadas
        print(letras_acertadas)

    if(acertou):
        imprime_mensagem_ganhador()
    else:
        imprime_mensagem_perdedor(palavra_secreta)



def imprime_mensagem_ganhador():
    print("Fim de jogo! Você acertou a palavra! Parabéns!! :)")
    print("      ___________      ")
    print("     '._==_==_=_.'     ")
    print("     .-\\:      /-.    ")
    print("    | (|:.     |) |    ")
    print("     '-|:.     |-'     ")
    print("       \\::.    /      ")
    print("        '::. .'        ")
    print("          ) (          ")
    print("        _.' '._        ")
    print("       '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print(f"Fim de jogo! A palavra era {palavra_secreta.lower()}. Você foi enforcado! :(")
    print("      _______________         ")
    print("     /               \       ")
    print("    /                 \      ")
    print("  //                   \/\  ")
    print("  \|   XXXX     XXXX   | /   ")
    print("   |   XXXX     XXXX   |/     ")
    print("   |   XXX       XXX   |      ")
    print("   |                   |      ")
    print("   \__      XXX      __/     ")
    print("     |\     XXX     /|       ")
    print("     | |           | |        ")
    print("     | I I I I I I I |        ")
    print("     |  I I I I I I  |        ")
    print("     \_             _/       ")
    print("       \_         _/         ")
    print("         \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar()