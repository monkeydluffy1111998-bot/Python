#  _   _       _ _ ____             _    
# | \ | |_   _| | |  _ \ ___   ___ | |_  
# |  \| | | | | | | |_) / _ \ / _ \| __| 
# | |\  | |_| | | |  _ < (_) | (_) | |_  
# |_| \_|\__,_|_|_|_| \_\___/ \___/ \__|  

#         Created By: NullRoot

# ----------------------------
# 🧠 Logical Operators in Python
# ----------------------------

# NOT Operator - negates the condition
a = 50
b = 30

print(not (a > b))      # False, because a > b is True, not True → False
print(not False)        # True
print(not True)         # False

# AND Operator - True if both conditions are True
val1 = True
val2 = True

print("And Operator:", val1 and val2)   # Output: True

# OR Operator - True if at least one condition is True
print("Or Operator:", (a == b) or (a > b))  # Output: True (a > b is True)
print("Or Operator:", (a == b) or (a < b))  # Output: False (both conditions are False)
print("Or Operator:", (a == b) or (a != b)) # Output: True (a != b is True)
print("Or Operator:", (a < b) or (a > b))   # Output: True (a > b is True)
print("Or Operator:", (a < b) or (a < 100)) # Output: True (a < 100 is True)
print("Or Operator:", (a > b) or (a < 100)) # Output: True (both conditions are True)
print("Or Operator:", (a < b) or (a > 100)) # Output: False (both conditions are False)
print("Or Operator:", (a > b) or (a > 100)) # Output: True (a > b is True)
