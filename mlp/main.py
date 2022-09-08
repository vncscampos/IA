from mlp import MLP
from database import Database

and_table = [[[0,0], [0]],
             [[0,1], [0]],
             [[1,0], [0]],
             [[1,1], [1]]]

or_table = [[[0,0], [0]],
             [[0,1], [1]],
             [[1,0], [1]],
             [[1,1], [1]]]

xor_table = [[[0,0], [0]],
             [[0,1], [1]],
             [[1,0], [1]],
             [[1,1], [0]]]

robo_table = [[[0,0,0],[1,1]],
              [[0,0,1],[0,1]],
              [[0,1,0],[1,0]],
              [[0,1,1],[0,1]],
              [[1,0,0],[1,0]],
              [[1,0,1],[1,0]],
              [[1,1,0],[1,0]],
              [[1,1,1],[1,0]]]

ERA = 10000

# Bases triviais
# QTD_IN = 3
# QTD_OUT = 2
# QTD_H = 2
# NI = 0.3
# TABLE = robo_table

# Base individual
QTD_IN = 21
QTD_OUT = 10
QTD_H = 12
NI = 0.0001
TABLE = Database().table

rna = MLP(QTD_IN, QTD_OUT, QTD_H, NI)

for e in range(ERA):
    erro_epoca_aprox = 0
    
    for a in range(len(TABLE)):
        amostra = TABLE[a].copy()
        x_in = amostra[0].copy()
        y = amostra[1].copy()
        erro_amostra_prox = 0

        o = rna.training(x_in, y)

        for i in range(len(o)):
            erro_amostra_prox += abs(y[i] - o[i])
        
        erro_epoca_aprox += erro_amostra_prox

    print("Época: {} - Erro de aproximação: {}".format(e, erro_epoca_aprox))
