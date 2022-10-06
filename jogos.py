import forca
import adivinhacao

def escolher_jogo():
    print("*********************************")
    print("*******      Jogos!!      *******")
    print("*********************************")

    print(f"(1) Forca (2) Adivinhação")
    jogo = int(input("Escolha um jogo: "))

    if(jogo == 1):
        print("Jogando forca...")
        forca.jogar()
    elif(jogo ==2):
        print("Jogando adivinhação...")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolher_jogo()