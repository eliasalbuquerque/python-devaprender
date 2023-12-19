# 202312 - Python 3.12.0
# 8.5 - Como usar - if main == '__main__'


# funcao com execucao direta
def faca_algo():
    print('1. Rodando script apenas uma vez')

faca_algo()


# funcao com condicao de execucao
def faca_algo_uma_unica_vez():
    print('2. Usando "if __name__ == \'__main__\'"')

if __name__ == '__main__':
    faca_algo_uma_unica_vez()