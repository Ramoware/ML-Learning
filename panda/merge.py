import pandas as pd

# ANSI escape codes for bold text
BOLD = '\033[1m'
RESET = '\033[0m'

# 🎓 Student dataset
students = pd.DataFrame({
    'ID':   [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})
print(f"{BOLD}👥 Students Dataset:{RESET}\n", students)

# 🧮 Scores dataset
scores = pd.DataFrame({
    'ID':   [1, 2, 4],
    'Math': [85, 90, 95]
})
print(f"\n{BOLD}📘 Scores Dataset:{RESET}\n", scores)

# 🔗 INNER JOIN → only matching IDs
print(f"\n{BOLD}🔗 INNER JOIN (Only common IDs):{RESET}\n", 
      pd.merge(students, scores, on='ID', how='inner'))

# 👈 LEFT JOIN → all students, scores where available
print(f"\n{BOLD}👈 LEFT JOIN (All Students, match scores if found):{RESET}\n", 
      pd.merge(students, scores, on='ID', how='left'))

# 👉 RIGHT JOIN → all scores, students where available
print(f"\n{BOLD}👉 RIGHT JOIN (All Scores, match students if found):{RESET}\n", 
      pd.merge(students, scores, on='ID', how='right'))

# 🌍 OUTER JOIN → union of all IDs from both tables
print(f"\n{BOLD}🌍 OUTER JOIN (All IDs from both datasets):{RESET}\n", 
      pd.merge(students, scores, on='ID', how='outer'))
