import sys

def main():
    #idade para abilitação
    ipa = int(input("Quantos anos você tinha quando se inscreveu para tirar a habilitação? "))

    if ipa < 18:
        print()
        print("Opa, tem algo errado! Você precisa de pelo menos 18 anos para tirar a carteira")
        sys.exit()

    #datas de renovaçao
    ddr = []

    print("Você tera que renovar a carteira com as seguintes idades:")
    while ipa < 100:
        if ipa >= 70:
            ipa += 3
        if ipa >= 50 and ipa < 70:
            ipa += 5
        if ipa < 50:
            ipa += 10
        ddr.append(ipa)
        
    print(ddr)
    
main()
