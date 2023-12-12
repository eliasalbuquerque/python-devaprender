def colorir_mensagem(funcao):
    def wrapper(msg):
        print("\033[1;34m---------------------------------")
        funcao(msg)
        print("---------------------------------\033[0m")
    return wrapper

@colorir_mensagem
def print_colorido(mensagem):
    print(mensagem)

print_colorido('Olá mundo!')



import random

def sortear_numeros(function):
    def wrapper(*args):
        function(random.randint(*args))
    return wrapper

@sortear_numeros
def print_qualquer_coisa(*args):
    print(*args)

print_qualquer_coisa(1, 10)