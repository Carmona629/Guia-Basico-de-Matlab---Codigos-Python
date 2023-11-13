import numpy as np
import matplotlib.pyplot as plt

# ---Linear fit---
x = [0, 1.1, 2.3, 3.7, 4.2, 5.9]  # conjunto de dados x
y = [0.5, 1.4, 3.9, 6.3, 8.8, 9.7]  # conjunto de dados y
plt.subplot(1, 2, 1)
plt.scatter(x, y, color="black", linewidths=7)
plt.xlabel("X (unidades)", fontsize=18, fontname="Arial")
plt.ylabel("Y (unidades)", fontsize=18, fontname="Arial")
plt.xlim([-1, 7])
plt.ylim([-1, 11])


plt.show()
