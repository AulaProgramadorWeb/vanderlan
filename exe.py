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

