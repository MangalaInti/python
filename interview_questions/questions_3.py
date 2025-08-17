--Write python code to remove duplicate, square the elements and order in descending order
numbers = [3,2,5,2,7,3,1,8,5,4,6]

list = sorted(set(x**2 for x in numbers), reverse = True)

--Write a program to accept a string from the user and display characters that are present at an even index number.
For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.
str = 'pynative'
size = len(str)
for i in range(0,size -1, 2):
    print(str[i])
--Alternate Way

x = list(str)
for i in x[0::2]:
    print(i)
