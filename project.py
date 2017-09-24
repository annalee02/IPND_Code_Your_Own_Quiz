introduction = '''Please select game difficulty by typing it in!
Possible choices include easy, medium, and hard.'''
print introduction
options = ['easy', 'medium', 'hard']
user_input = raw_input() # input easy or medium or hard or etc

# Check if the option is easy or medium or hard
while user_input not in options:
    print "Invalid"
    user_input = raw_input("Enter a valid option. If you want to finish the program, write 'quit' and Enter\n >")
    if user_input == 'quit':
        print "End of the program bye!"
        raw_input()
        break # End of quiz

unknown_number = ['x', 'y', 'z', 't']# blank name


# Questions
easy_description = '''A. 1+1 = _x_
B. 2+2 = _y_
C. 3+3 = _z_
D. 4+4 = _t_'''

medium_description = '''A. 3*4 = _x_
B. 15*3 = _y_
C. 45*7 = _z_
D. 36*9 = _t_'''

hard_description = '''A. 852/12 = _x_
B. 456/8 = _y_
C. 62%7 = _z_
D. 374%13 = _t_'''

# answers
easy_answers = [2,4,6,8]
medium_answers = [12,45,315, 324]
hard_answers = [71,57,6,10]

def check_replacement(n, unknown_number):# To check if there is a replacement
    for pos in unknown_number:
        if pos in n:
            return pos # Means there is a replacement and return what it is
    return None # Means there is no replacement


def marker(user_input, answers, index):# For marking
    if str(answers[index]) != user_input:
        print "Not correct!"
        print
        return -1
    print "Correct!"
    print
    return 0

# Behaviour: If the answer is wrong, it provides 3 times tryes
# Args: variables used in play_game function below
def rechallenge(user_input, answers, index, replacement, s, replaced):
    i = 0
    max_try = 3
    while i < max_try:
        print "You have " + str(3-i) + " trys left"
        print
        print " ".join(replaced)
        user_input = raw_input("What should be substituted in for " + replacement + "?")
        if marker(user_input, answers, index) == 0:
            s = s.replace("_"+replacement+"_", user_input)
            replaced.append(s)
            return # If a user writes the correct answer, it adds the user's input and gets out of this function.
        i += 1
    replaced.append(str(answers[index]))
    return # If a user used up 3 times tryes, it adds the answer and get out of the function.


def play_game(ml_string, unknown_number, answers):# Return: a replaced sentence
    draft = ml_string.split()
    index = 0
    replaced = []
    for s in draft:
        replacement = check_replacement(s, unknown_number)
        if replacement == None: # if it is not x,y,z,t
            replaced.append(s)
        else:# replace x,y,z,t with what a user input
            user_input = raw_input("What should be substituted in for " + replacement + "? \n")
            if marker(user_input, answers, index) == 0:# If a user's answer is correct
                s = s.replace("_"+replacement+"_", user_input)
                replaced.append(s)
            else: # If the answer is incorrect
                rechallenge(user_input, answers, index, replacement, s, replaced) # retry 3 times
            print " ".join(replaced) # Join and print the current "replaced"
            index += 1
    return " ".join(replaced) # The final "replaced"


def execution(user_input):# What to show when you choose a level of difficulty
    print "You've chosen "+str(user_input)+"!"
    print
    print "You will get 3 guesses per problem \n"
    # Assign questions and answers to the chosen level
    description_list = {'easy': easy_description, 'medium': medium_description, 'hard': hard_description}
    answers_list = {'easy': easy_answers, 'medium': medium_answers, 'hard': hard_answers}
    description = description_list[user_input]
    answers = answers_list[user_input]
    print description
    return play_game(description, unknown_number, answers)

if user_input in options:# If the user choose a valid option, execute the quiz
    execution(user_input)
    print
    print "End of the program bye!"
    raw_input()# End of quiz
