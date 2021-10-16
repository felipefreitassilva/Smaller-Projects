
q = int(input("Qual a quantidade de termos? "))
n = 1
soma = 0

print("Digite 0 como", q + 1, "dígito")

while n != 0:
    print()
    n = float(input("Digite um número: ")) or 0
    soma = soma + n
print("A média é: ", soma / q)
