import forca
import advinhacao

def escolhe_jogo():
    print("(1) Forca (2) Advinhação")

    jogo = int(input("Qual jogo?"))

    if(jogo == 1):
    print("jogando forca")
    forca.jogar()
    elif(jogo == 2):
    print("jogando Advinhação")  
    advinhacao.jogar()  

if (__name__ == "__main__"):
    escolhe_jogo()    