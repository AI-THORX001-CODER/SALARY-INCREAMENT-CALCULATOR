import numpy as np

# Input user IDs
ids = input("Enter user IDs  ").split(',')

# Input posts (job roles)
posts = input("Enter posts : ").split(',')

# Input salaries
data = input("Enter salaries : ")
salaries = np.array(data.split(','), dtype=float)

# Increment %
inc = float(input("Enter increment %: "))

# Calculation
new_salary = salaries * (1 + inc/100)

# Output
print("\n--- Result ---")
for i in range(len(ids)):
    print(f"ID: {ids[i]} | Post: {posts[i]} | Old: {salaries[i]} | New: {new_salary[i]}")

