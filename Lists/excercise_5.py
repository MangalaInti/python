# From below list of mixed list seperate all numbers
my_list = [1, 2, 3, 'Jessa', 4, 5, 'Kelly', 'Jhon', 6]

numbers = [ n for n in my_list if isinstance(n,(int,float))]

print(numbers)
List comprehensions provide a concise way to create lists.
isinstance() method to filter elements based on their type.

 #concatenate two lists index wise

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

list3 = [ i+j for i,j in zip(list1,list2)]
print(list3)

# combine two lists in as expected o/p
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
#Expected o/p
list3 = [i +j for i in list1 for j in list2]
print(list3)  

     




