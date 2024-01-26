
############################ LISTS ############################

# Creating a list
my_list = [1, 2, 3, 'hello', ['nested', 'list']]

# Accessing elements
print(my_list[0])          # Output: 1
print(my_list[4][0])       # Output: nested

# Modifying elements
my_list[1] = 'world'

# Adding elements
my_list.append(4)
my_list.insert(2, 'new')

# Removing elements
removed_item = my_list.pop(3)
my_list.remove('world')

# List operations
len(my_list)
sorted_list = sorted(my_list)
reversed_list = list(reversed(my_list))

# List comprehension
squared_numbers = [x**2 for x in range(5)]

############################ DICTIONARIES ############################

# Creating a dictionary
my_dict = {'key1': 'value1', 'key2': 2, 'key3': [1, 2, 3]}

# Accessing values
print(my_dict['key1'])      # Output: value1
print(my_dict.get('key2'))  # Output: 2

# Modifying values
my_dict['key1'] = 'new_value'

# Adding new key-value pairs
my_dict['key4'] = 'value4'

# Removing key-value pairs
removed_value = my_dict.pop('key3')

# Dictionary operations
keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()

# Nested dictionaries
nested_dict = {'outer': {'inner': 'nested_value'}}

############################ NESTING ############################

# Lists in a dictionary
person = {'name': 'John', 'ages': [25, 30, 35]}

# Dictionaries in a list
students = [
    {'name': 'Alice', 'age': 22},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 21}
]

# Lists in a list (2D list)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing nested elements
print(person['ages'][0])         # Output: 25
print(students[1]['age'])        # Output: 25
print(matrix[2][1])              # Output: 8

# Modifying nested elements
person['ages'][0] = 26
students[0]['name'] = 'Alicia'
matrix[1][2] = 10


