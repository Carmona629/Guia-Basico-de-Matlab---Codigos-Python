import matplotlib.pyplot as plt

valores = [2, 6, 8, 1]
labels = ["type 1", "type 2", "type 3", "type 4"]

plt.pie(valores, labels=labels)
plt.legend(labels, loc="upper center", bbox_to_anchor=(0.5, 0), ncol=len(labels))
plt.show()
