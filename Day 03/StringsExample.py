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

print(str[1:-1])

# Example 5: