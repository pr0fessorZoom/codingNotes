'''
    # Basic datastructures
    # A data structure is a a way to organize information
'''

# List - A list of things

my_list = [1,'a',True]
print(len(my_list)) # Watch large of the list

# Dict - Organizing with characteristics

my_dict = {
    "users":{
        "flash" : "good",
        "reverse" : "bad"
    }
}
print(my_dict)

# Tuple - UNmodifiable data

my_tuple = (1,'a',True)
print(my_tuple)

# Add new item in list

my_list.append("i'm new item")
print(my_list)

# Remove last item in list
my_list.pop()
print(my_list)

# Remove specific position in list
my_list.pop(0)
print(my_list)

# Remove first item with selected value
my_list.append('a')
print(my_list)
my_list.remove('a')
print(my_list)

# Look for list size

list_size = len(my_dict)
print(list_size) # All lists starts in 0, so if our list_size is 1, really is 2 -> 0-1