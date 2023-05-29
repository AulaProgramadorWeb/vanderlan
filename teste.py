idade = int(input("Qual é a sua idade? "))

if idade >= 5 and idade <= 7:
    print("Categoria: {}".format("Infantil A"))
elif idade >= 8 and idade <= 10:
    print("Categoria: {}".format("Infantil B"))
elif idade >= 11 and idade <= 13:
    print("Categoria: {}".format("Juvenil A"))
else:
    print("Categoria: {}".format("Sênior"))

