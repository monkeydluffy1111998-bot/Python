#  _   _       _ _ ____             _    
# | \ | |_   _| | |  _ \ ___   ___ | |_  
# |  \| | | | | | | |_) / _ \ / _ \| __| 
# | |\  | |_| | | |  _ < (_) | (_) | |_  
# |_| \_|\__,_|_|_|_| \_\___/ \___/ \__|  

#         Created By: NullRoot

# ----------------------------
# 🔤 Strings in Python
# ----------------------------

# ✅ Different ways to create strings

str1 = "Hlo NullRoot"
str2 = 'Hlo NullRoot'
str3 = """Hlo NullRoot"""              # Multi-line or triple quote string

# ✅ Including quotes inside a string

str4 = "Hlo NullRoot 'Aka Roronoa Zoro'"    # Single quotes inside double quotes
str5 = 'Hlo NullRoot "Aka Roronoa Zoro"'    # Double quotes inside single quotes

# ✅ Escape Characters

str6 = "Null \nRoot"       # \n adds a new line
print(str6)
# Output:
# Null 
# Root

# ----------------------------
# ➕ String Concatenation & Length
# ----------------------------

first_name = "Null"
len1 = len(first_name)
print(len1)                # Output: 4

second_name = "Root"
len2 = len(second_name)
print(len2)                # Output: 4

full_name = first_name + second_name
print(full_name)           # Output: NullRoot
print(len(full_name))      # Output: 8

# ----------------------------
# 🛠️ String Functions
# ----------------------------

str = "I Am NullRoot"

# 1. Check if string ends with a specific word
print(str.endswith("Root"))           # Output: True

# 2. Capitalize the first letter
print(str.capitalize())               # Output: 'I am nullroot'

# 3. Replace part of the string
print(str.replace("NullRoot", "Roronoa Zoro"))   # Output: 'I Am Roronoa Zoro'

# 4. Find index of first occurrence of character
print(str.find("R"))                  # Output: 8

# 5. Count how many times a character appears
print(str.count("I"))                 # Output: 1

