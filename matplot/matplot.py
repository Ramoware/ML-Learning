import matplotlib.pyplot as plt
import pandas as pd

#Titanic dataset
df = pd.read_csv("D:/Ml/excel/train.csv")

#Bar plot of Survived counts
survived_counts = df["Survived"].value_counts()

plt.bar(survived_counts.index,survived_counts.values,color = ["red","green"])
plt.xticks([0,1],["Not Survived","Survived"])
plt.xlabel("Status")
plt.ylabel("Number of Passengers")
plt.title("Titanic Survival Count(Matplotlib)")
plt.show()