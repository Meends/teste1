#Escreva um programa que receba como entrada um valor inteiro em reais e 
#imprima na tela a quantidade necessária de notas de R$ 100, R$ 50, R$ 20, R$10, R$ 5, R$ 2 e R$ 1 
#para pagar esse valor com o menor número de notas possível. Por exemplo,
#para pagar R$ 80 são necessárias apenas três notas, uma nota de R$ 50, uma nota de R$ 20 e uma nota de R$10.
 
#Considere que no inicio da execução do programa existem disponíveis somente 5 notas de cada valor totalizando R$ 940.
#5 notas de R$ 100         = R$ 500	
#5 notas de R$ 50           = R$ 250
#5 notas de R$ 20           = R$ 100
#5 notas de R$10            = R$ 50
#5 notas de R$ 5             = R$ 25
#5 notas de R$ 2             = R$ 10
#5 notas de R$ 1             = R$ 5
#Total em Reais = R$ 940
 
#O usuário poderá realizar vários saques sem necessitar executar o programa novamente.
#O primeiro saque deve ser no máximo de R$ 940 e os demais dependerá do saldo restante.
#Para pagar R$ 670 são necessárias apenas 9 notas, cinco notas de R$ 100, três nota de R$ 50 e uma nota de R$20.
# Quantidade inicial de cada nota
notas_disponiveis = {
    100: 5,
    50: 5,
    20: 5,
    10: 5,
    5: 5,
    2: 5,
    1: 5
}

def total_disponivel():
    return sum(valor * qtd for valor, qtd in notas_disponiveis.items())

def exibir_notas():
    print("Notas disponíveis:")
    for nota in sorted(notas_disponiveis.keys(), reverse=True):
        print(f"R$ {nota}: {notas_disponiveis[nota]}")

def sacar(valor):
    global notas_disponiveis
    if valor > total_disponivel():
        print("Saldo insuficiente para o saque.")
        return

    saque = {}
    restante = valor

    for nota in sorted(notas_disponiveis.keys(), reverse=True):
        usar = min(restante // nota, notas_disponiveis[nota])
        if usar > 0:
            saque[nota] = usar
            restante -= nota * usar

    if restante > 0:
        print("Não é possível realizar o saque com as notas disponíveis.")
    else:
        for nota, qtd in saque.items():
            notas_disponiveis[nota] -= qtd
        print(f"Saque de R$ {valor} realizado com as seguintes notas:")
        for nota in sorted(saque.keys(), reverse=True):
            print(f"R$ {nota}: {saque[nota]}")
        print(f"Saldo restante: R$ {total_disponivel()}")

# Loop principal
print("Caixa Eletrônico - Notas Limitadas")
exibir_notas()

while True:
    try:
        entrada = input("\nDigite o valor para saque (ou 'sair' para encerrar): ")
        if entrada.lower() == 'sair':
            print("Encerrando o programa.")
            break
        valor = int(entrada)
        if valor <= 0:
            print("Digite um valor positivo.")
        else:
            sacar(valor)
            exibir_notas()
    except ValueError:
        print("Entrada inválida. Digite um número inteiro ou 'sair'.")