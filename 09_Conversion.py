#  _   _       _ _ ____             _    
# | \ | |_   _| | |  _ \ ___   ___ | |_  
# |  \| | | | | | | | |_) / _ \ / _ \| __| 
# | |\  | |_| | | |  _ < (_) | (_) | |_  
# |_| \_|\__,_|_|_|_| \_\___/ \___/ \__|  

#         Created By: NullRoot

# ----------------------------
# 🔄 Type Conversion in Python
# ----------------------------

# ✅ 1. Automatic Type Conversion (Implicit)

# a = 10       # int
# b = 3.5      # float
# c = a + b    # int + float → float
# print(c)     # Output: 13.5

# Python automatically converts 'a' to float for the operation.

# ✅ 2. Manual Type Conversion (Explicit)

a = "23"               # string
print(type(a))         # Output: <class 'str'>

# Convert string to integer
b = int(a)
print(b + 7)           # Output: 30
print(type(b))         # Output: <class 'int'>

