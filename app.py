# O Dado possui 6 lados númerados de 1 a 6
# Objetivo do programa: Gerar um valor aleatório de 1 a 6
# Os numeros serão lançados no CONSOLE, fique atento na execução

# A biblioteca random é responsável por gerar valores aleatórios.

import random

# Inferface para o simulador

import PySimpleGUI as sg #implementação da interface

class SimuladorDeDado:
    def __init__(self):
        # Valor Inicial
        self.valor_minimo = 1
        # Valor máximo
        self.valor_maximo = 6
    
        # Template
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('Sim'), sg.Button('Não')]
        ]

    def iniciar(self):
        # Janela
        self.janela = sg.Window('Simulador de Dado',layout=self.layout)
        # Ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
         # Tratamento de Excessões
        try:
            if self.eventos == 'Sim' or self.eventos == 's':
                self.GerarNovoValor()
            elif self.eventos == 'Não' or self.eventos == 'n':
                print('Programa finalizado.')
            else:
                print('Digite somente [sim] ou [não]')
        except:
                print('Erro ao receber sua resposta. Tente novamente um novo valor.')
    def GerarNovoValor(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

    # Instanciar a classe
simulador = SimuladorDeDado()
simulador.iniciar()