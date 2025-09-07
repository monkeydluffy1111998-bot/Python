#  _   _       _ _ ____             _    
# | \ | |_   _| | |  _ \ ___   ___ | |_  
# |  \| | | | | | | |_) / _ \ / _ \| __| 
# | |\  | |_| | | |  _ < (_) | (_) | |_  
# |_| \_|\__,_|_|_|_| \_\___/ \___/ \__|  

#         Created By: NullRoot

# String & Numeric values can operate together with *

# Example: multiplying a string with integers repeats the string
A, B = 2, 3
Txt = "@"
print(2 * Txt * 3)  # Output: '@@@@@@'

# String & String can operate with +

# Uncomment below to see how string concatenation and multiplication works
# print((str(A) + Txt) * B)  # Output: '2@2@2@'

# Numeric values can operate with all arithmetic operators
A, B = 2, 5.0
C = 4
print(A + B * C)  # Output: 22.0 (5.0 * 4 + 2)

# Result of division operator with two integers will be float
A, B = 1, 2
C = A / B
print(C)  # Output: 0.5

# Integer division (//) with float and int gives floor division result
A, B = 1.5, 3
C = A // B
print(C, A / B)  # Output: 0.0 0.5

# Modulo operation (remainder) with negative denominator
A, B = 5, -2
C = A % B
print(C)  # Output: -1
