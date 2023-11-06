import matplotlib.pyplot as plt
import numpy as np

f = 20  # frequência do sinal (Hz)
fs = 1000  # frequência de amostragem (Hz)
w = f * 2 * np.pi

ti = 0  # tempo inicial
tf = 1  # tempo final

t = np.arange(ti, tf, (1 / fs))  # usando NumPy para criar um array de tempo

sinal = []
for i in range(len(t)):
    A = np.exp((-1) * (((t[i] - 0.5) / 0.1) * ((t[i] - 0.5) / 0.1)))
    sinal.append(A * np.cos(w * t[i]))

# Plotando o sinal
plt.plot(t, sinal)
plt.xlabel("Tempo")
plt.ylabel("Amplitude")
plt.title("Sinal Discretizado no Tempo")
plt.show()  # plota o gráfico
