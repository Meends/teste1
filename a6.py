
while True:
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
            break  
    except ValueError:
        print("Isso não é um número positivo inteiro.")
