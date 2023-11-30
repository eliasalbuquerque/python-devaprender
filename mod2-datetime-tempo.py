# 202311 - Python 3.12.0
# 2 - Como receber e trabalhar com dados
# 2.11 - Datetime e Tempo

from datetime import datetime

print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)

# Criar uma data
daniel = datetime(2023, 11, 23)  # year, month, day
print(daniel)
print(type(daniel))

# Alterando formatacao de input
# dia, mes, ano (padrao pt-br)
uma_data = datetime.strptime(
    input('Digite uma data (dia/mês/ano): '), '%d/%m/%Y')
print(uma_data)

# Calcular o intervalor entre duas datas
data_atual = datetime.now()
dias = data_atual - uma_data
print(dias)

# DESAFIO
# Calcule quantos dias faltam até o seu aniversário

# 1. input data do aniversario
data_aniversario = input('Digite sua data de aniversario (ddmm): ')

# 2. verificar se o aniversario ja passou da data atual
if int(data_aniversario[2:4]) >= int(datetime.now().month):
    ano = datetime.now().year
else:
    ano = datetime.now().year + 1

# 3. transformar string em objeto datetime
aniversario = datetime(
    ano, int(data_aniversario[2:4]), int(data_aniversario[:2]))

# 4. subtrair datas
diferenca_datas = aniversario - datetime.now()

# 5. para contar o dia de hoje como dia util
faltam_dias = diferenca_datas.days + 1

# 6. print
if faltam_dias > 1:
    print(str(faltam_dias) + ' dias')
elif faltam_dias == 1:
    print(str(faltam_dias) + ' dia')
    print('Seu aniversário é amanhã.')  
else:
    print(str(faltam_dias) + ' dias')
    print('Parabéns, hoje é seu aniversário!')
