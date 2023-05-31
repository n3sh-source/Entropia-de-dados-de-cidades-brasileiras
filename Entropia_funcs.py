"""
Trabalho de Entropia

Gustavo Costa Arakaki
"""

import math as m

#Probabilidade das classes
def probs(dados):
    return [dados.count(x)/len(dados) for x in set(dados)]

#Entropia
def entropia(probs):
    return -sum([x * m.log2(x) for x in probs])

#Entropia Maxima
def MAXentropia(dados):
    return m.log2(len(set(dados)))







