# Sabrina Turney
# September 24, 2018
# Maximum of Two Values
# This program takes two inputs from a user in functions, and displays the
# larger number as a return.

#function definitions

#return type: none
#parameters: none
#Purpose: This function displays the intro to the user.
#It does not require any parameters to be sent to it
#so the parameters are empty ().
#First Function!
def PrintIntro():
    print("Welcome to my program!")

#return type: none
#parameters: 1 string value(user's name)
#Purpose: This function displays a greeting to the user using their name.
def PrintGreeting(name): #name is a formal parameter. An actual parameter must
    #be passed to this function when it is called
    #The + signs concatenate which means are added right next to the text, so
    #we add the space before or after the " where needed
    print("Hello "+ name + ", I hope you enjoy using my program!\n")
    print("I'll need two number values. Then I'll display the greater one!")
    #This doesn't produce a type error because the print statement matches
    #the type of the variable, which is a string value as well.

#return type: integers
#parameters: 2, the 2 numbers we'll be comparing.
#purpose: We get the two inputs we'll be using to find the larger number.
def getNumbers(number1, number2):
    number1 = input("Please enter your first number!")
    number2 = input("And now please enter your second number!")
    return number1, number2

#return type: string
#parameters: 2, the 2 numbers we had the user input in our getNumbers module
#purpose: Now we find the max value of the two, and display it to the user.
def findMax(number1, number2):
    biggerNumber = max(number1, number2)
    return biggerNumber

def main():
    #declare all the variables in the main function
    name = input("Please enter your name: ") #ask for user's name for intro
    number1 = 0.0 #float number inputs, user can choose any number.
    number2 = 0.0 #these are the numbers the user will input.
    biggerNumber = 0 #Where we will put the biggest number variable.

    #Then we just call all of our functions!
    PrintIntro()
    #Say hello
    PrintGreeting(name)
    #Say hello with your name
    number1, number2 = getNumbers(number1, number2)
    #Get two number inputs (float, negative, whole, etc.)
    biggerNumber = findMax(number1, number2)
    #use python's built in method of finding max values
    print("The biggest number between " +number1+ " and  " +number2+ " is \n" +biggerNumber+ "!")
    #This print line is a little wordy, but I like seeing the variables here.
    #I also print the biggest number on a new line to be clear.

main()
#Last but not least is calling the main function for the user.
