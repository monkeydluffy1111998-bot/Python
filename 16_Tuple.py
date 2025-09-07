#  _   _       _ _ ____             _    
# | \ | |_   _| | |  _ \ ___   ___ | |_  
# |  \| | | | | | | |_) / _ \ / _ \| __| 
# | |\  | |_| | | |  _ < (_) | (_) | |_  
# |_| \_|\__,_|_|_|_| \_\___/ \___/ \__|  

#         Created By: NullRoot

# Creating a tuple
tup = (1, 5, 3, 4, 1)

# Single element tuple (comma is important!)
single_element = (42,)
not_a_tuple = (42)  # This is just an integer

# Checking the type

print(type(tup))  # Output: <class 'tuple'>

# Accessing Tuple Elements (Indexing)

print(tup[0])  # Output: 1
print(tup[2])  # Output: 3



## Tuple Methods
#returns index of first occurrence

print(tup.index(3))  # Output: 2


#counts total occurrences tup.count(1) is 2
print(tup.count(1))  # Output: 2

# Tuple Slicing

tup = (10, 20, 30, 40, 50)

print(tup[1:4])   # Output: (20, 30, 40)
print(tup[:3])    # Output: (10, 20, 30)
print(tup[-2:])   # Output: (40, 50)
