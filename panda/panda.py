import pandas as pd

# ANSI escape code for bold text
BOLD = '\033[1m'
RESET = '\033[0m'

# 🚀 Load the dataset
df = pd.read_csv('D:/ML/excel/train.csv')

 # 👀 Preview the first 5 rows of the dataset
print(f"{BOLD}📋 First 5 rows of the dataset:{RESET}\n", df.head(5))

# 🔢 Display the shape of the DataFrame (rows, columns)
print(f"\n{BOLD}📐 Shape of the dataset (rows, columns):{RESET}", df.shape)

# 🧬 Show data types of each column
print(f"\n{BOLD}🔍 Data types of each column:{RESET}\n", df.dtypes)

# 📊 Generate descriptive statistics for numerical columns
print(f"\n{BOLD}📈 Summary statistics:{RESET}\n", df.describe())

# 🧮 Calculate and print the mean of the 'Age' column
print(f"\n{BOLD}📌 Mean of 'Age' column:{RESET}", df['Age'].mean())

# 🕳️ Total number of missing values in the dataset
print(f"\n{BOLD}❓ Total missing values in the dataset:{RESET}", df.isnull().sum().sum())

# 📊 Frequency of unique rows (may be large)
print(f"\n{BOLD}📦 Value counts of entire rows (may be large):{RESET}\n", df.value_counts())

# 🔎 Check for missing values specifically in 'Age'
print(f"\n{BOLD}❓ Null values in 'Age' column (before filling):{RESET}\n", df["Age"].isnull())

# 🛠️ Fill missing values in 'Age' with the column's mean
df.fillna({'Age': df['Age'].mean()}, inplace=True)

# ✅ Verify if missing values in 'Age' are filled
print(f"\n{BOLD}✅ Null values in 'Age' column (after filling):{RESET}\n", df["Age"].isnull())

# 🎯 Unique values in the 'Age' column after filling
print(f"\n{BOLD}🧾 Unique values in 'Age' column (after filling):{RESET}\n", df["Age"].unique())

# 🛠️ Fill missing values in 'Embarked' with 'Unknown'
df.fillna({'Embarked': 'Unknown'}, inplace=True)

# ✅ Check if 'Embarked' still has missing values
print(f"\n{BOLD}✅ Null values in 'Embarked' column (after filling):{RESET}\n", df['Embarked'].isnull())

# 📍 Unique values in 'Embarked' column after filling
print(f"\n{BOLD}🧭 Unique values in 'Embarked' column:{RESET}\n", df['Embarked'].unique())