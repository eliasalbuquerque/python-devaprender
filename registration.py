# 202311 - Python 3.12.
# author: Elias Albuquerque
# 2 - Como receber e trabalhar com dados
# 2.15 - Projeto 1 - Cadastre-me!


# SPRINT 1
# -[x] fazer funcionar;
# SPRINT 2
# -[x] remover h, min, seg, miliseg do registro;
# -[x] tratar string do nome para primeira letra maiuscula e o resto minusculas;


# MODULO 1 - Gerar registro do funcionario
from datetime import datetime
import random

# 1. Obtenha o nome do usuário
usr_name = input('Digite seu nome: ')
usr_name = usr_name.capitalize()

# 2. Obtenha a idade do usuário
# 5. Guarde informações sobre a data de aniversário do funcionário(dd/mm/aaaa)
current_date = datetime.now()

usr_birth = datetime.strptime(
    input('Qual a data do seu aniversário? (dd/mm/aaaa): '), '%d/%m/%Y')

usr_age = current_date.year - usr_birth.year

if (current_date.month, current_date.day) < (usr_birth.month, usr_birth.day):
    usr_age -= 1

# 3. Registre de forma automática a data do cadastro do usuário, usando a data
# do registro como data de registro
now = current_date.strftime('%d/%m/%Y')

# 4. Para cada novo funcionário que é registrado na empresa, ele recebe um dos
# seguintes cartões, que é sorteado de forma aleatória:
cartoes = ['R$50,00', 'R$250,00', 'R$120,00']
sorteio = random.choice(cartoes)


# MODULO 2 - Gerar apreserntacao do funcionario
print(f'Olá {usr_name}, seu registro foi concluído com sucesso no dia {now}.')
print(f'Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de {sorteio}.')


# SPRINT 3
# -[ ] aprender a desenvolver um teste simples;
