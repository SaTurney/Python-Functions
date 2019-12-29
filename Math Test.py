# Sabrina Turney
# Program Name: Math Test
# This program asks a series of addition questions to the user
# after getting their name. After the short test is over,
# the program returns the total number of questions correct, along
# with the average number correct. Lots of functions!

import random
#Imported from Python's standard library, allows random num generation.

def main():
    #Declare local variables
    counter = 0
    #Used in our repetition structure, starts at 0
    studentName = "NO NAME"
    #Will change to user's input
    averageRight = 0.0
    right = 0.0
    #averageRight and right will be floats because calculations
    #are done to find the average, which isn't always whole.
    number1 = 0
    number2 = 0
    #These numbers change as the program runs to get random numbers.
    answer = 0.0

    studentName = inputNames(studentName) #Get user name
    #Repetition structure begins here to loop program!
    while counter < 10: #When counter reaches 10, the program ends.
        number1, number2 = getNumbers(number1, number2) #Get numbers here
        answer = getAnswer(number1, number2, answer) #Get user answer here
        right = checkAnswer(number1, number2, answer, right) #Get number right
        counter = counter + 1 #Add one to the counter for each question asked.

    #Call our other functions outside the loop- Calculation to see the
    #average number of questions correct, and displaying that info to
    #the user to finish the program.
    averageRight = results(right, averageRight)
    displayInfo(right, averageRight, studentName)

#This function just gets the user's name as an input and returns it
#to the main function. Don't forget to return the variable values!
def inputNames(studentName):
    studentName = input("Enter Student Name: ")
    return studentName

#This function uses the random function from Python's standard library,
#which allows the program to always pick two random numbers between 1 and
#499. These numbers are returned again in variable form to main to be used again
def getNumbers(number1, number2):
    number1 = random.randrange(1, 500)
    number2 = random.randrange(1, 500)
    return number1, number2

#This function asks all the hard questions. You'll see this set of print
#statements ten times for the number of questions, as well as the next function,
#which will also print either correct or incorrect ten times.
def getAnswer(number1, number2, answer):
    print("What is the answer to the following equation?")
    print(number1)
    print("+")
    print(number2)
    answer = int(input("What is the sum? "))
    return answer

#This function just checks if your math adds up! If you're smart (or using
#a calculator), you'll see correct more often than not. This is also a
#If Then structure for all answers.
#Remember to return you variable values, you need them to finish the program.
def checkAnswer(number1, number2, answer, right):
    if answer == (number1 + number2):
        print("Correct!")
        right = right + 1
    else:
        print("Incorrect.")
    return right

#Here's our calculation function. We take the number right by the user,
#then divide it by the number of questions asked (10, remember the counter?)
#Then we return that variable for the end of the program.
def results(right, averageRight):
    averageRight = right/10
    return averageRight

#Last but not least, this module will display the final scores for the user.
#It prints nice statements listing the student's name, then the number of
#questions correct, and lastly, the average number of questions correct.
def displayInfo(right, averageRight, studentName):
    print("Information for student:", studentName)
    print("The number right:", right)
    print("The average right is:", averageRight)
    return

#We call main() for the user.
main()
