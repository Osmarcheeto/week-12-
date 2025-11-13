# Objective:
# Students will learn how to compare values using Python’s comparison operators and interpret Boolean results.

# Topics Covered:
# ==, !=, >, <, >=, <=

# Key Notes:

# Comparison operators compare two values and return either True or False.

# Remember: = is assignment, while == is comparison.

a = 3
b = 4

print(a == b)   # False
print(a != b)   # True
print(a > b)    # False
print(a < b)    # True
print(a >= b)   # False
print(a <= b)   # True


#predict the output of the following comparisons:
10 > 5
7 == 2 * 3 + 1
8 != 8
4 <= 2 + 2

# Write 3 examples that result in True and 3 that result in False.

# Create a simple grade-checking condition:

# practice problem :
# where a student must check if their score is greater than or equal to 60 to pass a test.# The password must be at least 8 characters long and contain at least one digit.password = "mypassword1"
c = 7
e = 8
print(c == e)   # False
print(c != e)   # True
print(c > e)    # False
print(c < e)    # True
print(c >= e)   # False
print(c <= e)   # True

# Create a simple grade-checking condition:
score = 75  # Change this value to test different scores
if score >= 60:
    print("Pass")
else:
    print("Fail")

# practice problem :
# where a student must check if their score is greater than or equal to 60 to pass a test.# The password must be at least 8 characters long and contain at least one digit.password = "mypassword1"
password = "mypassword1"  # Update with a different password if needed
if len(password) >= 8 and any(char.isdigit() for char in password):
    print("Password is valid")
else:
    print("Password is invalid")
