# From below list of mixed list seperate all numbers
my_list = [1, 2, 3, 'Jessa', 4, 5, 'Kelly', 'Jhon', 6]

numbers = [ n for n in my_list if isinstance(n,(int,float))]

print(numbers)
List comprehensions provide a concise way to create lists.
isinstance() method to filter elements based on their type.




