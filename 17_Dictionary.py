#  _   _       _ _ ____             _    
# | \ | |_   _| | |  _ \ ___   ___ | |_  
# |  \| | | | | | | |_) / _ \ / _ \| __| 
# | |\  | |_| | | |  _ < (_) | (_) | |_  
# |_| \_|\__,_|_|_|_| \_\___/ \___/ \__|  

#         Created By: NullRoot

# Creating a Dictionary

Student = {
    "Name": "NullRoot",
    "Age": 17,
    "Courses": ["Social Enginering", "Python"],
    "Marks":  85.5,
    "Result" : True,
}
print(Student)  # Output: {'Name': 'NullRoot', 'Age': 17, 'Courses': ['Social Enginering', 'Python'], 'Marks': 85.5, 'Result': True}


# Adding/Updating Elements

Student["Grade"] = "A"  # Adding a new key-value pair
Student["Marks"] = 90.0  # Updating an existing key's value
print(Student)
# Output: {'Name': 'NullRoot', 'Age': 17, 'Courses': ['Social Enginering', 'Python'], 'Marks': 90.0, 'Result': True, 'Grade': 'A'}




### Dictionary Methods

#returns all keys
Student1 = {
    "Name": "NullRoot",
    "Age": 17,
    "Courses": ["Social Enginering", "Python"],
    "Marks":  85.5,
    "Result" : True,
}
print(Student1.keys())

#returns all values
print(Student1.values())

#returns all key-value pairs
print(Student1.items())

#returns value for specified key
print(Student1.get("Name"))  # Output: NullRoot

#insrts the specified item to the dictionary
Student1.update({"Age": 18, "Grade": "A"})
print(Student1)
# Output: {'Name': 'NullRoot', 'Age': 18, 'Courses': ['Social Enginering', 'Python'], 'Marks': 85.5, 'Result': True, 'Grade': 'A'}
