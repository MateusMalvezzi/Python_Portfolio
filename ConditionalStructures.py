"""
idade = int(input('Qual a sua idade?'))
if idade >= 18:
    print('Você é maior de idade')
else:
    print('Você é menor de idade.')

Imagine que você queira imprimir Aprovado(a), caso o estudante tenha uma média superior ou igual a &, e "Reprovado", caso a média seja inferior a 7
"""

primeira_nota = float(input('Qual foi a sua primeira nota?'))
segunda_nota = float(input('Qual foi a sua segunda nota?'))
terceira_nota = float(input('Qual foi a sua terceira nota?'))
media = ((primeira_nota + segunda_nota + terceira_nota) / 3)

if(media >= 7):
    print('Você foi aprovado com media', media)
elif (media >=5 and media < 6.9):
    print('Você está de recuperação com media', media)
else:
    print('Você foi reprovado com media', media)