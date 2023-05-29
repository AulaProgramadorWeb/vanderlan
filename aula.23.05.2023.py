#Ex 3: Pedir ao usuário o valor do Euro, Dólar e Real de hoje, pedir um valor ao mesmo e fazer a conversão de todas as opções.

valor_de_conversao_reais = float(input("digite valor a ser convertido:"))
valor_de_conversao_dolar = float(input("digite valor a ser convertido:"))
valor_de_conversao_euro = float(input("digite valor a ser convertido:"))

# Taxas de câmbio
taxa_dolar = float(input("digite valor da taxa do euro:" ))
taxa_euro = float(input("digite valor da taxa  do dólar:" ))
taxa_real = float(input("digite valor da taxa  do real:" ))

# Conversão de dólar para euro
dolar = valor_de_conversao_dolar * taxa_euro
print("o valor de {} dólares em euros equivale a {} euros.".format(valor_de_conversao_dolar, dolar))

# Conversão de euro para dólar
euro = valor_de_conversao_euro * taxa_dolar
print("O valor de {} euros equivalem a {} dólares.".format( valor_de_conversao_euro, euro))

# Conversão de real para euro
real = valor_de_conversao_reais * taxa_euro
print("O valor de {} reais equivalem a {} euros.".format(valor_de_conversao_reais, real))

# Conversão de real para dólar
real2 = valor_de_conversao_reais * taxa_dolar
print("O valor de {} reais equivalem a {} dólares.".format(valor_de_conversao_reais, real2))


#Ex 4: 
#Pedir a idade ao usuário, e testar se ele pode participar da competição, e qual categoria ele seria.  
#de 5 a 7 infantil A, 8 a 10 infantil B, 11 a 13 Juvenil A, 14 pra cima Sênior.

#variavel
idade = int(input("Qual é a sua idade? "))

#Categorias
if (idade >= 5 and idade <= 7):
    categoria = "Infantil A"
    print("Categoria: {}".format(categoria))
elif (idade >= 8 and idade <= 10):
    categoria = "Infantil B"
    print("Categoria: {}".format(categoria))
elif (idade >= 11 and idade <= 13):
    categoria = "Juvenil A"
    print("Categoria: {}".format(categoria))
else:
    print("Categoria: {}".format("Sênior"))

