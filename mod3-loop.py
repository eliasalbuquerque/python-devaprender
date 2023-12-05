# 202312 - Python 3.12.0
# 3 - Aprenda a controlar o fluxo de seus programas
# 3.10 - Loop For (Laço For)
# 3.11 - Nested Loops (Loops aninhados)
# 3.13 - Loop While (Laço While)


# 3.10 - Loop For (Laço For)


# laco do 1 ao 20
for i in range (1, 21):
    print(i)

# laco do 1 ao 20 de 2 em 2 (step)
for i in range (1, 20, 2):
    print(i)

# laco com iteraveis
nomes = ['Jeff','Elon','Mark','bill']
for nome in nomes:
    print(nome)

# Desafio 1
# Usando um loop, exiba na tela: Estamos em X onde x é um valor iniciando em 18 
# e finalizando em 110
for numero in range(18, 111):
    print(f'estamos em {numero}')

# Desafio 2
# Você precisa de 10 passos para finalizar uma tarefa, exiba na tela, usando 
# loop for a seguinte frase: "Realizando Passo X"
for passo in range(1, 11):
    print(f'realizando passo {passo}')


# 3.11 - Nested Loops (Loops aninhados)


paises = ['Brasil','India','Estados Unidos','China']
estacoes = ['primavera','verao','outono','inverno']

for pais in paises:
    for estacao in estacoes:
        print(f'{pais} {estacao}')

# DESAFIO
celulares = ['Asus', 'Samsung', 'Sony', 'IPhone']
versoes = ['Plus', 'Premium Plus', 'Premium Deluxe', 'Plus Premium Ultra']

for celular in celulares:
    for versao in versoes:
        print(celular, versao)


# 3.13 - Loop While (Laço While)


# contador
tentativas = 0
while tentativas < 3:
    tentativas += 1 #incremento
    print(f'tentativa {tentativas}')

# senha
senha = ''
while senha != '1234':
    senha = input('Digite sua senha: ')
print('Boas vinhas')

# DESAFIO 1 - Crie um loop while que irá contar e imprimir no console de 1 até 
# 120
counter = 1
while counter <= 120:
    print(f'desafio 1: {counter}')
    counter += 1

# DESAFIO 2 - Crie um loop while que irá continuamente pedir ao usuário a senha 
# para entrada, e só irá permitir o programa continuar caso ele digite a senha 
# 'secreto'
senha = ''
while senha != 'secreto':
    senha = input('desafio 2: digite sua senha "secreta": ')
    senha = senha.lower()
print('desafio 2: finalizado!')

# DESAFIO 3 - Crie um loop que conte e imprima na tela o valor em ordem 
# descrescente de 100 para 1
counter3 = 100
while counter3 >= 1:
    print(f'desafio 3: {counter3}')
    counter3 -= 1
