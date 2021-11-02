
import datetime
import re

def inputExample():
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

    # Calculate age and display a simple message (only in years, no taking in account months)
    if year > now.year:
        print("Wow! you seems to come from the future!")
    else:
        age = now.year - year
        print("Your age is: "+str(age))

# ---------------------------------------------------------------------------------------------------------------------------------

def variableType():
    '''
    Example 2 - 
        Variables types in Python - Printing the type of variable
        with type function
    '''
    
    # Using type to get type variable and str to convert
    # and print a message
    myName = "Diana Rodriguez Martinez"
    varType = type(myName).__name__
    # Using f-strings formats
    print(f"Variable called {myName} is a type of {str(varType)}")
    
    myAge = 32
    varType = type(myAge).__name__
    # Using f-strings formats
    print(f"Variable called {myAge} is a type of {str(varType)}")

    #Math operations with that input
    print(f"Let's calculate how old you will be in 2050")
    yearsToSum = 2050 - datetime.datetime.now().year
    yearsToHave = yearsToSum + myAge
    print(f"We are {yearsToSum} years from 2050, so you will have {str(yearsToHave)}") 

#----------------------------------------------------------------------------------------------------------------------------------

def stringManipulation():
    """
    Example 3 - 
        A litle bit of examples where we use some of strings manipulations
    """
    stringEx = "IAmLearningHowToProgramingPythonLanguage"
    print(f"The lenght of the string {stringEx} is {str(len(stringEx))} characters")

    print(f"All letters to upper: {stringEx.upper()}")

    print(f"All letters to lower: {stringEx.lower()}")

    spaces = " ".join(stringEx)
    print(f"Add spaces between letters: {spaces}")

    # Adding a regular expression, looking for the upper letter
    # to insert a white space
    spacesUpper = re.sub('([A-Z])', r' \1', stringEx)
    print(f"Adding spaces after each upper letter: {spacesUpper}")

    # Find if substring is in the original string
    subStr = "PythonLanguage"
    if subStr in stringEx:
        print(f"Substring {subStr} is in the string {stringEx}")
    
    subStr = "The dog is black"
    if subStr in stringEx:
        print(f"Substring {subStr} is in the string {stringEx}")
    else:
        print(f"Substring {subStr} is NOT in the string {stringEx}")
    
#----------------------------------------------------------------------------------------------------------------------------------

# Main method in order to call only a specific function, not the whole script
def main():

    # Example 1 - 
    # inputExample()

    # Example 2 - 
    #variableType()

    # Example 3 -
    stringManipulation()


if __name__ == '__main__':
    main()
    