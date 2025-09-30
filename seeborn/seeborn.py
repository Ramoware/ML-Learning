import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("D:/ML/excel/train.csv")

#Histogram of Age
sns.histplot(df["Age"].dropna(),bins=20,kde=True,color="skyblue")
plt.title("Age Distribution  of Titanic Passengers (Seaborn)")
plt.show()

#Boxplot of Age by Sex
sns.boxplot(x="Sex",y="Age")
plt.title("Boxplot of Age by Gender (Seaborn)")
plt.show()