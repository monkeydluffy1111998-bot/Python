#  _   _       _ _ ____             _    
# | \ | |_   _| | |  _ \ ___   ___ | |_  
# |  \| | | | | | |_) / _ \ / _ \| __| 
# | |\  | |_| | | |  _ < (_) | (_) | |_  
# |_| \_|\__,_|_|_|_| \_\___/ \___/ \__|  

#         Created By: NullRoot

# ----------------------------
# ✂️ Slicing in Python
# ----------------------------

# ✅ Slicing a String

name = "NullRoot"

# From index 1 to 4 (5 is excluded)
print(name[1:5])       # Output: "ullR"


# ✅ Slicing a List

name2 = ["NullRoot", "Ghost", "Zero"]

# From index 1 to 2 (3 is excluded)
print(name2[1:3])      # Output: ['Ghost', 'Zero']


# ✅ Slicing from Start or to End

name3 = "NullRoot"

print(name3[:9])       # Output: 'NullRoot' (index 9 doesn't exist but no error)
print(name3[0:])       # Output: 'NullRoot' (from 0 to end)


# ✅ Negative Index Slicing

name4 = "NullRoot"

# Slices from start to -2 (excluding last 2 characters)
print(name4[:-2])      # Output: 'NullRo'
