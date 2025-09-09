#  _   _       _ _ ____             _    
# | \ | |_   _| | |  _ \ ___   ___ | |_  
# |  \| | | | | | | |_) / _ \ / _ \| __| 
# | |\  | |_| | | |  _ < (_) | (_) | |_  
# |_| \_|\__,_|_|_|_| \_\___/ \___/ \__|  

#         Created By: NullRoot

collection = {1, 2, 2, 2, "hello", "world", "hello"}  # Duplicates will be removed
print(collection)  # Output: {1, 2, 'hello', 'world'}
print(type(collection))  # Output: <class 'set'>

students = set()
students.add(1)
students.add(2)
students.add(2)
students.add(3)
students.add(4)
students.add("NullRoot")
students.add((1,2,3))
students.remove(1)
#students.clear()
students.pop()
print(len(students))
print(students) 


set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))
print(set1.intersection(set2))


