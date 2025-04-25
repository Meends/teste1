#Fazer um programa que solicite um número ao usuário e após mostre todos os números ímpares existentes 
# entre 0 e o número informado.

inicio=0
fim=int(input("Digite um numero"))

for i in range(inicio,fim,1):

    if i%2 != 0:
        print(i) 