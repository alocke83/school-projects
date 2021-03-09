# FILE:2252_ALocke_Final.py
# NAME:Quiz for Real Nerds
# AUTHOR(s): Adam Locke
# DATE:month/day/year  05/3/2020
# PURPOSE: weeds the scrubs out of the tolkien fandom and leaves the ones who know the First Age thoroughly


'''I seriously considered adding a timer to each of the questions and so I found a pretty good concept for one on
stackoverflow that takes the value of current time since epoch, adds 10, and then loops the time until the current
time is equal to 10 seconds ago plus 10, which i thought was pretty clever.  On the other hand, I'm asking some
hardcore questions and I already penalize you for getting even one question wrong.  So I just wanted to go on the
record saying I Could have put a response time limit on it but I elected not to as a kindness.'''


'''---------------------data elements-----------------'''
#global variables
question_total= 0
hits = 0
misses = 0
current_question= ''
asked = ['null']
playing = True



#import statements
import csv
import random



'''---------------------functions---------------------'''
#a function to let the player choose how many questions will be asked, with a maximum possible of 20, graduating the degree of scrubdom success exonerates your from
def difficulty():
    global questions_total
    global elrohir
    print('Enter the number of questions you will answer\nThe more questions you elect to try, the more honor you will earn.\nYou can choose a maximum of', len(elrohir), 'questions and a minimum of 5 questions.\nIf you miss even one question you will fail the assessment, but the fewer questions you choose, the less impressive the result.\n')
    choice = int(input())
    while choice < 5 or choice > len(elrohir) or type(choice) == str:
        print('you must choose a number of questions between 5 and', len(elrohir), '\n')
        choice = int(input())
    questions_total = choice
    if questions_total == 5:
        print('Humble?  A noble trait but not a very impressive one.  Only 5 questions will be asked.')
    elif questions_total > 5 and questions_total <10:
        print('A modest beginning, you will answer questions for the lowest possible ranking category of Watcher of Films.')
    elif questions_total >9 and questions_total <15:
        print('A respectable choice, your success will set you among the Reader of Books.')
    elif questions_total >14 and questions_total <20:
        print('An impressive display of knowledge, if you succeed.  You will be marked among the Keepers of Lore.')
    elif questions_total >= 20:
        print('So you choose to attempt 20 or more questions?  You are either very foolish, or else you are among The Wise.')
    elif questions_total == len(elrohir):
        print('Hubris!  So, you will now attempt to answer all of the questions in the keeping of Master Elrond?  So be it!')
    choose_question()
    

#a function to select at random a quesiton from the list of questions and confirm that it has not been asked before, if the list of questions is expended, end the game
def choose_question():
    global asked
    global elrohir
    global current_question
    current_question = random.choice(elrohir)
    picking = 0
    while picking == 0:
        #print(asked)
        if current_question in asked:
            current_question = random.choice(elrohir)
        else:
            asked.append(current_question)
            picking += 1
            question()                
            

#a function to present the question with the order of answers randomized, take the response into a variable and compare it to the global variable into which the correct answer is loaded, then tally either the hit or miss global variables, kicking them out of the test if they failed
def question():
    global elrohir #the list of questions, derived from
    global elrond  #the dictionary of questions and answers
    global hits
    global misses
    global current_question
    correct=''
    wrong1=''
    wrong2=''
    wrong3=''
    for items in elrond:
        if items == current_question:
            alist = elrond.get(current_question)
            #print(alist)
            correct= alist[0]
            wrong1= alist[1]
            wrong2= alist[2]
            wrong3= alist[3]
            #print(current_question)
            #print(correct)
    a_pick=[]
    a_pick.append(correct)
    a_pick.append(wrong1)
    a_pick.append(wrong2)
    a_pick.append(wrong3)
    #print(a_pick)
    random.shuffle(a_pick)
    #print(a_pick)
    print(current_question,'\n1.',a_pick[0],'\n2.',a_pick[1],'\n3.',a_pick[2],'\n4.',a_pick[3],'\n')
    answer = input()
    try:
        answer = int(answer)
    except ValueError:
        print('You must enter a choice using the numbers 1 through 4, words may not be entered.')
        answer = int(input())            
    while answer != 1 and answer != 2 and answer != 3 and answer != 4:
        print('You must enter a choice using the numbers 1 through 4.')
        answer = int(input())
    answer = answer-1
    answer = a_pick[answer]
    print('You chose',answer)
    if answer != correct:
        print('Fool of a Took!  The answer was', correct)
        #print('You are undone by your carelessness, but you may try again.)
        misses += 1
        main()
    else:
        print('Correct!')
        hits += 1
        mandos()
        
#a function to assess the results and ask if the player wants to go again, checking to see how long of a test they elected to take and rewarding only a perfect score while declaring you a scrub if you miss even one question
def mandos():
    global hits
    global misses
    global questions_total
    name= 'null'
    win = False
    winner = []
    if misses == 0 and hits < questions_total:
        print('You have answered', hits, 'of the total', questions_total,'questions in the challenge.')
        print('\n\n')
        choose_question()
    elif hits == questions_total:
        print("You have successfully completed the challenge!")
        win = True
    else:
        print('You have failed!  Only a perfect score can be added to the halls of honor!')
# a collection of responses based upon the number of questions attempted must be offered consistent with the difficulty pick function
    if questions_total == 5 and win == True:
        print('You have answered 5 questions!  Your peasant mother must be whatever passes for proud among your kind.\nWhat no-doubt dwarf name shall I record for you?\n')
        name = input()
        winner =[name, 'peasant', str(questions_total)]
        try:
            lists = open('winners.csv', mode = 'r', newline='')
        except FileNotFoundError:
            print('Regrettably, the high scores file is not in the proper directory.  Add the winners.csv file to the directory and try again.')
        else:
            eonwe = csv.reader(lists)
            holder = []
            for lines in eonwe:
                holder.append(lines)
            holder.append(winner)
            lists.close()
            lists = open('winners.csv', mode = 'w', newline='')
            olorin = csv.writer(lists)
            for lines in holder:
                olorin.writerow(lines)
            lists.close()
    elif questions_total > 5 and questions_total <10 and win == True:
        print('A Watcher of Films, you have the enthusiasm for the Tolkien fandom, if not the commitment.  What prosaic commoner name shall I record for you?\n')
        name = input()
        winner =[name, 'Watcher of Films', str(questions_total)]
        try:
            lists = open('winners.csv', mode = 'r', newline='')
        except FileNotFoundError:
            print('Regrettably, the high scores file is not in the proper directory.  Add the winners.csv file to the directory and try again.')
        else:
            eonwe = csv.reader(lists)
            holder = []
            for lines in eonwe:
                holder.append(lines)
            holder.append(winner)
            lists.close()
            lists = open('winners.csv', mode = 'w', newline='')
            olorin = csv.writer(lists)
            for lines in holder:
                olorin.writerow(lines)
            lists.close()
    elif questions_total >9 and questions_total <15 and win == True:
        print('A Reader of Books, you know enough for respectable people to tolerate being seen with you publicly.  By what name shall you be called among polite company?\n')
        name = input()
        winner =[name, 'Reader of Books', str(questions_total)]
        try:
            lists = open('winners.csv', mode = 'r', newline='')
        except FileNotFoundError:
            print('Regrettably, the high scores file is not in the proper directory.  Add the winners.csv file to the directory and try again.')
        else:
            eonwe = csv.reader(lists)
            holder = []
            for lines in eonwe:
                holder.append(lines)
            holder.append(winner)
            lists.close()
            lists = open('winners.csv', mode = 'w', newline='')
            olorin = csv.writer(lists)
            for lines in holder:
                olorin.writerow(lines)
            lists.close()
    elif questions_total >14 and questions_total <20 and win == True:
        print('A Keeper of Lore, you have earned an honored place at the table of true Tolkien fans.  What honored name shall be recorded?\n')
        name = input()
        winner =[name, 'Keeper of Lore', str(questions_total)]
        try:
            lists = open('winners.csv', mode = 'r', newline='')
        except FileNotFoundError:
            print('Regrettably, the high scores file is not in the proper directory.  Add the winners.csv file to the directory and try again.')
        else:
            eonwe = csv.reader(lists)
            holder = []
            for lines in eonwe:
                holder.append(lines)
            holder.append(winner)
            lists.close()
            lists = open('winners.csv', mode = 'w', newline='')
            olorin = csv.writer(lists)
            for lines in holder:
                olorin.writerow(lines)
            lists.close()
    elif questions_total >= 20 and win == True:
        print('One of The Wise, none would question your commitment to the fandom or your mastery of the stories and songs of Middle Earth.\nWhat name shall stand among those others of deep wisdom?\n')
        name = input()
        winner =[name, 'The Wise', str(questions_total)]
        try:
            lists = open('winners.csv', mode = 'r', newline='')
        except FileNotFoundError:
            print('Regrettably, the high scores file is not in the proper directory.  Add the winners.csv file to the directory and try again.')
        else:
            eonwe = csv.reader(lists)
            holder = []
            for lines in eonwe:
                holder.append(lines)
            holder.append(winner)
            lists.close()
            lists = open('winners.csv', mode = 'w', newline='')
            olorin = csv.writer(lists)
            for lines in holder:
                olorin.writerow(lines)
            lists.close()
    elif questions_total == len(elrohir) and win == True:
        print('You are a master of the trivia and lore of the Tolkien legendarium, and none would dare to question your skill,\nBe he foe or friend, be he foul or clean,\nbrood of Morgoth or bright Vala,\nElda or Maia or Aftercomer,\nMan yet unborn upon Middle-earth.\n\nCongratulations on a perfect score of 100% of the questions database.')
        name = input()
        winner =[name, 'Spirit of Fire', str(questions_total)]
        try:
            lists = open('winners.csv', mode = 'r', newline='')
        except FileNotFoundError:
            print('Regrettably, the high scores file is not in the proper directory.  Add the winners.csv file to the directory and try again.')
        else:
            eonwe = csv.reader(lists)
            holder = []
            for lines in eonwe:
                holder.append(lines)
            holder.append(winner)
            lists.close()
            lists = open('winners.csv', mode = 'w', newline='')
            olorin = csv.writer(lists)  
            for lines in holder:
                olorin.writerow(lines)
            lists.close()
            
    main()

# a function to explain how to expand the list so enthusiastic nerds can expand the game
def expand_help():
    print('Thanks for playing the game, you can help expand the game\nif you have the commitment to pore through Silmarillion pages or haunt the wikis.\nThe game questions are in the file quiz_questions.csv\nand you can expand the list using excel as long as you remember to keep it in .csv format.\n  The first column is for your question, the second for the correct answer,\n and the following three for three wrong answers.\nTry and choose wrong answers that are near to the correct answer,\nwe\'re in the business of weeding the knowledgable from the passing familiars.')
    input('hit enter to continue')
    print('The list of winners is also kept in such a file.\nIf you lose it, you can create a new one,\nso long as you remember that your first line should have \'NAME,RANK,QUESTIONS\' in it.')
    input('hit enter to return to the home menu')
    main()

#a main menu where you can read the names of those who have succeeded as well as begin or quit the game
def main():
    global playing
    global question_total
    global hits
    global misses
    global current_question
    global asked
    global playing
    #reinitialization
    question_total= 0
    hits = 0
    misses = 0
    current_question= ''
    asked = ['null']
    playing = True
    while playing == True:
        print('##################MENU######################')
        print('Enter your selection\n\n1. Begin the Challenge\n2. See the Lists of Honor\n3. Help\n4. Quit')
        selection = int(input())
        try:
            selection = int(selection)
        except ValueError:
            print('You must enter a choice using the numbers 1 through 4, words may not be entered.')
            selection = int(input())            
        while selection != 1 and selection != 2 and selection != 3 and selection != 4:
            print('You must enter a choice using the numbers 1 through 4.')
            selection = int(input())
        if selection == 1:
            difficulty()
        elif selection == 2:
            halls_of_honor()
        elif selection ==3:
            expand_help()
        elif selection == 4:
            print('Thank you for playing')
            exit()

#a fucntion to pull the winners from the list of winners and display it
def halls_of_honor():
    try:
        lists = open('winners.csv', mode = 'r')
    except FileNotFoundError:
        print('Regrettably, the high scores file is not in the proper directory.  Add the winners.csv file to the directory and try again.')
    eonwe = csv.reader(lists)
    t1=''
    t2=''
    print('|||||||||||||||THESE ARE THE NAMES OF HONOR AMONG THE VALAR||||||||||||||')
    for lines in eonwe:
        if len(lines[0]) >= 6 and len(lines[0])<10:
            t1 = '\t'
        elif len(lines[1]) >10:
            t1 =''
        else:
            t1= '\t\t'
        if len(lines[1]) >=6 and len(lines[1]) <10:
            t2 = '\t'
        elif len(lines[1]) >10:
            t2 = ''
        else:
            t2= '\t\t'
        print(lines[0],t1,lines[1],'\t',t2,lines[2])
    lists.close()
    main()
    
'''
|||||||||||||||||||The operational logic||||||||||||||||||||||
'''
#flat code for things that must always happen
#a dictionary question lists paired against lists of answers, the first item in the question list must be the question, the second the correct answer, pulled from a csv so that the test can become ever more difficult
silmaril = open('quiz_questions.csv', mode = 'r')
eonwe = csv.DictReader(silmaril)
elrond = {}
elrohir = []
for lines in eonwe:
    key_prep = lines['q']
    values_prep= [lines['a'], lines['w1'], lines['w2'], lines['w3']]
    elrond.update({key_prep:values_prep})
silmaril.close()

for keys in elrond:
    elrohir.append(keys)

#a welcome message to frighten the unworthy and stir the courage of the bold
print("Welcome to Silmarillion Quiz\nWhere we distinguish the real Tolkien nerds from the plebian rabble")

#function loops
main()
