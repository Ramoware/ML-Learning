import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 randome values between 0 and 10
data = np.random.uniform(0,10,1000)

plt.hist(data, bins = 20, edgecolor = 'black')
plt.title("Uniform Distribution(0,10)")
plt.show()