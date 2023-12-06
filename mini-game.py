# Desafio 1
# Monte um mini-game turtle, que possibilite que o usuário controle para qual
# direção a tartaruga deve andar(frente/trás) e qual ângulo deverá ser tomado a
# cada nova movimentação


# Desafio 2
# Usando o mini-game, desenha um quadrado passando instruções para a turtle, 
# totalmente através do input do usuário


# Dicas Iniciais
# * Crie uma nova turtle primeiro
# * Coloca seu programa em loop
# * Faça perguntas ao usuário para decidir se a tartaruga deve movimentar para 
#   frente ou para trás
# * Após decidir se ele deve movimentar para frente ou para trás, receba do 
#   usuário quantos pixels devem ser percorridos
# * Faça perguntas ao usuário para decidir se a tartaruga deve rotacionar para 
#   esquerda ou direta
# * Após decidir se ele deve rotacionar para esquerda ou direita, receba do 
#   usuário quantos pixels devem ser rotacionados
# * Ao executar essa ação pergunte ao usuário "Continuar andando?", e reaga de 
#   acordo com a resposta do usuário.

# Dicas Adicionais
# * Não esqueça de converter o input do usuário para o tipo apropriado
# * Resolva um problema de cada vez e lembre de seguir a seguinte lógica:
# Pergunte -> Processe resposta -> A

# import turtle as t
# from random import random

# for i in range(100):
#     steps = int(random() * 100)
#     angle = int(random() * 360)
#     t.right(angle)
#     t.fd(steps)

# from turtle import Turtle
# from random import random

# t = Turtle()
# for i in range(100):
#     steps = int(random() * 100)
#     angle = int(random() * 360)
#     t.right(angle)
#     t.fd(steps)

# t.screen.mainloop()

# Importing turtle module
import turtle
import os

# criando o objeto 
t = turtle.Turtle()

# criando config iniciais
t.speed(1)
t.shape("turtle")
t.color("green")

# manual do jogo
print('MOVIMENTAÇÃO:')
print('Direção:\n\ta = para trás\n\ts = para baixo\n\td = para frente\n\tw = para cima')
print('Distância: de 1 a 10') 
print('Exemplo:\n\tInserir direção e distância: a10')

# movimentacao
while True:
    dist = input('Inserir direção e distância: ')
    t.forward(dist)


# t.forward(100)
# t.right(90)
# t.forward(100)

# Hiding the turtle
# t.hideturtle()


# ------------- SPACE TO FINISH APP ----------------
# Function to close the window when space key is pressed
# def close_window():
    # turtle.bye()

# Binding the space key to the close_window function
# turtle.onkey(close_window, "space")

# Listening for key presses
# turtle.listen()
# ------------- SPACE TO FINISH APP ----------------


# Keeping the window open until it is manually closed or space key is pressed
turtle.mainloop()
