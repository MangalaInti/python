
#Calculate the sum of all numbers from 1 to a given number
# Get the number from the user
num = int(input("Enter a number:"))

# Initialize variables
sum = 0
i = 1

# Calculate the sum using a while loop
while i <= num:
    sum += i
    i += 1

# Print the result
print("The sum of all numbers from 1 to", num, "is", sum)


#Write a program to display only those numbers from a list that satisfy the following conditions

#The number must be divisible by five
#If the number is greater than 150, then skip it and move to the next number
#If the number is greater than 500, then stop the loop


numbers = [12, 75, 150, 180, 145, 525, 50]

for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    elif item % 5 == 0:
        print(item)



#Count the total number of digits in a number
number = 75869
number_str = str(number)
count_digits = len(number_str)

print("The total number of digits in", number, "is", count_digits)

#Count the total number of digits in a number using WHILE loop

number = 6789
count_digits = 0

while number > 0:
    count_digits += 1
    number //= 10

print("The total number of digits is", count_digits)

#Find the facorial
n=5
for i in range(1,n+1):
    factorial = i*i
print(factorial)   

#Write a pgm to display all number 1 to 100
i =1
while i <=100:
    print(i, end = ' ') 
    i = i+1

#Using for loop
for i in range(1,101):
    print(i, end = ' ')
