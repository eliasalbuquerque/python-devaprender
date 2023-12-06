# title: 'mini-game.py'
# author: 'Elias Albuquerque'
# version: 'Python 3.12.0'
# created: '2023-12-05'
# update: '2023-12-06'


# Desafio 1
# Monte um mini-game turtle, que possibilite que o usuário controle para qual
# direção a tartaruga deve andar(frente/trás) e qual ângulo deverá ser tomado a
# cada nova movimentação


# Desafio 2
# Usando o mini-game, desenha um quadrado passando instruções para a turtle, 
# totalmente através do input do usuário


import turtle
import os

# criando o objeto 
t = turtle.Turtle()

# criando config iniciais
t.speed(1)
t.shape("turtle")
t.color("green")

# funcao manual do jogo
def manual_jogo():
    print('----- MANUAL -----')
    print('Direção: a = para esquerda\n\t s = para baixo\n\t d = para direita\n\t w = para cima')
    print('Distância: de 1 a 10') 
    print('Exemplo: Inserir direção e distância: d10  --> direita 10 passos\n')

# funcao clear the terminal
def clear_terminal():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

# limpa o terminal e mostra o manual
clear_terminal()
manual_jogo()

# movimentacao da turtle
direcoes = ['a','s','d','w']

while True:
    coordenadas = input('Inserir direção e distância: ')
    direcao = coordenadas[0].lower()
    distancia = int(coordenadas[1:] + '0')

    if direcao in direcoes and distancia <= 100:

        # movimentar para esquerda 180°
        if direcao == 'a':
            t.seth(180)
            t.forward(distancia)

        # movimentar para baixo 270°
        if direcao == 's':
            t.seth(270)
            t.forward(distancia)

        # movimentar para direita 0°
        if direcao == 'd':
            t.seth(0)
            t.forward(distancia)

        # movimentar para cima 90°
        if direcao == 'w':
            t.seth(90)
            t.forward(distancia)

    else:
        print('\n> Inserir dados conforme MANUAL!')
        manual_jogo()

turtle.mainloop()
