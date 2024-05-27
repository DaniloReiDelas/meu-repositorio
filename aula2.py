idade = int(input("insira sua idade: \n"))

if idade > 100 or idade <= 0:
    print("idade invalida")
else:
    if idade < 13:
        print("voce eh um infantil")
    elif 18 > idade >= 13:
        print("voce eh um adolescente")
    elif idade >= 18:
        print("voce eh um adulto")
    else: 
        print("Inválido")