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








