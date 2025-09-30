import pandas as pd

# ANSI escape codes for bold text
BOLD = '\033[1m'
RESET = '\033[0m'

# 🎯 Employee dataset
data = {
    'Department': ['HR', 'HR', 'IT', 'IT', 'Finance', 'Finance'],
    'Employee':   ['A',  'B',  'C',  'D',  'E',       'F'],
    'Salary':     [40000,42000,50000,52000,60000,62000],
    'Bonus':      [2000, 2500, 3000, 3500, 4000, 4500]
}

df = pd.DataFrame(data)

print(f"{BOLD}👥 Original Employee Dataset:{RESET}\n", df)

# 🔎 Average salary per department
print(f"\n{BOLD}💰 Average Salary per Department:{RESET}\n", 
      df.groupby('Department')['Salary'].mean())

# 🔢 Employee count per department
print(f"\n{BOLD}👤 Number of Employees per Department:{RESET}\n", 
      df.groupby('Department')['Employee'].count())

# 📊 Multiple aggregations in one go
print(f"\n{BOLD}📈 Salary (mean & max) and Bonus (sum) per Department:{RESET}\n", 
      df.groupby('Department').agg({'Salary':['mean','max'], 'Bonus':'sum'}))

# 🧩 Multi-level grouping
print(f"\n{BOLD}🔗 Salary per Department & Employee:{RESET}\n", 
      df.groupby(['Department','Employee'])['Salary'].sum())

# 🧮 Salary range (max - min) within each department
print(f"\n{BOLD}📏 Salary Range (Max - Min) per Department:{RESET}\n", 
      df.groupby('Department')['Salary'].apply(lambda x: x.max() - x.min()))

# ==============================================================
# 🎓 Student Grades Dataset
grades = pd.DataFrame({
    'Student': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie'],
    'Subject': ['Math','Math','Math', 'Science', 'Science', 'Science'],
    'Score':   [85, 78, 88, 90, 76, 95]
})

print(f"\n{BOLD}📚 Student Grades Dataset:{RESET}\n", grades)

# 🎯 Average score per student
print(f"\n{BOLD}📝 Average Score per Student:{RESET}\n", 
      grades.groupby('Student')['Score'].mean())

# 🎯 Average score per subject
print(f"\n{BOLD}📊 Average Score per Subject:{RESET}\n", 
      grades.groupby('Subject')['Score'].mean())
