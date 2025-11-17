# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.

# Examples:

# my_list = ['apple', 'banana', 'cherry']
# print(my_list[0])         # apple
# print(my_list[1:])        # ['banana', 'cherry']

# my_list.append('grape')
# print(my_list)

# my_list.pop(1)
# print(my_list)

# numbers = [3, 1, 4, 2]
# numbers.sort()
# print(numbers)

#collections are used to store miltiples items in a single variables
# list are ordered collections of items
#list are mutable, meaning you can chnage their content
# lists are crared using square brackets []
list_of_fruits =  ["apple", "banana", "cherry", "date"]
print(list_of_fruits)
print(type(list_of_fruits)) #<class 'list'>
#Accesing items in a list 
print(list_of_fruits[0]) #apple
print(list_of_fruits[1]) #banana
print(list_of_fruits[-1]) #date
print(list_of_fruits[1:3]) # banana cherry
# reversing a list
list_of_fruits.reverse()
print(list_of_fruits)  #date cherry banana apple
print(list_of_fruits [::-1]) # apple bananan cherry date
list_of_fruits.append("elderberry") # add items to the end of the list
print(list_of_fruits)
list_of_fruits.append("starfruit")
list_of_fruits.append("guava")
list_of_fruits.append("kumquats")
print(list_of_fruits)
list_of_fruits.extend(["mango","honeydrew","strawberry"])
print(list_of_fruits)
popped_item = list_of_fruits.pop()
print(popped_item)
print(list_of_fruits)
list_of_fruits.insert(1, "blueberry")
print(list_of_fruits)
list_of_fruits.remove("banana")
print(list_of_fruits)
list_of_fruits.insert(3, "pineapple")
list_of_fruits.sort()
print(list_of_fruits)
#NUMBERS
list_of_items = list(range(1, 1010101))
print(list_of_items)
print(len(list_of_items)) #1000
list_of_items.extend(range(1001,2001))
print(len(list_of_items))


#instead of creating seperate variables
#for each item we can store them in a list
#this makes our job easier
#this makes managing the complexity of our code easier
#when we need to manage multiple items
# PERFORMNACE TASK ANSWER

#sets and tuples
#sets and tuples are also part of the collections
# family in python
#sets examples
set1 = {1, 2, 3, 4, 5}
set2 = {"apples", "banana", "cherry}
print(set1)
print(set2)
print(type(set1))
set_with_duplicates = {1, 2, 3, 4, 5}
print(set_with_duplicates)
print(3 in set1)
print(6 in set1)
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ("apples", "banana", "cherry")
print(tuple1)
print(tuple2)
print(type(tuple1))
social_security_number = (123444, 444756, 879236)
# Practice Problems:
list_of_fav_foods = ["birria", "tacos", "chilaquiles", 'nopales", "albondigas de pollo"}
                     
print(list_of_fav_foods[1])
print(list_of_fav_foods[-1])

# # # Add a new item using .append().
list_of_fav_foods.append('Burger')
print(list_of_fav_foods)    
# # # Remove the first item using .pop(0).
list_of_fav_foods.pop(0)
print(list_of_fav_foods)

# # # Reverse your list using .reverse().
list_of_fav_foods.reverse()
print(list_of_fav_foods)

# # # Create a list of 3 lists (matrix), and access the middle element.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
middle_element = matrix[1][1]
print(middle_element)  # Output: 5




