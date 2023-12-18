# 202312 - Python 3.12.0
# 6.2 - O que fazer quando coisas dão errado
# 6.3 - Não decore exceções, faça isso
# 6.4 - Finally! (execute código mesmo em casos de erro)
# 6.5 - Log e Logging (Uma forma de manter um histórico de o que acontece na
# 		sua aplicação)
# 6.6 - Mantendo um log (histórico) de exceções


'''
The most commonly used exceptions in Python:

- SyntaxError: Raised by the parser when a syntax error is encountered1.
- NameError: Raised when a variable is not found in local or global scope21.
- TypeError: Raised when an operation or function is applied to an object of 
  inappropriate type.
- ValueError: Raised when a built-in operation or function receives an argument 
  that has the right type but an inappropriate value3.
- IndexError: Raised when the index of a sequence is out of range21.
- KeyError: Raised when a key is not found in a dictionary21.
- AttributeError: Raised when an attribute reference or assignment fails3.
- ImportError: Raised when the imported module is not found3.
- ZeroDivisionError: Raised when the second argument of a division or modulo 
  operation is zero32.
'''

import logging


# 6.2 - O que fazer quando coisas dão errado


# excessão mais básica
try:
    # valor = int(input('Digite um valor em dolares: '))
    valor = 5
    print(f'1. valor em reais: R${valor * 5.25}')
except:
    print('1. Favor digitar apenas números')

print()


# 6.3 - Não decore exceções, faça isso


try:
    meses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print(f'2. {meses[15]}')

# copie o erro do console e use na expressao
except IndexError as erro:
    print('2. Favor acessar um índice válido')
    print(erro)  # nunca exibir isso para o usuário

print()


# 6.4 - Finally! (execute código mesmo em casos de erro)


# 3. exemplo 1
internet = None

try:
    print('3. Fazendo conexao com a ' + internet)
except TypeError as erro:
    print('3. Não há conexão com a internet')

# quanto é algo precisa ser processado mesmo quando ocorre um erro
finally:
    print('3. Desfasendo a compra!')


# 4. exemplo 2
try:
    # valor = int(input('4. Digite um valor: '))
    print(f'4. divisao: {valor / 0}')
except ZeroDivisionError as erro:
    print('4. Não é possível dividir por zero!')
except ValueError as erro:
    print('4. Favor digitar somente números')
finally:
    print('4. A operação foi cancelada!')

print()


# 6.5 - Log e Logging (Uma forma de manter um histórico de o que acontece na
# 		sua aplicação)


'''
# Para a utilizacao:

Deve se saber qual o nivel de impacto na aplicacao tem a informacao que estou 
guardando no logging.

- debug: só estou adicionando informacoes para desenvolvedores;
- info: só quero informar algo que esta acontecendo no programa mas nao é erro;
- warning: quero alertar sobre algo que esta acontecendo fora do esperado, nao 
  é um erro, mas pode gerar um futuramente;
- error: um erro ocorreu na aplicacao;
- critical: um erro com conseguencias graves acaba de ocorrer na aplicacao;
'''


# 1. para exibir logging de 'debug' e 'info' no terminal:
# logging.basicConfig(level=logging.DEBUG)


# 2. para criar arquivo de log para acesso e análise:
# parametro: setar o level
# parametro: filename define o nome do arquivo
# parametro: filemode define se o arquivo escreve "w" ou acrescenta "a" dados
# parametro: format define o formato

logging.basicConfig(level=logging.DEBUG, encoding='utf-8',
                    filename='app.log', filemode='a', format='%(levelname)s - %(message)s - %(asctime)s')


# mensagens de logging:
""" 
logging.debug('Logging nível debug')
logging.info('Logging nível info')
logging.warning('Logging nível warning')
logging.error('Logging nível error')
logging.critical('Logging nível critical')
 """


# 6.6 - Mantendo um log (histórico) de exceções



try:
    email = input('5. Digite seu e-mail: ')
    senha = int(input('5. Digite sua senha: '))
    if senha == 1234:
        logging.info(f'{email} fez login')
except ValueError as erro:
    print('5. Favor digitar apenas números')
    logging.warning(erro)
