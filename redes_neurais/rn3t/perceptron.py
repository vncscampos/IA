import random
from typing import List
import math

class Perceptron:
    def __init__(self, numIn:int, numOut:int, ni:float):
        self.__numIn = numIn
        self.__numOut = numOut
        self.__ni = ni
        self.__w = []
        self.__generate_weight()

    def learn(self, x:List[int], y:List[int], era:int):
        sample = len(y[0])

        for e in range(era):
            errorEra = 0
            errorSample = 0 #erro amostra

            for s in range(sample):
                line_x = x[s]

                u = []
                o = []
                
                error = 0

                for i in range(self.__numOut):
                    calc = 0

                    line_w = self.__w[i]
                    cur_y = y[i][s]

                    for j in range(self.__numIn+1):
                        calc += line_w[j] * line_x[j]

                    u.append(calc)

                    # Calcula teta da função sigmoidal
                    func = 1/(1+math.pow(math.e, -u[i]))
                    o.append(func)

                    # Atualiza pesos
                    for j in range(len(line_w)):
                        line_w[j] += self.__ni * (cur_y - o[i]) * line_x[j]
                    self.__w[i] = line_w

                    error += abs(cur_y - o[i])

                errorSample += error

            errorEra = errorSample

            print('Época: {} - Erro de aproximação: {}'.format(e, errorEra))

    def __generate_weight(self):
        for i in range(self.__numOut):
            line = []
            for j in range(self.__numIn+1):
                line.append(random.uniform(-0.3, 0.3))
            self.__w.append(line)
