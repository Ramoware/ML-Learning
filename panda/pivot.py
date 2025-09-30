import pandas as pd

# ANSI escape codes for bold text
BOLD = '\033[1m'
RESET = '\033[0m'

# ==============================================================
# 🏪 Sales Dataset
sales = pd.DataFrame({
    'Region':  ['North', 'South', 'East', 'West', 'North', 'South'],
    'Product': ['A','A','B','B','A','B'],
    'Sales':   [100, 150, 200, 250, 300, 350],
    'Profit':  [10, 20, 30, 40, 50, 60]
})

print(f"{BOLD}🛒 Sales Dataset:{RESET}\n", sales)

# 1️⃣ Pivot: Sales by Region × Product
print(f"\n{BOLD}📊 Sales by Region × Product:{RESET}\n", 
      pd.pivot_table(sales, values='Sales', index='Region', columns='Product'))

# 2️⃣ Pivot: Total Sales per Region
print(f"\n{BOLD}💰 Total Sales per Region:{RESET}\n", 
      pd.pivot_table(sales, values='Sales', index='Region', aggfunc='sum'))

# 3️⃣ Pivot: Average Sales & Profit per Region
print(f"\n{BOLD}📈 Average Sales & Profit per Region:{RESET}\n", 
      pd.pivot_table(sales, values=['Sales', 'Profit'], index='Region', aggfunc='mean'))

# 4️⃣ Pivot: Sales grouped by Region + Product
print(f"\n{BOLD}🔗 Sales per Region & Product:{RESET}\n", 
      pd.pivot_table(sales, values='Sales', index=['Region','Product'], aggfunc='sum'))

# 5️⃣ Pivot with fill_value (replace NaN with 0)
print(f"\n{BOLD}🧩 Pivot Table with Fill Value (0 for missing):{RESET}\n", 
      pd.pivot_table(sales, values='Sales', index='Region', columns='Product', fill_value=0))

# ==============================================================
# 🎓 Student Info + Grades Dataset
student_info = pd.DataFrame({
    'Student': ['Alice', 'Bob', 'Charlie'],
    'Grades':  ['A', 'O', 'A']
})

grades = pd.DataFrame({
    'Student': ['Alice', 'Bob', 'Charlie'],
    'Marks':   [90, 95, 85]
})

print(f"\n{BOLD}👩‍🎓 Student Info Dataset:{RESET}\n", student_info)
print(f"\n{BOLD}📝 Marks Dataset:{RESET}\n", grades)

# Merge student info with grades
print(f"\n{BOLD}🔗 Merge Student Info + Marks:{RESET}\n", 
      pd.merge(grades, student_info, on='Student'))

# ==============================================================
# 🏫 Detailed Grades Dataset
grades = pd.DataFrame({
    'Student': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie'],
    'Subject': ['Math','Math','Math', 'Science', 'Science', 'Science'],
    'Score':   [85, 78, 88, 90, 76, 95],
    'Grade':   ['A', 'B', 'C', 'A', 'B', 'C']
})

print(f"\n{BOLD}📚 Detailed Grades Dataset:{RESET}\n", grades)

# Average score per student
print(f"\n{BOLD}🧮 Average Score per Student:{RESET}\n", 
      grades.groupby('Student')['Score'].mean())

# Average score per subject
print(f"\n{BOLD}📊 Average Score per Subject:{RESET}\n", 
      grades.groupby('Subject')['Score'].mean())

# Merge grades with student_info
print(f"\n{BOLD}🔗 Merge Grades with Student Info:{RESET}\n", 
      pd.merge(grades, student_info, on='Student'))

# Pivot: Average Score by Subject × Student
print(f"\n{BOLD}🎯 Pivot: Average Score by Subject × Student:{RESET}\n", 
      pd.pivot_table(grades, values='Score', index='Subject', columns='Student', aggfunc='mean'))