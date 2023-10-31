# print odd number of letters from string
str = "pynative" 
word = list(str) 
for i in word[0::2]:
  print(i)

#.find(), .count() these methods can used in strings & lists
s = 'linkedin'
print(s.find('n'))

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




