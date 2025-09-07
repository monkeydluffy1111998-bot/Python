#  _   _       _ _ ____             _    
# | \ | |_   _| | |  _ \ ___   ___ | |_  
# |  \| | | | | | | |_) / _ \ / _ \| __| 
# | |\  | |_| | | |  _ < (_) | (_) | |_  
# |_| \_|\__,_|_|_|_|_| \_\___/ \___/ \__|  

#         Created By: NullRoot

# ----------------------------
# 📋 List Basics
# ----------------------------

marks = [87, 64, 33, 95, 76]

print(marks)           # Output: [87, 64, 33, 95, 76]
print(type(marks))     # Output: <class 'list'>
print(len(marks))      # Output: 5

print(marks[0])        # Output: 87
print(marks[1])        # Output: 64

# ----------------------------
# ⚙️ List Methods
# ----------------------------

# Sample list
student = ['Prabh', 'Ankit', 'Rohit', 'Sahil']
print(student)

# Append - Adds element at the end
student.append('Aman')
print(student)         # ['Prabh', 'Ankit', 'Rohit', 'Sahil', 'Aman']

# Insert - Adds element at specified position
student.insert(2, 'Ravi')
print(student)         # ['Prabh', 'Ankit', 'Ravi', 'Rohit', 'Sahil', 'Aman']

# ----------------------------
# 🔢 Sorting & Reversing (Numerical Example)
# ----------------------------

student = [2, 5, 1, 4, 3]

# Sort the list in ascending order
student.sort()
print(student)         # [1, 2, 3, 4, 5]

# Sort in descending order
student.sort(reverse=True)
print(student)         # [5, 4, 3, 2, 1]

# Reverse the current order of the list
student.reverse()
print(student)         # [1, 2, 3, 4, 5]

# Insert at index 3
student.insert(3, 5)
print(student)         # [1, 2, 3, 5, 4, 5]
