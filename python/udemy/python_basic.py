
import datetime

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

#----------------------------------------------------------------------------------------------------------------------------------

# Main method in order to call only a specific function, not the whole script
def main():

    # Example 1 - 
    # inputExample()

    # Example 2 - 
    variableType()


if __name__ == '__main__':
    main()
    