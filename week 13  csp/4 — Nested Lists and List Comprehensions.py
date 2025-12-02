list1 = [1, 2, 3]
print(list1[-1])
list2 = [4, 5, 6]
print(list2[0])
nested_list = [list1, list2]
print(nested_list[0]) #output 1,2,3
print(nested_list[1]) #output 4,5,6
print(nested_list[0][1]) #output
print(nested_list[1][1])
print(nested_list[1][0])
fruits = ["apples","bananas","pineapple","grapes"]
vegetables = ["celery","carrots","potatoes"]
meats = ["chicken","meat","beef"]
nested_lists = [fruits, vegetables, meats]
print(nested_lists[2][2])
print(nested_lists[0][2])


groceries = [["apples","bananas","pineapple","grapes"],
 ["celery","carrots","potatoes"],
 ["chicken","meat","beef"]]

for collections in groceries:
    for food in collections:
        print(food, end=" ")
    print()


num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ('*', 0, '#'))

for row in num_pad:
    for num in row:
        print(num, end=' ')
    print()

 #nested loops
# for i in range(1,101):
#     for j in range(1,101):
#         if i > 0 and j < 0:
#             for k in range(1,101):
#                 print("the number is", i, j, k)


# Objectie:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])    # 6

# List comprehension
first_col = [row[0] for row in matrix]
print(first_col)       # [1, 4, 7]





# Practice Problems:

# Build a matrix variable containing 3 lists of 3 numbers each.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Print the first list.
print(matrix[0])
# Print the second item from the third list.
print(matrix[2][1])
# Use a list comprehension to extract the last item from each sub-list.
sum_list = [row[-1] for row in matrix]
print(sum_list)
# Challenge: Create a new list containing squares of numbers from 1–10 using a comprehension.
squares = [x**2 for x in range(1,11)]
