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

