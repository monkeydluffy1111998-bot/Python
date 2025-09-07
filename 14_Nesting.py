#  _   _       _ _ ____             _    
# | \ | |_   _| | |  _ \ ___   ___ | |_  
# |  \| | | | | | | |_) / _ \ / _ \| __| 
# | |\  | |_| | | |  _ < (_) | (_) | |_  
# |_| \_|\__,_|_|_|_|_| \_\___/ \___/ \__|  

#         Created By: NullRoot

# ----------------------------------
# 🔁 Nesting Conditions in Python
# ----------------------------------

# Sample value
age = 94

# Outer condition
if age >= 18:
    # Inner condition
    if age >= 80:
        print("Cannot Drive")
    else:
        print("Can Drive")
else:
    print("Cannot Drive")
# Output: Cannot Drive