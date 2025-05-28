--Write python code to remove duplicate, square the elements and order in descending order
numbers = [3,2,5,2,7,3,1,8,5,4,6]

list = sorted(set(x**2 for x in numbers), reverse = True)
