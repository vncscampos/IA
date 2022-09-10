from mlp import MLP
from database import Database

ERA = 10000

# Base individual
QTD_IN = 21
QTD_OUT = 10
QTD_H = 12
NI = 0.0001
TABLE_TREINO = Database().table
TABLE_TESTE = Database().table

rna = MLP(QTD_IN, QTD_OUT, QTD_H, NI)

for e in range(ERA):
    erro_epoca_treino = 0
    
    # Roda treino
    for a in range(len(TABLE_TREINO)):
        amostra = TABLE_TREINO[a].copy()
        x_in = amostra[0].copy()
        y = amostra[1].copy()
        erro_amostra_prox = 0

        o = rna.training(x_in, y)

        for i in range(len(o)):
            erro_amostra_prox += abs(y[i] - o[i])
        
        erro_epoca_treino += erro_amostra_prox

    # Roda teste
    erro_epoca_teste = 0
    for a in range(len(TABLE_TESTE)):
        amostra = TABLE_TESTE[a].copy()
        x_in = amostra[0].copy()
        y = amostra[1].copy()
        erro_amostra_prox = 0

        o = rna.execute(x_in)

        for i in range(len(o)):
            erro_amostra_prox += abs(y[i] - o[i])
        
        erro_epoca_teste += erro_amostra_prox

    print("Época: {} - Erro de aproximação treino: {} - Erro de aproximação teste: {}".format(e, erro_epoca_treino, erro_epoca_teste))
