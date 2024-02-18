idade = '26'

print(idade, type(idade))

idade_inteira = int(idade)

print(idade_inteira, type(idade_inteira))

# int()  >> Converte 'qualquer coisa' para um inteiro // Converts 'anything' to an integer.
# str()  >> Qualquer tipo de variável para o tipo string // Any variable type to string type
# float()>> Qualquer tipo de variável para float // Any variable type to float type
# bool() >> Qualquer tipo de variável para booleano // Any variable type to bool type


#altura = input('Informe a sua altura: ') #Tudo que o user digitar é lido como string
#altura_convert = float(altura)
#print(altura_convert, type(altura_convert))

#otimizando a altura da L15
altura = float(input('Informe a sua altura: '))
print(altura, type(altura))