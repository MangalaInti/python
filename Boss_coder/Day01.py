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
