import numpy as np
import matplotlib.pyplot as plt

# Dados de exemplo para x e y
x = np.array([0, 1.1, 2.3, 3.7, 4.2, 5.9])
y = np.array([0.5, 1.4, 3.9, 6.3, 8.8, 9.7])

# Criar um gráfico de dispersão para os pontos x e y
plt.scatter(x, y, color="blue", label="Dados")

# Adicionar rótulos aos eixos e uma legenda
plt.xlabel("X (unidades)")
plt.ylabel("Y (unidades)")
plt.legend()
plt.xlim([-1, 7])
plt.ylim([-1, 11])

plt.axis(True)
plt.grid(True, which="both")

# Calcular a matriz de correlação
correlacao_pearson = np.corrcoef(x[::-1], y[::-1])[0, 1]

# Adicionar a linha da correlação de Pearson
plt.plot(x, x + (x * correlacao_pearson), color="red")
plt.text(
    -0.5, 8, f"rho = {correlacao_pearson:.3}", fontname="Arial", fontsize=18
)  # mostra o resultado da correlação no gráfico

# Mostrar o gráfico
plt.show()
