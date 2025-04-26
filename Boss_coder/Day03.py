# write program to accept list of integers, find all even numbers and store them in new list
even = [n for n in range(1, 20) if n % 2 == 0]
print(even)
#Given list strings, print the strings start with letter 'a'
lst =['apple','grapes','ant','baby','arrow']

res = [word for word in lst if word.lower().startswith('a')]
print(res)  

#implement a pgm that prints the multiplication table of given number

# Get number from user
num = int(input("Enter a number: "))

# Print multiplication table from 1 to 10
print(f"Multiplication table for {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

#iCalculate the sum of digits of given number

# Get number from user
num = int(input("Enter a number: "))
total = 0

# Loop through each digit
for digit in str(num):
    total = total+ int(digit)

print("Sum of digits:", total)







    
