# Find missing number in the sequence
def missing_num_summation(a):

 sum1 = 0
 n =a[-1] 
 total = n*(n+1)//2
 sum1 = sum(a)
 print(total - sum1)
a = [1,2,4,5,6,7]
missing_num_summation(a)

#Find the letter which occured only once
str1 = 'netsetosnet'
d= {}

for i in str1:
  if i in d.keys():
    d[i] = d[i] +1
  else:
    d[i] = 1 
for k,v in d.items():
  if v == 1:
    print(k,v)
    break
# Remove duplicates using mutiple ways

arr = [1,2,3,4,3,6,2]

# Using Set method
arr1 = list(set(arr))
print(arr1)

#Using for loop
arr1 = []
for i in arr:
  if i not in arr1:
    arr1.append(i)
  else:
    pass 
print(arr1)

#Using Lambda Filter
my_list = [1, 2, 2, 3, 4, 4, 5]

# Use filter and lambda to remove duplicates
filtered_list = list(filter(lambda x: my_list.count(x) == 1, my_list))

print(filtered_list)


# Write a  python program to find largest element in a list

#Method I

numbers = [1,20,90,45,60,100]
print(max(numbers))

# Using Loop method

def max_num(numbers):
    largest = numbers[0]
    for n in numbers:
        if n > largest:
            largest = n
    return largest       
num = max_num(numbers)
print(num)

