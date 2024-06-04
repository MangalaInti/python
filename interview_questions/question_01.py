# Find common letter between two strings:
def common_letter(str1,str2):
#Convert them to set to remove duplicates    
    s1 = set(str1)
    s2 = set(str2)
    # & in set will give common letters
    lst = s1 & s2
    print(list(lst))

common_letter('naina','reene')

# Count the frequency of words appearing in a string
str1 = 'sheena loves eating apple and mango.Her sister also loves eating mango and apple'
str2 = str1.split(' ')
d = {}
for i in str2:
    if i in d.keys():
       d[i]= d[i] +1
    else:
        d[i]= 1
print(d)    

#Convert list to a dictionary
keys = [1,2,3]
values= ['one','Two','Three']
result = dict(zip(keys,values))
print(result)

#Sort a List in Descending Order
lst = [2, 5, 6, 8, 1, 8, 9, 11]
lst.sort(reverse = True)
print(lst)


#Count item occurence
list1 = ['John','Kelly', 'Peter', 'Moses', 'Peter']
count = 0
for i in list1:
    if i == 'Peter':
     count = count+1
print(count)

#Alternate way
list1.count('Peter')

Python has a built in module called calender
import calender

How to get current date and time
from datetime import datetime

#Flatten a nested list
list1 = [[1, 2, 3],[4, 5, 6]]
new_lst = []
for i in list1:
  for j in i:
    new_lst.append(j)     
print(new_lst) 

#Find the index of Biggest number

def index_of_largest(lst):
    if not lst:
        return None  # Return None if the list is empty
    max_index = 0
    for i in range(1, len(lst)):
        if lst[i] > lst[max_index]:
           max_index = i
    return max_index

# Example usage:
numbers = [10, 5, 20, 8, 15]
largest_index = index_of_largest(numbers)
print("Index of largest number:", largest_index)
print("Largest number:", numbers[largest_index])

# Empty string
str1 = ''
if not str1:
print('This string is empty')
else:
print('This string is NOT empty')
Output:
This string is empty
Example


    


