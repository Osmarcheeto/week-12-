# # Objective:
# # Students will understand how to create, modify, and access elements in Python lists.

# # Topics Covered:
# # Creating lists, indexing, slicing, appending, popping, sorting, reversing.

# # Examples:

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


# # Practice Problems:

# # Create a list with 5 of your favorite foods.

# # Print the second and last item.

# # Add a new item using .append().

# Remove the first item using .pop(0).

# Reverse your list using .reverse().

# Create a list of 3 lists (matrix), and access the middle element.
