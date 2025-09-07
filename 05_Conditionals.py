#  _   _       _ _ ____             _    
# | \ | |_   _| | |  _ \ ___   ___ | |_  
# |  \| | | | | | | |_) / _ \ / _ \| __| 
# | |\  | |_| | | |  _ < (_) | (_) | |_  
# |_| \_|\__,_|_|_|_| \_\___/ \___/ \__|  

#         Created By: NullRoot

light = input("Light Color: ").capitalize()  # Capitalize to handle case-insensitive input

if light == "Red":
    print("Stop")

elif light == "Yellow":
    print("Look")

elif light == "Green":
    print("Go")

else:
    print("Light is Broken")
