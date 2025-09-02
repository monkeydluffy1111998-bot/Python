# String

str1 = "Hlo NullRoot"
str2 = 'Hlo NullRoot'
str3 = """Hlo NullRoot"""

str4 = "Hlo NullRoot 'Aka Roronoa Zoro'"
str5 = 'Hlo NullRoot "Aka Roronoa Zoro"'

str6 = "Null \nRoot"
print(str6)

# Concatenation 

first_name = "Null"
len1 = len(first_name)
print(len1)

second_name = "Root"
len2 = len(second_name)
print(len2)

full_name = first_name + second_name
print(full_name)    
print(len(full_name))

### String Functions

str = "I Am NullRoot"
print(str.endswith("Root"))
print(str.capitalize())
print(str.replace("NullRoot", "Roronoa Zoro"))
print(str.find("R"))
print(str.count("I"))