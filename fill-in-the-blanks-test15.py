# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

sample_1 = '''A common first thing to do in a language is display
'Hello __1__!'  In __2__ this is particularly easy; all you have to do
is type in:
__3__ "Hello __1__!"
Of course, that isn't a very useful thing to do. However, it is an
example of how to output to the user using the __3__ command, and
produces a program which does something, so it is useful in that capacity.

It may seem a bit odd to do something in a Turing complete language that
can be done even more easily with an __4__ file in a browser, but it's
a step in learning __2__ syntax, and that's really its purpose.'''

sample_2 = '''A __1__, is created with the def keyword. You specify the inputs a __1__, takes by
adding __2__, separated by commas between the parentheses. __1__s by default return __3__ if you
don't specify the value to return. __2__s can be standard data types such as string, number, dictionary,
tuple, and __4__ or can be more complicated such as objects and lambda functions.'''

sample_3 = '''When you create a __1__, certain __2__s are automatically
generated for you if you don't make them manually. These contain multiple
underscores before and after the word defining them.  When you write
a __1__, you almost always include at least the __3__ __2__, defining
variables for when __4__s of the __1__ get made.  Additionally, you generally
want to create a __5__ __2__, which will allow a string representation
of the method to be viewed by other developers.

You can also create binary operators, like __6__ and __7__, which
allow + and - to be used by __4__s of the __1__.  Similarly, __8__,
__9__, and __10__ allow __4__s of the __1__ to be compared
(with <, >, and ==).'''

user_input_request = ['__1__', '__2__', '__3__', '__4__', '__5__', '__6__', '__7__', '__8__', '__9__', '__10__']

answers_1 = ['world', 'Python', 'print', 'html']
answers_2 = ['function', 'arguments', 'None', 'lists']
answers_3 = [ 'class', 'method', '__init__', 'instance', 'repr', 'add', 'sub', 'less than', 'greater than', 'equals']

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/

sample = ""


def choose_sample(level):          # Choose sample based on difficulty level.
    if level == "easy":            # Samples are all in string form.
        sample = sample_1
    if level == "medium":
        sample = sample_2
    if level == "hard":
        sample = sample_3
    listed_sample = sample.split()      # Split sample string into a list.
    return listed_sample


def choose_answers(level):          # Choose answers based on difficulty level.
    if level == "easy":             # All answers are already in list form.
        answers = answers_1
    if level == "medium":
        answers = answers_2
    if level == "hard":
        answers = answers_3
    return answers


def choose_level():            # Select valid game difficulty level.
    level = ''
    print "Please choose a game difficluty level by typing it in"
    level = raw_input("The choices are; easy, medium or hard : " + level + " ") # Inputs string for level.
    while level not in ['easy', 'medium', 'hard']:                      # Make sure of user input format.
        print "Please input a valid answer for level"
        level = raw_input("The choices are; easy, medium or hard : " + level + " ") # Inputs string for level.
        print "you have chosen ", level
    return level                 # Returns selected level to play game function.


def user_def_attempts():     # Select valid number of user attempts.
    user_attempts = ''
    print "input integer value for number of attempts from 1 to 5, maximum # of attempts is 5"
    user_attempts = input("Choose number of attempts: " + user_attempts + " ")       # Inputs integer value.
    while user_attempts not in [1, 2, 3, 4, 5]:                             # Make sure of user input format.
        user_attempts = ''
        print "Please choose a valid integer value for number of attempts from 1 to 5, maximum is 5"
        user_attempts = input("Choose number of attempts: " + user_attempts + " ")    # Inputs integer value.
        print "you have chosen ", user_attempts
    print "you will get", user_attempts, "attempts per question", ""
    return user_attempts


def word_in_pos(word):       # Determine if user_input required to answer quiz.
    for input in user_input_request:
        if input in word:
            return input
    return 'not_user_input'


def answer_index_value(test):   # Find index value for quiz answer in listed_answers
    index_value = 0             # by comparing to the list of user_input_requests.
    for test_index in user_input_request:
        if test in test_index:
            return index_value
        else:
            index_value += 1


def check_answer(user_attempts, test, sample, listed_answers):
    """
    The check_answer function compares the answer given by the user in user_input
    with the string stored in the listed_answers list at the answer_index_value found in
    the listed_answers list. It allows the user to have a user-selcted number of attempts.
    If the answer is correct it returns the user_input to the build_quiz_answer function.
    If the number of attempts is exceeded it returns the None value and the game
    will be ended in the build_quiz_answer function.
    """
    user_input = ""                        # Define empty string for user_input.
    attempt = 0                            # Set user attemps to zero.
    while attempt < user_attempts:
        print sample
        user_input = raw_input("Type in a word to replace: " + test + " ")  # User request to answer quiz qstn.
        i = answer_index_value(test)                    # Find index location of correct answer in answers.
        if user_input == listed_answers[i]:             # Compare user_input with correct answer.
            print "you chose; ", user_input, "that is the correct answer!"
            return user_input                            # Return correct answer to build_quiz_answer function.
        else:
            print "sorry wrong answer", "try using a Capital first letter for important names"
            print "please try again"
        attempt += 1                       # Record user attemp count in counter called attempt.
        print "attempt =", attempt
    return None                            # Return None value if atttempts exceeds user_def_attempts.


def build_quiz_answer(listed_sample, replaced, user_attempts, sample, listed_answers):
    """
    The build_quiz_answer steps through the words in the listed quiz correspondong to the level selected by
    the user in the play_game function. It builds the answer in the empty string, replaced, until it detects
    that user_input is required. When user_input is required it uses the check_answer function to ask for
    the answer from the user. If the correct answer is returned it continues building the answer in replaced.
    If the correct answer is not returned it returns the string "sorry...better luck next time ".
    """
    test = ""
    for word in listed_sample:
        test = word_in_pos(word)                        # Test if sample requires user input?
        if test is 'not_user_input':                    # If not put word in empty list called replaced.
            replaced.append(word)
        else:                                      # Else request answer by user in check_answer function.
            user_answer = check_answer(user_attempts, test, sample, listed_answers)
            if user_answer is None:                 # If None is returned no correct answers were given.
                return "sorry you exceeded the number of permitted attempts","better luck next time"
            else:                                               # Replace the first instance of test
                sample = sample.replace(test, user_answer, 1)   # in sample with the correct answer.
                word = word.replace(test, user_answer)  # Replace test with answer in listed sample.
                replaced.append(word)                   # Put correct answer in empty list called replaced.
    completed_quiz_string = " ".join(replaced)        # Convert completed list of words into string.
    print "you won! Here is the completed paragraph."
    return completed_quiz_string                      # Return completed quiz string to play game function


def play_game():
    """
    The play_game function requests the user to select a difficulty level and number of atttempts
    to complete the fill-in-the-blanks quiz. It initialises a string to contain the answers and
    sends that along with the quiz and quiz answers, in list form, to the build_quiz_answer function.
    It returns the out put of the build_quiz_answer function as a string to be printed.
    """
    replaced = []
    level = choose_level()                      # Requests user to input difficulty level.
    user_attempts = user_def_attempts()         # Request user to input number of attempts.
    listed_sample = choose_sample(level)        # Returns selected quiz sample in list form.
    listed_answers = choose_answers(level)      # Returns quiz answers in list form.
    sample = " ".join(listed_sample)            # Reformat quiz sample as string for later use.
    return build_quiz_answer(listed_sample, replaced, user_attempts, sample, listed_answers)


print play_game()
