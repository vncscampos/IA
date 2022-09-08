from rna import RNA
import numpy as np
import math

class MLP(RNA):
    def __init__(self, qnt_in, qnt_out, qnt_h, ni):
        self.qnt_in = qnt_in
        self.qnt_out = qnt_out
        self.qnt_h = qnt_h
        self.ni = ni
        self.min = -0.3
        self.max = 0.3
        self.weight_hid = self.__random_matrix(qnt_in+1, qnt_h)
        self.weight_out = self.__random_matrix(qnt_h+1, qnt_out)
        
    def __random_matrix(self, rows: int, columns: int):
        weigth_matrix = np.random.uniform(
            low=self.min, high=self.max, size=(rows, columns))
        return weigth_matrix

    def exec(self, x_in: list):
        pass

    def training(self, x_in: list, y: list):
        x = x_in.copy()
        x.append(1)

        # obtem as saidas dos neuronios das camadas intermediarias
        H = []
        for h in range(self.qnt_h):
            u = 0

            for i in range(len(x)):
                u += x[i] * self.weight_hid[i][h]

            temp = 1/(1+ math.pow(math.e, -u))
            H.append(temp)
        
        H.append(1)

        # obtem as saidas dos neuronios das camadas de saída
        out = []
        for j in range(self.qnt_out):
            u = 0
            for h in range(len(H)):
                u += H[h] * self.weight_out[h][j]
            out.append(1/(1+ math.pow(math.e, -u)))


        # calculando do delta da camada de saída
        DO = []
        for j in range(self.qnt_out):
            DO.append(out[j] * (1-out[j]) * (y[j]-out[j]))
        
        # calculando o delta da camada intermediária
        DH = []
        for h in range(self.qnt_h):
            s = 0
            for j in range(len(out)):
                s += DO[j] * self.weight_out[h][j]
            DH.append(H[h] * (1-H[h]) * s)

        # Ajuste de peso camada intermediária
        for i in range(len(self.weight_hid)):
            for h in range(len(self.weight_hid[0])):
                self.weight_hid[i][h] += self.ni * DH[h] * x[i]

        # Ajustando peso da camada de saida
        for h in range(len(self.weight_out)):
            for j in range(len(self.weight_out[0])):
                self.weight_out[h][j] += self.ni * DO[j] * H[h]

        return out