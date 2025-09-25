# print odd number of letters from string
str = "pynative" 
word = list(str) 
for i in word[0::2]:
  print(i)

#.find(), .count() these methods can used in strings & lists
find() method is used to find the substring in given string, if the substring is found it returns the lowest index of the substring

s = 'linkedin'
x = s.find('n')
print(x)

count() method is used count the number of times the item/element occured in given string
x = s.count('n')
print(x)

# Palidrome
def palidrome(num):
 num1 = str(num)
 num2 = num1[::-1]
 if num1 == num2:
   return num
 else:
  print('number is not palidrome') 
res = palidrome(121)
print(res) 

# combine 2 lists
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
list1.extend(list2)
print(list1)

# Difference between end and sep, notice difference
print('Name', 'Is', 'James', end = '**')
print('Name', 'Is', 'James', sep = '**')




