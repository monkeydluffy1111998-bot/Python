  _   _       _ _ ____             _    
 | \ | |_   _| | |  _ \ ___   ___ | |_  
 |  \| | | | | | | |_) / _ \ / _ \| __| 
 | |\  | |_| | | |  _ < (_) | (_) | |_  
 |_| \_|\__,_|_|_|_| \_\___/ \___/ \__|  

        Created By: NillRoot




##  Python Notes 🐍

---

### **INDEX** 📘 
1. [What Is Programming?](#what-is-programming)
2. [What is Compiler?](#what-is-compiler)
3. [What is Interpreter?](#what-is-interpreter)
4. [What is Code?](#what-is-code)

---

### **What Is Programming?**

Programming is the process of giving instructions to a computer so it can perform specific tasks. A computer does not understand human language directly, so we use programming languages (like Python, Java, C, etc.) to write instructions in a structured way that the computer can understand and execute.

**In Simple Words**: Telling a computer what to do and how to do it.

---

### **What is Compiler?**

A **compiler** is a special program that translates code written in a high-level programming language (like C, C++, Java) into machine language (binary 0/1) that the computer hardware can actually understand and execute.

**Compiler =** Translates everything first, then runs.

---

### **What is Interpreter?**

An **interpreter** is a program that translates and runs your code line by line, instead of translating the whole program at once like a compiler does.

**Interpreter =** Translates and runs line by line.

---

### **What is Code?** 💻 

**Code** is a set of written instructions (using a programming language) that tells the computer what to do.

---

### ***Python Character Set***

Letters - A to Z, a to z
Digits - 0 to 9
Special Symbols - + - * /etc.
Whitesspaces - Blank Space, tab, carriage returns, newline, formfeed
other characters - Python can process all ASCII and Unicode characters as part of data or literals

---


### ***Variables***

A Variable is a container (or a box) in a memory that stores data, and you give it a name so you can use it latter.

name = NillRoot
age = 17

---

### ***Rules of Identifiers***

1.Identifiers can be combination of upparcase and lowercase letter digits or an underscore (_). so myvariable, variable_1, variable_for_print, all are valid points.

2.An Identifiers can not start with digit so while variable_1 is valid, 1variable is not valid.

3.We can't use special symbols like !,@,#,$,%, etc in our Identifiers.

4.Identifiers can be any length.

---

### ***Data Types***

Data Types tells the computer what kind of data is stored.

Interger (int) = whole number (positive, negative, or zero)
String (str) = text (inside quotes)
Floating point (float) = Decimal number (frictions)
Boolean (bool) = True or False values (used for logic)
None 
list (list) = collection of multiple values (ordered, changeable)
tuple (tuple) = similar to list, but unchangeble (immutable)
dictionary (dict) = key-value pairs (like a mini database)
set (set) = collection of unique values (no duplicates)

---

### ***Keywords***

keywords are reserved words in python.

False, True, None, if, else, elif, while, for, break, continue, def, return, import, class, try, except, finally, with, as, pass, global, nonlocal, lambda, yield, in, is, not, and, or, from, raise, del

---

### ***Types of Tokens***

# Punctuators

Punctuators are Symbols to organize sentence structure in programming.

Perentheses ()
Braces {}
Brackets []
comma ,
colon :
Semicolon ;
@ , # , -=, +=, /=, *=, //=, =. etc..

### ***Expression Execution***

# String & Numeric value can operate together with *

A,B = 2,3
Txt = "@"
print(2*Txt*3)

# String & String can operate with +

A,B = 2,3
Txt = "@"
print((A+Txt)*B)

# Numeric values can operate with all arithmetic operators.

A,B = 2, 5.0
C = 4
print(A+B*C)

# Arithmetic Expression with integer and float will result in float

A,B = 10, 50
C = A*B
print(C)

# Numeric Values can operate with all arithmetic operators.

A,B = 2,3
C = 4
print(A+B*C)

# Arithmetic Expression with integer and float will result in float

A,B = 10, 50
C = A*B
print(C)


# Result of division operator with two integer will be float

A,B = 1,2
C = A/B
print(C)

# Integer division (//) with float and int will give int display as float 

A,B = 1.5, 3
C = A/B
print(C, A/B)


# Floor gives closest integer which is lesser than or eqal to float value result of (A//B) is same as floor (A//B)

A,B = 12,5
C = A//B
print(C)

A,B = -12,5
C = A//B
print(C)

A,B = 12,-5
C = A//B
print(C)

#  Remainder is negative when denominator is negative.

A,B = -5,2
C = A%B
print(C)

A,B = 5,2
C = A%B
print(C)

A,B = 5,-2
C = A%B
print(C)

### ***Comments***

Notes in code, ignored by the computer, but useful for humans.

(#) Single Line comment 
("""This is Multiple line comment""")

---

### ***Types of Operators***

# Arithmetic operators

+,-,*,/,%,**

# Relational / Comparision OPerators

==,!=,>,<,>=,<=

# Assignment Operators

=,+=,-=,*=,/=,%=,**=

# Logical Operators 

not, and, or

---

### ***Type Conversion***

Conversion means changing the data type of a variable into another type.
1.Automatically - Python does it automatically.
2.Manually - You do it using functions.

---

### ***Inputs in Python***

Input statment is used to accept values (using keyboards) from users.

---

### ***String***

String is a data type that contain a sequence of characters.

## Basic Operations

# Concatenation

Concatenation means joining two or more strings together.
only work with string (text).

# Length of String

len(str)

# Indexing 

Indexing means accessing individual elements of a sequence (like string,list or tuple) using their position number.
index number start from 0 in python.

# Slicing

Slicing means extracting a part of a string, list, or tuple using index range.

### ***Condition Statements***

Conditional Statements allow a program to make decision and execute code based on conditions (True/False).

if...elif...else

# Nesting Conditions 

Nesting means putting one thing inside another.


### ***Conditional Statement***

