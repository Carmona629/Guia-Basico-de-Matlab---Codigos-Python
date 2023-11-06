import matplotlib.pyplot as plt

# gráfico X em função de Y
x = [2, 5.5, 7, 7.8, 9]  # vetor de valores de x
y = [8, 11, 12, 12.5, 15]  # vetor de valores de y
y_error = [1, 0.5, 1, 1.3, 0.8]  # vetor de valores do erro de y
plt.subplot(2, 2, 1)
plt.errorbar(x, y, yerr=y_error, fmt="ok", elinewidth=1.3, capsize=3)
plt.xlabel("X (unidades)", fontsize=18, fontname="Arial")
plt.ylabel("Y (unidades)", fontsize=18, fontname="Arial")
plt.xlim([1, 10])
plt.ylim([6, 17])
plt.axis(True)
plt.grid(visible=True, which="both")

# gráfico de barras
x_bar = ("A", "B", "C", "D", "E")
y_bar = [98, 123, 240, 66, 12]
plt.subplot(2, 2, 2)
plt.bar(x_bar, y_bar, width=0.75)
plt.xlabel("Categoria", fontsize=18, fontname="Arial")
plt.ylabel("Contagem", fontsize=18, fontname="Arial")
plt.axis(True)
plt.grid(visible=True, which="major")


# gráfico pizza
valores = [2, 6, 8, 1]
labels = ["type 1", "type 2", "type 3", "type 4"]
plt.subplot(2, 2, 3)
plt.pie(valores, labels=labels)
plt.legend(labels, loc="upper center", bbox_to_anchor=(0.5, 0), ncol=len(labels))

plt.show()
