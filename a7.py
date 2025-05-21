#Modificar o programa anterior para que ao final ele pergunte ao usuário
#Se ele deseja informar um outro número. Caso positivo, o programa deve ser repetido.
check='1'
while check=='1':
    try:
        num = int(input("Digite um número positivo inteiro: "))
        if num < 1:
            print("Isso não é um número positivo inteiro.")
        else:
            print(f"Números pares entre 1 e {num}:")
            for i in range(1, num):
                if i % 2 == 0:
                    print(f"{i}, ", end="")
            print()  
            check=input("Deseja utilizar outro numero?[S/N]")
            if check=='N':
                    print("fim do app")
                    break
            if check=='S':
                check='1'
    except ValueError:
        print("Isso não é um número positivo inteiro.")
