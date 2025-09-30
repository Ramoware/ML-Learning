import seaborn as sns
import matplotlib.pyplot as plt

#Data
x = [1,2,3,4,5]
y = [1,4,9,16,25]

#Plot
sns.lineplot(x=x, y=y, marker="o")

#Labels and title
plt.title("Basic Line Plot (Seaborn)")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()