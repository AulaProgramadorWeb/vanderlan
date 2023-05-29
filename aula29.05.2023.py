#Faça um jogo de Impar ou Par com o usuário (pergunte qual opção ele deseja, e peça um número de 1 a 5).

import random

num1 = int(input("digite um num de 1 a 5:"))
num2 = random.randint(1,5)
soma = num1 + num2

if soma % 2 == 0:
    print("Seu número é par vc ganhou!")
else:
    print("Seu número é ímpar, vc perdeu!")