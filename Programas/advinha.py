import random

def Advinha():
    print("Bem Vindo ao nosso jogo Luiza")
    num = str(input("Qual é o nome do pato da disney?"))
    if num == "Pato Donald":
        print ("Parabens você acertou!")
    else:
        print ("Que pena, você errou.")

if(__name__ == "__main__"):
    Advinha()