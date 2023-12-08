# 202312 - Python 3.12.0
# 4.7 - Decorators - Aproveitando e estendendo o que já está pront


from datetime import datetime, timedelta
import random


# chamar funcao dentro de funcao
def depositar_dinheiro():
    print('1. depositando dinheiro')

    def depositando_dolar():
        print('- depositando dolares')

    def depositando_reais():
        print('- depositando reais')

    depositando_dolar()
    depositando_reais()


depositar_dinheiro()


# retornar referencia de funcoes
def pai(numero):

    def filho_1():
        print('2. Sou filho 1')
        # ID comparacao com ID resultado()
        print(f"ID objeto filho_1   : {id(filho_1)}")

    def filho_2():
        print('2. Sou filho 2')
        # ID comparacao com ID resultado()
        print(f"ID objeto filho_2   : {id(filho_2)}")

    if numero == 1:
        return filho_1

    if numero == 2:
        return filho_2


resultado = pai(2)
resultado()

# ID comparacao com ID filho_1() e filho_2()
print(f"ID objeto resultado : {id(resultado)}")

'''
NOTE:
No código, a função `pai()` retorna uma referência para as funções `filho_1()` 
ou `filho_2()`, dependendo do valor do argumento `numero`. Quando você chama 
`pai(2)`, a função `pai()` retorna uma referência para a função `filho_2()`. 
Essa referência é então armazenada na variável `resultado`. Quando você chama 
`resultado()`, você está realmente chamando a função `filho_2()`, por esse 
motivo, tanto `resultado` como `filho_2` tem o mesmo ID.

Aqui está uma explicação passo a passo:

1. Você chama a função `pai()` com o argumento `2`.
2. Dentro da função `pai()`, o número `2` corresponde à função `filho_2()`, 
   então `filho_2()` é retornado.
3. A referência para a função `filho_2()` é armazenada na variável `resultado`.
4. Quando você chama `resultado()`, você está realmente chamando `filho_2()`, 
   então "2. Sou filho 2" é impresso na tela.
'''


# usando @ (decorator)
def meu_decorator(funcao):
    def wrapper():  # wrapper-en = pacote-ptbr
        print('3. antes da função')
        funcao()
        print('3. depois da função')
    return wrapper


@meu_decorator  # note:
def parabenizar():
    print('3. Parabéns!!')

# parabens = meu_decorator(parabenizar)
# parabens()


parabenizar()

'''
NOTE:
`@meu_decorador` é chamado de "decorador" e substitui o uso da variavel 
`parabens`.

No código, `@meu_decorator` é aplicado à função `parabenizar()`. Isso significa 
que `parabenizar()` será passada como argumento para a função `meu_decorator()
`, e o resultado dessa função (que é a função `wrapper()`) será usado no lugar 
de `parabenizar()`.

Portanto, quando você chama `parabens()`, você está realmente chamando a função 
`wrapper()` que foi retornada por `meu_decorator(parabenizar)`.
'''


# DESAFIO 1
# Crie um decorador que irá pegar a função que for passada para ele e imprimir
# o horário atual antes de executar a função e depois imprimir o horário após
# finalizar a execução da função.

# 1. funcao(arg)
#    pacote:
#    a. horario atual
#    b. funcao()
#    c. horario final apos executar b
# 2. funcao-arg()
#    registro
# 3. chamar funcao-arg()

def log_entrada_saida(function):
    def pacote():

        # entrada != saída em segundos
        now = datetime.now()
        atraso = random.randint(1, 10) + random.random()
        saida = now + timedelta(seconds=atraso)

        print(f'h.entrada: {now.time()}')
        function()
        print(f'h.saída: {saida.time()}')

    return pacote


@log_entrada_saida
def registro():
    print('entrada do registro')


registro()
