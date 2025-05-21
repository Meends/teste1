#Implemente um programa que receba o valor da compra e o valor pago pelo cliente.
#O programa deve calcular o troco e informar quantas notas de cada valor serão entregues,
#usando o menor número possível de notas, respeitando a quantidade limitada disponível.
#Após cada operação, atualize o estoque de notas.

#🧾 Especificações:
#O caixa possui 5 notas de cada valor: R$ 100, R$ 50, R$ 20, R$ 10, R$ 5, R$ 2, R$ 1.

#O programa deve continuar executando enquanto houver notas disponíveis.

#Se não for possível fornecer o troco exato com as notas disponíveis, informe o erro.

#O usuário pode digitar sair para encerrar.

qtd_notas_disponiveis= {
    100:5,
    50:5,
    20:5,
    10:5,
    5:5,
    2:5,
    1:5
}

while True:
    entrada=(input("Digite o valor da compra:\n(Para sair digite [sair]) ")).strip().lower()
    if entrada=='sair':
        print("programa encerrado.")
        break
    valor_compra=float(entrada)
    valor_pago=float(input("Digite o valor pago pelo cliente: "))
    troco = round(valor_pago-valor_compra)

    if troco<0:
        print("Valor pago é insuficiente")
        continue
    elif troco==0:
        print("Não há troco a ser dado")
        continue

    print(f"O troco necessário é de: R${troco}")

    troco_a_dar=troco
    notas_usadas={}

    for nota in sorted(qtd_notas_disponiveis.keys(), reverse=True):
        max_notas=min(troco_a_dar // nota, qtd_notas_disponiveis[nota])
        if max_notas > 0:
            notas_usadas[nota] = max_notas
            troco_a_dar -= nota * max_notas
    
    if troco_a_dar == 0:
        print("Troco entregue")
        for nota, qtd in notas_usadas.items():
            print(f"R${nota}: {qtd}")
            qtd_notas_disponiveis[nota]-=qtd #atualiza o estoque
        print("Notas restantes no caixa:")
        for nota in sorted(qtd_notas_disponiveis.keys(), reverse=True):
            print(f"R${nota}: {qtd_notas_disponiveis[nota]}")
    else:
        print("Não é possível fornecer o troco com as notas disponíveis.")
