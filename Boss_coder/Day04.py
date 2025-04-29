#Function to accept list of numbers, find the sum of all positive numbers
def func(lst):
    result = sum(num for num in lst if num >0)
    return result
d = func([1,0,-1,-2,1,2,3])
print(d)

#Implement a function that returns the factorial of a given number using recursion

def factorial(num):
    if num ==0 or num ==1:
        return 1
    return num * factorial(num-1)
print(factorial(3))

#Create a function to find the square of element in a list
#Method 1
def square(lst):
   result = [num * num for num in lst]
   return result
print(square([2,3,4]))

#Method 2
def square(lst):
    return list(map(lambda x: x * x, lst))
print(square([2, 3, 4]))  # Output: [4, 9, 16]

lambda x: x * x defines an anonymous function that squares a number.
map(...) applies this function to each element in the list.
list(...) converts the result from a map object to a list.

#Create a function that takes a list of strings and returns  the list sorted alphabetically

def sort_strings(string_list):
    return sorted(string_list)

print(sort_strings(['hen', 'cow', 'man', 'elephant', 'ant']))

#Write a function that takes two lists and returns their intersection(common) elements
def intersection(lst1, lst2):
    return list(set(lst1).intersection(set(lst2)))

print(intersection([1, 2, 3, 4, 5], [3, 4, 5, 6]))

#Check if the given year is leap year or not
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0):
        return True
    else:
        return False
print(is_leap_year(2020))   




