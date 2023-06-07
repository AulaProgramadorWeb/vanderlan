# vanderlan
#Ex1: Calcular a área de terreno (largura x altura)

largura = float(input("Digite a largura do terreno: "))
altura = float(input("Digite a altura do terreno: "))
area_terreno = largura * altura
print("A área do terreno é:", area_terreno)


#Ex2: perguntar quantos pães franceses e quantos sonhos o cliente deseja comprar. 
# PÃO = 0,50 R$ e SONHO = 2,00 R$. (lembre-se de exibir o valor final.)

pao = 0.50
sonho = 2.00

quantidade_pao = int(input("Quantos pães franceses você deseja comprar? "))
quantidade_sonho = int(input("Quantos sonhos você deseja comprar? "))

total_pao = quantidade_pao * pao
total_sonho = quantidade_sonho * sonho
valor_total = total_pao + total_sonho

print("O valor total é R$ {}".format(valor_total))

#Ex3: Calcular o valor da viagem de um cliente, de acordo com a distância que ele vai andar, 
# o preço da gasolina (o cliente informa o valor) e quanto o carro dele faz por litro
consu_gas = int(input("consumo de gasolina:"))
dist = int(input("Distância: "))
val_gas = int(input("Valor da gasolina: "))
quanti = dist/consu_gas
val_TOTAL = quanti* val_gas
print ("O valor total da viagem é R$ ", val_TOTAL)


#Ex4: Pedir ao usuário sua altura em centimetros e exibir em metros (conversão simples)
alturacm = float (input( "Descreva sua altura em cm?")) 
alturaM = alturacm / 100 
print ("valor da sua altura em metros é:" , alturaM)


#Ex5: Pedir ao usuário o valor de sua compra, e aplicar um desconto de 15%
VAL_COMP = float (input("VALOR DE SUA COMPRA POR FAVOR MEU CONSAGRADO?"))  
VAL_DESC = VAL_COMP * 0.15
VAL_TOTAL = VAL_COMP - VAL_DESC
print ("O VALOR TOTAL DE SUA COMPRA É: R$", VAL_TOTAL)           

#Ex 1: Fazer uma calculadora de divisão com apenas 2 números, e testar se o número é valido (não é zero)
num1 = float(input("digite o numero desejavel:"))
num2 = float(input("digite o numero desejavel:"))
result = num1 / num2
if (result > 0 ):
    print ("seu resultado é {} ".format(result))

else :
    print ("esse número é inválido!!!")


#Ex 2: Calcular o desconto do salário de um funcionário (11%), 
# exibindo o valor ou o desconto máximo permitido (318,20R$)

sal_duf = float(input("digite valor de salário:"))
desc = sal_duf * 0.11
desc_max = 318.20
if (desc <= desc_max):
    print ("seu desconto foi de: R${}".format(desc))
else:
    print("Seu desconto será de : R${:.2f}".format(desc_max))

#Ex 3: Pedir ao usuário o valor do Euro, Dólar e Real de hoje, 
# pedir um valor ao mesmo e fazer a conversão de todas as opções.

# Pedindo os valores das moedas ao usuário
valor_dolar=float(input("digite o valor dolar:"))
valor_euro=float(input("digite o valor euro:"))
valor_real=float(input("digite o valor real:"))

# converter
valor = float(input("Digite o valor a ser convertido: "))

# Realizando as conversões
valor_euro = valor * valor_euro
valor_dolar = valor * valor_dolar
valor_doll_euro = valor_dolar / valor_euro
valor_euro_doll = valor_dolar * valor_euro
valor_euro_real = valor_euro * valor_real
valor_doll_real = valor_dolar * valor_real



# Exibindo resultado
print("valor do real em Euro:{}".format (valor_euro))
print("valor do real em Dólar:{}" .format (valor_dolar))
print("valor do dolar em euro:{}". format (valor_euro_doll))
print("valor do euro em dólar:{}". format (valor_doll_euro))
print("valor do euro em real:{}". format (valor_euro_real))
print("valor do dolár em real:{}". format (valor_doll_real))

#Ex 4: Pedir a idade ao usuário, e testar se ele pode participar da competição, e qual categoria ele seria.  
# de 5 a 7 infantil A, 8 a 10 infantil B, 
# 11 a 13 Juvenil A, 14 pra cima Sênior.

#variavel
idade = int(input("Qual é a sua idade? "))

#Categorias
if (idade >= 5 and idade <= 7):
    categoria = "Infantil A"
    print("Categoria: {} sua idade {}".format(categoria,idade))
elif (idade >= 8 and idade <= 10):
    categoria = "Infantil B"
    print("Categoria: {}".format(categoria))
elif (idade >= 11 and idade <= 13):
    categoria = "Juvenil A"
    print("Categoria: {}".format(categoria))
else:
    print("Categoria: {}".format("Sênior"))

    #Exercício Extra

    #Faça um jogo de Impar ou Par com o usuário 
    # (pergunte qual opção ele deseja, e peça um número de 1 a 5).

import random

num1 = int(input("digite um número de sua escolha:"))
num2 = random.randint(1,5)
soma = num1 + num2

if soma % 2 == 0:
    print("Seu número é par vc ganhou!")
else:
    print("Seu número é ímpar, vc perdeu!")

    #Lista de exercícios 3

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

#2- Criar um loop onde exibe os números de 1 a 30, mas pula os números 4, 19 e 23.
print ("INICIO DE CONTAGEM")
num = 0

while num <= 30:
    if num == 4 or num == 19 or num == 23:
        num += 1
        continue

    
    print(num)
    num += 1

    if num > 31:
        break

else:
    print("FIM DE CONTAGEM")