#Given a list of names, concatenate them into single string separated by spaces.
# Sample list of names
names = ["Alice", "Bob", "Charlie", "Diana"]

# Concatenate using join()
result = " ".join(names)

# Output the result
print("Concatenated string:", result)

#Write program that convert given number of minutes into hours and minutes
# Input: total number of minutes
total_minutes = int(input("Enter the number of minutes: "))

# Conversion
hours = total_minutes // 60
minutes = total_minutes % 60

# Output
print(f"{total_minutes} minutes is equal to {hours} hour(s) and {minutes} minute(s).")
