
import datetime

'''
Example 1 - Asking values through console with function input - https://www.geeksforgeeks.org/taking-input-in-python/
'''

# Asking string as input
name = input("What is your name? ")
print("Hello! "+name+". Nice to see that you are learning Python")

# Asking age as string, then convert it to integer. 
yearBirth = input("Which is your year of birth? I want calculate your age ")
year = int(yearBirth)
now = datetime.datetime.now()

# Calculate age and display a simple message
if year > now.year:
    print("Wow! you seems to come from the future!")
else:
    age = now.year - year
    print("Your age is: "+str(age))

# ---------------------------------------------------------------------------------------------------------------------------------
