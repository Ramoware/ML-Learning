import numpy as np
import matplotlib.pyplot as plt

# Mean = 50, Standard Deviation = 5
data = np.random.normal(50,5,1000)

plt.hist(data, bins = 20, edgecolor = 'black')
plt.title("Normal Distribution(mean = 50, sd = 5)")
plt.show()