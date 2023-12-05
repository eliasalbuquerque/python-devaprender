# 202311 - Python 3.12.0
# 3 - Aprenda a controlar o fluxo de seus programas
# 3.14 - Pass - Não tá pronto Não tem problema
# 3.15 - Break e Continue


# 3.14 - Pass - Não tá pronto Não tem problema


numero = 0
while numero < 0:
    pass

for numero in range(10):
    pass

print('passou')


# 3.15 - Break e Continue


# Continue: ignorar/pular

# imprimi números pares
for num in range(1, 11):
    if num % 2 == 0:
        print(num)
    else:
        continue

# imprimi números não pares
for num in range(1, 11):
    if num % 2 == 0:
        continue
    print(num)

# iteraveis
frutas = ['maça','manga','laranja','morango']
for fruta in frutas:
    if fruta == 'manga': # não imprimi 'manga'
        continue
    print(f'{fruta}')


# Break

# imprimi até o limite desejado
for num in range(1, 11):
    if num > 5:
        break
    print(num)

# iteraveis
frutas = ['maça','manga','laranja','morango']
for fruta in frutas:
    if fruta == 'manga': # não imprimi a partir de 'manga'
        break
    print(f'{fruta}')


# DESAFIO 1
# Use a operação necessária(break ou continue) para que a seguinte 
# condição aconteça.
# * Ao cegar ao estilo "Rap" o mesmo não deve ser impresso na tela
estilos = ['Hip-Hop','Rock','Rap','Pop']
for estilo in estilos:
    if estilo == 'Rap': 
        continue
    print(f'desafio 1: {estilo}')


# DESAFIO 2 
# Use a operação necessária(braek ou continue) para que a seguinte 
# condição aconteça:
# * Ao chegar ao estilo "Rock" a execução deve interrompida
estilos = ['Hip-Hop','Rock','Rap','Pop']
for estilo in estilos:
    if estilo == 'Rock':
        break
    print(f'desafio 2: {estilo}')