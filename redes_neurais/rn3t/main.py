from perceptron import Perceptron

NI = 0.3
NUMIN = 2
NUMOUT = 1

# # AND
# x = [[1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
# y = [[0, 0, 0, 1]]
# perceptron = Perceptron(NUMIN, NUMOUT, NI)
# perceptron.learn(x, y, 10000)

# # # # XOR
x = [[1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
y = [[0, 1, 1, 0]]
perceptron = Perceptron(NUMIN, NUMOUT, NI)
perceptron.learn(x, y, 10000)

# # # OR
# x = [[1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
# y = [[0, 1, 1, 1]]
# perceptron = Perceptron(NUMIN, NUMOUT, NI)
# perceptron.learn(x, y, 10000)

# # # ROBO
# x = [[1, 0, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1], [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 1]]
# y = [[1, 0, 1, 0, 1, 1, 1, 1], [1, 1, 0, 1, 0, 0, 0, 0]]
# perceptron = Perceptron(3, 2, NI)
# perceptron.learn(x, y, 10000)
