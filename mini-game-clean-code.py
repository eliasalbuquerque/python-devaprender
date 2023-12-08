"""
title: 'mini-game-clean-code.py'
author: 'Elias Albuquerque'
version: 'Python 3.12.0'
created: '2023-12-08'
update: '2023-12-08'
"""


import turtle
import os

t = turtle.Turtle()

def configuracoes_iniciais():
    t.speed(1)
    t.shape("turtle")
    t.color("green")

def manual_jogo():
    print('----- MANUAL -----')
    print('Direção: a = para esquerda\n\t s = para baixo\n\t d = para direita\n\t w = para cima')
    print('Distância: de 1 a 10') 
    print('Exemplo: Inserir direção e distância: d10  --> direita 10 passos\n')

def clear_terminal():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def mover(direcao, distancia):
    if direcao == 'a':
        t.seth(180)
    elif direcao == 's':
        t.seth(270)
    elif direcao == 'd':
        t.seth(0)
    elif direcao == 'w':
        t.seth(90)
    t.forward(distancia)

def movimentar_turtle(funcao):
    def pacote():
        coordenadas = funcao()
        direcao = coordenadas[0].lower()
        distancia = int(coordenadas[1:] + '0')
        direcoes = ['a','s','d','w']

        if direcao in direcoes and distancia <=100:
            mover(direcao, distancia)
        else:
            print('\n> Inserir dados conforme MANUAL!')
            manual_jogo()
    return pacote

@movimentar_turtle
def inserir_coordenadas():
    return input('Inserir direção e distância: ')


# rodando a aplicacao
configuracoes_iniciais()
clear_terminal()
manual_jogo()

while True:
    inserir_coordenadas()

turtle.mainloop()