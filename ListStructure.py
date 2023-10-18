# > LISTAS 

# Antes 
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# Com lista
notas = [7.9, 9.7, 8.2]

# > Criando listas 
lista = []
lista = list()
lista = [26, 'Mateus', 3.14159, False]
lista_de_listas = [10, [1, 2, 3]]

# > Indexação e Slices (fatiamento)
lista = [11, 'Mateus', 3.14154, True]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

print(lista[-1])

# Slices
lista = [10, 50, 30, 40, 25, 60, 5]
print(lista[0:3]) #retorna os valores: 10, 50, 30 >> começa no índice 0 e vai até menor que 3.
print(lista[0:6])
print(lista[3:]) # >> começa no índice 3 e vai até o final. 
print(lista[2:6:2]) # >> começa no 2, vai ao 6 mas PULA de 2 em 2. >> 30, 25

# > Iterações com FOR

# 1. Utilizando os próprios elementos da lista

for elemento in lista:
    print(elemento)

# 2. Utilizando os índices.

print('Comprimento da lista', len(lista))

for i in range(len(lista)):
    print(lista[i])