#Check if number is palidrome
def palindrome(num):
    num_str = str(num)
    if num_str == num_str[::-1]:
        return True
    else:
        return False

# Example usage
number = 121
if palindrome(number):
    print(f"{number} is a palindrome")
else:
    print(f"{number} is not a palindrome")


#Create a program that takes a sentence as input and counts the number of words in it.
 
# Get input from user
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Count the number of words
word_count = len(words)

# Print the result
print(f"The sentence contains {word_count} word(s).")

#Given a list of integers, find the sum of all positive numbers

# Define the list of integers
numbers = [3, -1, 7, -4, 2, -6, 8]

# Calculate the sum of positive numbers
positive_sum = sum(num for num in numbers if num > 0)

# Print the result
print(f"The sum of all positive numbers is: {positive_sum}")

# Given list of numbers, find minimum and maximum values

#Method 1 using loop
lst = [2, 4, 70, 70, 56, 3]

# Initialize min and max with the first element of the list
min_num = max_num = lst[0]

for num in lst:
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num

print("Minimum number:", min_num)
print("Maximum number:", max_num)

#Method 2 using loop
print(min(lst))
print(max(lst))

