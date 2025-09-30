import numpy as np
import matplotlib.pyplot as plt

# 1000 experiments of flipping a coin 10 times, probability of heads = 0.5
data = np.random.binomial(n=10, p=0.5, size=1000)

plt.hist(data, bins=20, edgecolor='black')
plt.title("Binomial Distribution (n=10, p=0.5)")
plt.show()