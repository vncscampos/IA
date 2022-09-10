from cmath import exp
import random
from typing import List
import sys

class Perceptron:
    def __init__(self, numIn:int, numOut:int, ni:float):
        self.__numIn = numIn
        self.__numOut = numOut
        self.__ni = ni
        self.__w = []
        self.__generate_weight()

    def learn(self, table: list, era:int):
        sample = len(table)

        for e in range(era):
            errorEra = 0
            errorSample = 0 #erro amostra

            for s in range(sample):
                x = table[s][:21]
                y = table[s][21:]

                u = []
                o = []
                
                error = 0
                for i in range(self.__numOut):

                    w = self.__w[i]

                    calc = w[0]
                    for j in range(self.__numIn):
                        calc += w[j+1] * x[j]

                    u.append(calc)

                    # Calcula teta da função sigmoidal
                    func = 0
                    try:
                        func = 1/(1+exp(-u[i]))
                    except OverflowError:
                        func = float('inf')
                        sys.exit()
                    o.append(func)

                    # Atualiza pesos
                    w[0] = self.__ni * (y[i] - o[i]) * 1
                    for j in range(1, len(w)):
                        w[j] += self.__ni * (y[i] - o[i]) * x[j-1]
                    self.__w[i] = w

                    error += abs(y[i] - o[i])

                errorSample += error

            errorEra = errorSample

            print('Época: {} - Erro de aproximação: {}'.format(e, errorEra))

    def __generate_weight(self):
        for i in range(self.__numOut):
            line = []
            for j in range(self.__numIn+1):
                line.append(random.uniform(-0.3, 0.3))
            self.__w.append(line)
