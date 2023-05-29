#EXE.3
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


#Ex 2: Calcular o desconto do salário de um funcionário (11%), exibindo o valor ou o desconto máximo permitido (318,20R$)
sal_duf = float(input("digite valor de salário:"))
desc = sal_duf * 0.11
desc_max = 318.20
if (desc <= desc_max):
    print ("seu desconto foi de: R${}".format(desc))
else:
    print("Seu desconto será de : R${:.2f}".format(desc_max))

#Ex 3: Pedir ao usuário o valor do Euro, Dólar e Real de hoje, pedir um valor ao mesmo e fazer a conversão de todas as opções.

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
