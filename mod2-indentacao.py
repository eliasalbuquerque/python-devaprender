# 202311 - Python 3.12.0
# 2 - Como receber e trabalhar com dados
# 2.3 - Indentacao

import time

def PensarPor10Segundos():
    print('pensando')
    time.sleep(10)
    print('Lembrei!')

if 10 > 5:
    print('10 é maior que 5')

class BemVindo():
    def __init__(self):
        print('Bem vindo')

oi = BemVindo()