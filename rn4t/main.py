# Como a base de dados é muito extensa, tive que colocar um valor muito baixo para o NI, pois  estava causando overflow na função math do python

from perceptron import Perceptron
from database import Database

NI = 0.00000000001
NUMIN = 21
NUMOUT = 10

database = Database()
table = database.table

perceptron = Perceptron(NUMIN, NUMOUT, NI)
perceptron.learn(table, era=10000)

