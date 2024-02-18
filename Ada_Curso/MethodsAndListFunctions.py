# > MËTODOS DE LISTAS 

lista = [1, 2, 12, 8, 2]

# append

print ('Antes do append', lista) # >> retorna [1, 3, 12, 8, 2]

lista.append(3)

print ('Depois do append', lista) # >> retorna [1, 2, 12, 8, 2, 3]

# insert

lista.insert(2, 10)

print ('Depois do insert', lista) # >> retorna [1, 3, 10, 12, 8, 2, 3]

# extend

lista2 = [1, 2, 3]

lista.extend(lista2)

print ('Depois do extend', lista) # >> retorna [1, 3, 10, 12, 8, 2, 3, 1, 2 ,3]

# pop

lista.pop()
print('Lista após o pop:', lista) # >> retorna [1, 3, 10, 12, 8, 2, 3, 1, 2]

lista.pop(0)
print('Lista após o pop:', lista) # >> retorna [3, 10, 12, 8, 2, 3, 1, 2]

# remove

lista.remove()
print('Lista após o remove:', lista) # >> retorna [10, 12, 8, 2, 3, 1, 2]

# count 

print('Quantidade de 2 na lista:', lista.count(2)) # >> retorna: Quantidade de 2 na lista: 2

# index 

print('Índice do elemento 12:', lista.index(12)) # >> retorna: Índice do elemento 12: 1

# sort

lista.sort(reverse=True)

print(lista ) # >> retorna [12, 10, 8, 3, 2, 2, 1]

# FUNÇÕES PARA LISTAS 

# len
print(len(lista)) #>> 7

# sum
print(sum(lista)) # >> 38

# max
print('Maior elemento da lista', max(lista)) # >> 12

# min
print('Menor elemento da lista', min(lista)) # >> 1
