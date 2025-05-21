import math
num=int(input("Digite um número: "))
a=0
e=0
fatorado=0
for i in range(a,num,1):
    a+=1
    fatorado= math.factorial(a)
    e+=fatorado
    print (f"o fatorial de {a} é {fatorado}.")
print(f"A soma de tudo(E) ={e}")
