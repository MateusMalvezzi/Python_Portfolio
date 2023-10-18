soma = 0 

for i in range(1, 4):
    nota = float(input(f'Informe sua nota {i}: '))
    soma = soma + nota
    nota_final = soma / 3
if nota_final > 6:
    print('Parabéns, aprovado com média', nota_final)
else:
    print('Reprovado com média', nota_final)

"""
for i in range(10): # > Vai de 0 até o número range -1
    print(i)

for i in range(1, 10): # > Vai de valor de inicio até o número final -1
    print(i)

for i in range(2, 23, 2): # > Digo qual o valor de início, valor de passo(de quanto em quanto eu quero pular) e de parada/step
    print(i)
"""