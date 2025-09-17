# Find the sum of all even numbers in list with exception handling
def sum_even(numbers):
  sum = 0
  for number in numbers:
    if isinstance(number, (int,float)):    #Checks if it is number, handle potential typeerrors
          if number % 2 == 0:
            sum = number + sum
          else:
            print(f'warning : Ignorning non numeric value : {number}'}          
            
  return sum        

numbers =[10,30,50,66,'a']
result = sum_even(numbers)
print(result)

#Alternate method

def sum_even(numbers):
  count = 0
  for n in numbers:
    try:
      if n % 2 == 0:
        count = count + n
    except TypeError:
      #Handle cases where n is not a number (e.g string, None, etc)
      print(f"skipping non-numeric value : {n}")
   except Exception as e:
      #catches any other unexpected errors
     print(f"Unexpected error with value {n}: {e}")
 return count
numbers =[10,30,50,66,'a']
result = sum_even(numbers)
print("Sum of even numbers", result)





