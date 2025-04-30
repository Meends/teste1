#Faça um programa que receba várias idades
#e que calcule e mostre a média das idades digitadas. Finalize digitando idade igual a 0.
check=1
idades=[]
while check==1:
    idade=int(input("Digiter a idade da pessoa(digite 0 para finalizar)"))
    if idade==0:
        break
    idades.append(idade)

print(f"idades recebidas:{idades}")
