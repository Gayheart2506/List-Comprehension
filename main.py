name = "Gayheart"
new_list = [letter.upper() for letter in name]
print(new_list)

l_name = "jessica"
new_last = [names.capitalize() for names in l_name ]
print(new_last)

numbers = [1, 2, 3, 4, 5]
multiple = [num*2 for num in numbers]
print(multiple)

fruits = ["mango", "apple", "oranges", "Guava", "lemon", "Groundnuts"]
f_list = [x for x in fruits if "a" in x]
print(f_list)