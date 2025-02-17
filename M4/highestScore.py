# File: highestScore.py
# 
# Purpose: To determine which student had the highest
#          quiz score based upon the user's input.  The
#          highest score and that student's name are
#          then printed.
#
# Programmer: Aidan Underwood


# prompt the user to enter the number of students, 
# then read it in
numOfStudents = int(input("Enter the number of students: "))

# prompt the user to enter a student name, then
# read it in.  Then prompt the user to enter the
# quiz score, then read it in
highestScoreStudent = input("Enter student name: ")
highestScore = int(input("Enter student score between 0 and 10: "))

# using a for loop, prompt for the remaining student
# names and their quiz scores, then read them in.
# During this process compare highest score seen so far
# with current student score that was just read in
for i in range(numOfStudents - 1):

    # prompt the user to enter a student name, then
    # read it in.  Then prompt the user to enter the
    # quiz score, then read it in
    student = input("Enter student name: ")
    score = int(input("Enter student score between 0 and 10: "))
    
    # is current student score that was just read in
    # higher than the current high score?  If so, make
    # this student's score the highest
    if score > highestScore:
        highestScoreStudent = student
        highestScore = score
# end for loop


# print out who had the highest score and
# what their score was
print("\nHighest grade belongs to",highestScoreStudent,". Score was",highestScore)

# print message to end program
print("\nThis program was written by Aidan Underwood" + "\nEnd of program.")