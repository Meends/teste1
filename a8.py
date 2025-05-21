#Faça um programa que receba várias idades e que calcule e mostre a média das
#idades digitadas. Finalize digitando idade igual a 0.

check=1
idades=[]
while check==1:
    idade=int(input("Digite a idade do caba: "))

    if idade==0:
        break
    idades.append(idade)

if len(idades)>0:
    media = sum(idades)/ len(idades)
    print(f"A média das idades é de {media:.2f}.")

else:
    print("Nenhuma idade válida foi informada.")