
#Faça um programa que receba a idade e o peso de sete pessoas. Calcule e mostre;

#a quantidade de pessoas com mais de 90 quilos;
#a média das idades das sete pessoas.

pessoas_max=0
idades=[]
pessoas_noventa=0
while pessoas_max<7:
    pessoas_max+=1
    idade=int(input("Digite a idade da pessoa: "))
    idades.append(idade)
    peso=float(input("Digite o peso da pessoa em quilos: "))
    if peso>90:
        pessoas_noventa+=1

media=sum(idades)/len(idades)
print(f"A media das idades é de : {media} anos.")
print(f"A quantidade de pessoas com mais de 90 quilos é de {pessoas_noventa} pessoas.")