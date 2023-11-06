from numpy import zeros
from random import random

X = 10  # tamanho da dimensão x da matriz
Y = 11  # tamanho da dimensão y da matriz

M = zeros((Y, X))  # cria uma matriz M de zeros de tamanho Y por X;

# utiliza a variável “i” para percorrer valores de 1 <inicial> até Y <final>:
for i in range(1, Y):
    # utiliza a variável “j” para percorrer valores de 1 <inicial> até X <final>:
    for j in range(1, X):
        # percorre a matriz M atribuindo valores entre -5 e 5 para a cada um de seus índices (i,j):
        M[i, j] = 10 * (0.5 - random())
