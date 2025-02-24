# File: testGrades.py
# 
# Purpose: Based upon five test scores entered by the
#          user their letter grade is determined and
#          printed.  The average of these five test
#          scores is also printed.
#
# Programmer: Aidan Underwood

def main():
    # prompt the user to enter the five test scores,
    # then read them in
    score1 = float(input("Enter score 1: "))
    score2 = float(input("Enter score 2: "))
    score3 = float(input("Enter score 3: "))
    score4 = float(input("Enter score 4: "))
    score5 = float(input("Enter score 5: "))
    
    # call function calcAverage() to calculate the
    # average of the test scores
    average = calcAverage(score1, score2, score3, score4, score5)
    
    # print out each test score with its letter grade
    # equivalent as well as the average.  Use the 
    # function determineGrade() to obtain the 
    # letter grade
    print('\n\t\tnumeric\t\tletter')
    print('score\t\tgrade\t\tgrade')
    print('-----\t\t------\t\t------')
    print("score 1:\t", score1, "\t\t", determineGrade(score1))
    print("score 2:\t", score2, "\t\t", determineGrade(score2))
    print("score 3:\t", score3, "\t\t", determineGrade(score3))
    print("score 4:\t", score4, "\t\t", determineGrade(score4))
    print("score 5:\t", score5, "\t\t", determineGrade(score5))
    
    # print out the average of the five test scores
    # and the average letter grade via the function
    # determineGrade()
    print("\nAverage: \t", format(average, ',.2f'), "\t\t", determineGrade(average))
    
    # call function goodBye() to end program  
    goodBye()  
# end function main

def goodBye():
    print("\nThis program was written by Aidan Underwood" + "\nEnd of program.")
# end function goodBye

def determineGrade(score):
    # determine the letter grade based on score
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
# end function determineGrade

def calcAverage(score1, score2, score3, score4, score5):
    # calculate the average of the five test scores
    return (score1 + score2 + score3 + score4 + score5) / 5
# end function calcAverage


# call/invoke the function main()
main()
