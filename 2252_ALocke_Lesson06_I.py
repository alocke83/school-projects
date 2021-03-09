# FILE:2252_ALocke_Lesson06_I.py
# NAME:Game of 50 States
# AUTHOR(s): Adam Locke
# DATE:month/day/year  04/25/2020
# PURPOSE: makes you good at sending letters

#i did not know that 'plaintextlist.com' was a thing but it is super handy

#import statements
import random
'import time'

#global variables
correct = []
miss = 0
hit = 0
answer = 'null'

#states dictionary
states = {'Alabama': 'AL',
'Alaska': 'AK', 
'Arizona': 'AZ', 
'Arkansas': 'AR', 
'California':'CA', 
'Colorado': 'CO',
'Connecticut': 'CT',
'Delaware': 'DE',
'Florida': 'FL',
'Georgia': 'GA',
'Hawaii': 'HI',
'Idaho': 'ID',
'Illinois':'IL',
'Indiana':'IN',
'Iowa':'IA',
'Kansas':'KS',
'Kentucky':'KY',
'Louisiana':'LA',
'Maine':'ME',
'Maryland':'MD',
'Massachusetts':'MA',
'Michigan':'MI',
'Minnesota':'MN',
'Mississippi':'MS',
'Missouri':'MO',
'Montana':'MT',
'Nebraska':'NE',
'Nevada':'NV',
'New Hampshire':'NH',
'New Jersey':'NJ',
'New Mexico':'NM',
'New York':'NY',
'North Carolina':'NC',
'North Dakota':'ND',
'Ohio':'OH',
'Oklahoma':'OK',
'Oregon':'OR',
'Pennsylvania':'PA',
'Rhode Island':'RI',
'South Carolina':'SC',
'South Dakota':'SD',
'Tennessee':'TN',
'Texas':'TX',
'Utah':'UT',
'Vermont':'VT',
'Virginia':'VA',
'Washington':'WA',
'West Virginia':'WV',
'Wisconsin':'WI',
'Wyoming':'WY'}



#function to choose a state at random and place them in a list of 10 states
def random_list():
    global correct
    correct = []
    counter = 0
    for items in states:
        if counter < 10:
            pick = random.choice(list(states.keys()))
            correct.append(pick)
            counter += 1
    'print(correct)'

#function to ask the question
def question():
    global correct
    if len(correct) > 0:
        print('What state does', states[correct[0]], 'stand for?')
        timer()
    else:
        print('The game has finished!')
        input('Hit any key for your results.')
        result()

#function to start and stop the timer, if it elapses the score is counted as a miss    
def timer():
    global miss
    global answer
    global hit
    '''timer = time.time()'''
    answer = input('The state is: ')
    answer.capitalize()  
    while answer != correct[0]:
        print('The correct answer is ', correct[0],'.', end='')
        miss += 1
        correct.pop(0)
        break
    else:
        print('CORRECT!')
        hit += 1
        correct.pop(0)
    input('Hit enter to start the next question.')
    question()

#function to reveal the result and request more tries or quit
def result():
    print('\n\nYou scored ', hit, ' correct answers and ', miss, ' incorrect answers.')
    if hit == 10:
        print('That\'s the perfect score!  You\'re ready to send letters anywhere.')
    elif hit > 7:
        print('That\'s an excellent score, try again to hit the perfect score.')
    elif hit>5:
        print('you\'re a fair hand at matching states against postal abbreviations.')
    else:
        print('Fortunately you can play as many times as you like and this score is not being stored anywhere.')
    print('\n\nPlay again?')
    playing = input('enter y to play again, n to quit.')
    while playing != 'y' and playing != 'n':
        playing = input('enter y to play again, n to quit.')
    if playing == 'y':
        rules()
    else:
        ('Thank you very much for playing, see you next time!')
        

#function to introduce the game rules and begin the game
def rules():
    global miss
    global hit
    miss = 0
    hit = 0
    print('Welcome to game of 50 States\nIn this game you will be presented with the abbreviations of 10 randomly chosen\nUS states.\n\nYou must provide the correct name of the state.')
    input('\n let\'s begin!  Press enter to start the first question.')
    random_list()
    question()


#debugging tools
'print(len(states))'
'random_list()'
'test_list = [6]'
'print(len(test_list))'
'question()'
'rules()'

#script for a timed response that I gave up on because I need to get this turned in
'''timer = time.time()'''
    #some script about putting in the answer
'''   while timer > time.time()-4.0:
        print('You took too long!  The correct answer is ', correct[0],'.', end='')
        miss += 1
        correct.pop(0)
        break        
    else:'''

#mainline logic
rules()
