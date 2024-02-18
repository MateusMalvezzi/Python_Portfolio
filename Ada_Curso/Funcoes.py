# Criação de funções 

def saudacao():
    print('Seja bem-vindo!')
    
saudacao()

def saudacao(nome, curso):
    print(f'Seja bem-vindo, {nome} !')
    print(f'É um prazer fazer o curso de {curso} !')
saudacao('Mateus', 'Python')

# Funções com parâmetros default

def saudacao(nome, curso='Python'):
    print(f'Seja bem-vindo, {nome} !')
    print(f'É um prazer fazer o curso de {curso} !')
saudacao('Mateus', 'Python')

# Funções com retorno

def soma(num1, num2):
    print('Soma =', num1 + num2)
    
soma (8, 10)