
q = int(input("Qual a quantidade de termos? "))
n = 1
soma = 0

while n != 0:
    print()
    n = float(input("Digite um número: "))
    soma = soma + n
print("A média é: ",soma / q)
