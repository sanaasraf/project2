# Test simulation program by Sana Asraf

"""
This program allows the user to attempt a multiple choice quiz. At first, it prompts the user to enter their details, after which
it directs them to the main quiz which has been configured with the help of an imported Class. Making use of the 'tabulate' module,
which had to be installed first, a final report, presented as a table, containing the candidates personal information alongside their
grade and status has also been programmed. The module 'datetime' has also been utilized within the table in order to specify the date of its issue.
The program also offers a choice to the user, and allows them to back out of the test if they feel unprepared.
How each module and class works is discussed at the end of the script.
"""


# Importing the module 'tabulate'
from tabulate import *

# Heading
print("***********\nEXAMINATION\n***********\n")

# Fetching input from the users regarding their personal details, before the test
candidate_name = input("Enter your full name: ")   # name
candidate_number = input("Enter your roll number: ")   # roll number
candidate_guardian = input("Enter the name of your guardian: ")   # name of their guardian
candidate_centre = input("Enter the name of your test centre: ")  # name of their test centre


# defining a function to create a make-shift admit card for the user for reference

def details(name, number, guardian, centre):  # takes in four parameters

#  making use of the tabulate module, creating a list of all the details (row and column wise)
    detailslist = [["Name", candidate_name], ["Roll Number", candidate_number], ["Candidate's Guardian", candidate_guardian], ["Test centre", candidate_centre]]
    print(tabulate(detailslist))  # the tabulate function assembles the details together and formulates the table

# the output of the above function will depend on the 4 inputs given by the user when the program is run. Therefore, the function is called with these 4 inputs as its parameters.
details(candidate_name, candidate_number, candidate_guardian, candidate_centre)

"""
scroll down to view the function that asks for the users confirmation to write the quiz
"""

def messagebox():  # function for a message box that will be displayed at the end of the program to ask th user if the test went well
    # the tkinter module allows the user to interact in a GUI
    import tkinter
    from tkinter import messagebox  # to display message box
    screen = messagebox.askyesno("Response Card", "Thank you for writing! We hope your test went well?")  # question, to which, the message box from tkinter will either display yes or no
    screen.geometry("200x200")  # size of screen
    screen.mainloop()  # to keep the screen visible

# importing the class I've created containing the attributes and parameters for questions/answers for the quiz.
from questionsclass import Questions

# Creating a list of questions and options for answers.
# Endless number of questions can be of input into this list. But for the sake of this program, there are five simple ones.

questionbank = ["How many letters are present in the English alphabet?\n(a)18\n(b)24\n(c)26\n(d)30\nYour answer: ",
                "How many planets exist in our Solar System?\n(a)3\n(b)4\n(c)7\n(d)8\nYour answer: ",
                "Which colour isn't present on the UAE flag?\n(a)Pink\n(b)Green\n(c)White\n(d)Black\nYour answer: ",
                "Are plants considered living things?\n(a)Yes\n(b)No\n(c)Both a and b\n(d)Neither a nor b\nYour answer: ",
                "Which country has the largest number of people?\n(a)USA\n(b)China\n(c)Spain\n(d)Russia\nYour answer: "

                ]

# creating a list that calls the imported class and assigns its attributes (question and answer), to each question from the question bank list and to the answer the user is expected to input
q_and_a = [Questions(questionbank[0], "c"),   # using indexing to call the question. starts from 0, up to 4.
           Questions(questionbank[1], "d"),
           Questions(questionbank[2], "a"),
           Questions(questionbank[3], "a"),
           Questions(questionbank[4], "b")
           ]

# defining a function for the execution of the quiz
def test(q_and_a):  # the parameter of this function depends upon the contents of the q_and_a list which is in turn facilitated by the 'Questions' class


    score = 0   # initial score is 0
    print("\n***\nAnswer with a, b, c, or d. You only get one shot at answering, think and choose wisely!\n***\n")  # header statement
    for q in q_and_a:  # loop to keep all five questions running
        answer = input(q.question)  # allows the question from the question bank list to be presented as an input, below which the user can write their answer


        if answer == q.user_answer:
            score = score + 1  # increase score for every time the user inputs the correct answer, ie, the input is equal to 'answer' from 'q_and_a'
            # allotting scores and grades based on final score
            if score == 5:
                grade = "A"
                status = "Passed"

            elif score == 4:
                grade = "B"
                status = "Passed"

            elif score == 3:
                grade = "C"
                status = "Passed"

            else:
                grade = "F"
                status = "Failed"

# final statement which takes in all the defining variables
    print("\nYou have managed to secure " + str(score) + "/" + str( len(questionbank)) + " questions correct. \nYou've recieved a/an " + grade + " grade which considers you as " + status + ".")


# asking if the user requires a report
    report_again = "Y"  # to initiate the input
    while report_again == "Y" or report_again == "y": # creating a conditional loop, so that in case the input does not match the requirements, the program does not run into an error
        asking = input("Would you like a report of your performance? type 'yes' or 'no': ")   # input
        if asking == 'yes':

            import datetime   # datetime module allows us to bring forth the system's date and time and incorporate it into our program.
            # in this case, it's helpful as it helps us figure out exactly when the report was issued
            thedate = datetime.date.today()   # function to help us retrieve the system's date


    # using tabulate again, to create the report
            table = [["Name: ", candidate_name],  # name
                     ["Roll Number: ", candidate_number],  # roll number
                     ["Name of Guardian: ", candidate_guardian],  # name of guardian
                     ["Test Centre: ", candidate_centre],  # test centre
                     ["Test Score: ", score],   # final score
                     ["Test Grade: ", grade],   # final grade
                     ["Test date: ", thedate]      # date of issue

                     ]
            print(tabulate(table, headers='secondrow', tablefmt='grid'))  # tabulating the table, alongside formatting it to enhance its appearance.
            messagebox()



        elif asking == 'no':
            messagebox()    # in the case that they don't want a report


        else:
            report_again = input("Invalid input. Press Y/y to try again. Or press any other key to exit the program.")  # loops again or exits, according to input


def begin():  # a function to finalize if the user wishes to go through with writing the quiz or not
    confirmation = input("Are you ready to attempt the quiz? Enter 'yes' or 'no': ")  # input for confirmation
    if confirmation == "yes":
        test(q_and_a)  # runs test


    elif confirmation == "no":
        print("Thank you. Do come back when you feel more prepared.")  # exits

    else:
        print("Enter a valid input. Try again.")
        begin()  # runs the function again

begin()   # calling the function















