# Create string variable

# Example 1: Creating string variables
s = "Welcome"
s = 'Welcome'
s = str("Welcome")

# empty string

name = str()
name = ""
name = ''

# Example 2:
# Mutable-Can change the value of variable,
# Immutable-Can't change the value of variable
# Strings are immutable

str1 = "Welcome"
print(id(str1))  # 2181433806000

str1 = str1 + "to python!"
print(str1)
print(id(str1))  # 2181435694720
# If the value is changed after updating then it is immutable...

# Example 3: How to use + and * with string
str= "Welcome"
print(str+" Python")
print(str*3)    # 3 times

# Example 4: Slicing []
# Starting index start with = 0
# Ending index  start with= 1
str="Welcome"
print(str[1:3])
print(str[:6])
print(str[2:])

print(str[1:-1])        # (-1) means remove last character

# Example 5: ord() and chr() //ASCII number

print(ord("A"))       # Find ASCii number

print(chr(65))      # Ascii number to character

# Example 6 : max() min()   len()

print(max("abc"))
print(min("abc"))
print(len("welcome"))

# Example 6: in, not in operator
s="welcome"
# in Operator
print("come" in s)  # True
print("lome" in s)  # False

# not in operator
print("come" not in s)  # False
print("lome" not in s)  # True

print("Example 08---------")
# Example 8: String comparison
print("tim" =="him")        # False
print("tim" != "him")       # True
print("tim" > "time")        # False
print("tim" < "time")       # True
print("right" >= "left")    # True
print("yellow" <= "fellow")     # False
print("abc" > "")       # True

# Example 9: Testing string  (True/False)
print("Example 9:")

s="Welcome to python"
print(s.isalnum())      # False
print("Welcome".isalpha())# True
print("2012".isdigit()) #True
print("first Number".isidentifier())    # False
print(s.islower())  # False
print("WELCOME".isupper())      # True
print(" ".isspace())        # True

# Example 10: Searching for Substring
print("Example 10:")
s= "welcome to python"
print(s.endswith("thon"))   # True
print(s.startswith("good")) # False
print(s.find("come"))   # 3
print(s.find("become")) # -1    -Not found
print(s.rfind("pyth"))      # 11
print(s.count("t"))     # 2

# Example 11: Converting string
print("Example 11:")
s = "String in PYTHON"
s1 = s.capitalize()
print(s1)       # String in python

s2 = s.title()
print(s2)       # String In Python

s3 = s.lower()
print(s3)       # string in python

s4 = s.upper()
print(s4)       # STRING IN PYTHON

s5 = s.swapcase()
print(s5)       # sTRING IN python

s6 = s.replace("in", "on")
print(s6)       # Strong on PYTHON

# Example 12: How to reverse string
print("Example 12:")
# Method_1
s= "welcome"
rev_str = ""
for i in s:
    rev_str = i + rev_str
print(rev_str)

# Method_2:
sa = "welcome"
rev_str1=sa[::-1]       # S[0:7:-1]
print(rev_str1)




