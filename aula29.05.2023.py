#Faça um jogo de Impar ou Par com o usuário (pergunte qual opção ele deseja, e peça um número de 1 a 5).

import random

num1 = int(input("digite um número de sua escolha:"))
num2 = random.randint(1,5)
soma = num1 + num2

if soma % 2 == 0:
    print("Seu número é par vc ganhou!")
else:
    print("Seu número é ímpar, vc perdeu!")

    #1- Crie um jogo onde o usuário deve adivinhar em 3 tentativas qual número de 1 a 10 foi sorteado. Deve exibir uma mensagem quando ele errar, 
#quantas chances ele já utilizou e quando ele venceu.

print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número de 1 a 10 em até 3 tentativas.")

import random

num = random.randint(1, 10)
tentativa1 = 0

while tentativa1 < 3:
        tentativa1 = int(input("Digite um número: "))
        tentativa1 += 1

        if tentativa1 == num:
            print("Parabéns! Você acertou!")
        else:
         print("Suas tentativas acabaram. O número sorteado era:", num)
