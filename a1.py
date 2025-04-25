#Fazer um programa para ler os dados (matrícula, idade, sexo, altura e concursado [S/N]) de vários funcionários de uma empresa.
#O último tem a matrícula igual a zero e não entra nos cálculos.
#Calcular e mostrar:
#o número de funcionárias concursadas;
#o número de funcionários (somente homens);
#a maior idade dos homens concursados;
#a quantidade de mulheres com mais de 30 anos sem concurso;
#a quantidade de concursados(as);
#a média das alturas dos homens com menos de 40 anos.

funcionarios=[]

num_funcionarias_con = 0
num_funcionarios_hom = 0
maior_idade_hom_con = 0
mais_trinta_mulher_semcon = 0
num_con = 0
med_alt_homem_menos_quarenta = 0
cont_homens_menos_quarenta = 0
stop=1
while True:
    matricula = int(input("Digite a matricula: "))
    if matricula == 0:
        break
    
    idade = int(input("Digite a idade do funcionário: "))
    sexo = (input("Digite o sexo do funcionário: [M/F]"))
    altura = float(input("Digite a altura do funcionário: "))
    concursado = input("O funcionário é concursado? [S/N]")

    funcionario = {
    'matricula': matricula,
    'idade': idade,
    'sexo': sexo,
    'altura': altura,
    'concursado': concursado
}

    funcionarios.append(funcionario)

    #calculos das estatisticas
    if sexo == 'F' and  concursado =='S':
        num_funcionarias_con +=1

    if sexo == 'M': 
        num_funcionarios_hom +=1

        if concursado == 'S' and idade > maior_idade_hom_con:
            maior_idade_hom_con=idade
    
        if idade<40:
            med_alt_homem_menos_quarenta += altura
            cont_homens_menos_quarenta += 1
        
    if sexo == 'F' and idade > 30:
        mais_trinta_mulher_semcon += 1
    
    if concursado == 'S':
        num_con +=1

#media altura homem

if cont_homens_menos_quarenta > 0:
    med_alt_homem_menos_quarenta/cont_homens_menos_quarenta
else:
    cont_homens_menos_quarenta=0

print("RESULTADOS")
print("Número de funcionárias concursadas:", num_funcionarias_con)
print("Número de funcionários homens:", num_funcionarios_hom)
print("Maior idade dos homens concursados:", maior_idade_hom_con)
print("Quantidade de mulheres com mais de 30 anos sem concurso:", mais_trinta_mulher_semcon)
print("Total de concursados(as):", num_con)
print("Média das alturas dos homens com menos de 40 anos:", round(med_alt_homem_menos_quarenta, 2))

# Exibindo os dados armazenados
print("\nDADOS DOS FUNCIONÁRIOS:")
for f in funcionarios:
    print(f)