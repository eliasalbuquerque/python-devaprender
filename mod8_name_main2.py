# 202312 - Python 3.12.0
# 8.5 - Como usar - if __name__ == '__main__'


from mod8_name_main import faca_algo, faca_algo_uma_unica_vez


# executando funcao sem condicao "if __name__ == '__main__'"
faca_algo()

# executando funcao com condicao "if __name__ == '__main__'"
faca_algo_uma_unica_vez()



# NOTE:
# faca_algo() ira rodar duas vezes pq no `from mod8_name_main`, o import do 
# modulo roda o script inteiro e depois volta para o script de import, que 
# executa mais uma vez a funcao no modulo original.
# Para evitar duplicidade de execucao, é realizada a condicao: 
# `__name__ == __main__` que garante uma única execucao, mesmo durante a 
# importacao do modulo.