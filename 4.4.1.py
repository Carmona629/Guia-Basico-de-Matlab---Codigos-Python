import matplotlib.pyplot as plt

# dados para preenchimento do gráfico
categoria = ["A", "B", "C", "D"]
contagem = [0, 1, 2, 3]

# cria o gráfico de barras
plt.bar(categoria, contagem)

# Adicionar rótulos aos eixos e ao gráfico
plt.xlabel("Categoria")
plt.ylabel("Contagem")
plt.title("Gráfico de Barras")

# plota o gráfico
plt.show()
