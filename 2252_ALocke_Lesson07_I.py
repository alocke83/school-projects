# FILE:2252_ALocke_Lesson07_I.py
# NAME: Records of World Series Data Tool
# AUTHOR(s): Adam Locke
# DATE:month/day/year  05/1/2020
# PURPOSE: presents the years in which a given team won, or tells you the winning team for a given year

#global variables
content = []
s_list = []
dates = []
winners =[]
dictionary = {}
counter = 0
checking = 'y'
data_type = 'null'

'''------------------------------flat code for things that happen every time-------------------------------------------------------'''
print("Welcome to Records of World Series Data Tool\n")
#open the file for use, if it's not in the directory complain about it, if it it is in the directory give some indication that you got it as a sort of comfort message
try:
    data = open('WorldSeriesWinners.txt', 'r')
except FileNotFoundError:
    print('The world series data is not in the current directory, please download the data and try again.')
else:
    input('Hit Enter to load data.')
    try:
        text = data.readlines()
        print(len(text), 'items loaded.')
    except:
        print('an error occurred while loading data.')

#write the contents into a dictionary in which the year is the key
'''first clean off all the useless bits from the strings and stick the strings in a list'''
for line in text:
    target = str(line)
    target = target.strip()
    if target[-1] == 'n' and target[-2] =='\\':
        target = target.slice[-2,-1]
    content.append(target)

'''next differentiate between years and team names and stick them in two lists of presumably equal length'''
for item in content:
    if item[0] == '1' or item[0] == '2':
        if item[1] == '9' or item[1] == '0':
            result = str(item)
            result.rstrip()
            dates.append(result)
    else:
        winners.append(str(item))

'''now combine the lists of equal length into the dictionary by using the dates as a key and mirroring their length-based indecies with that of the winning team list'''
for key in dates:
    dictionary.update({dates[dates.index(key)]:winners[dates.index(key)]})

          
'''close the file since the dictionary is all i need now'''
data.close()

'''-----------------------------------looping functions for user input decisions------------------------------------------------------------'''
#a function to report the team who won in a given year
def years_mode():
    global dictionary
    print('Enter the year you are insterested in, the team that won the world series will be displayed.')
    year = str(input())
    count = 0
    for keys in dictionary:
        if keys[0] == year[0] and keys[1] == year[1] and keys[2] == year[2] and keys[3] == year[3]:
                  print('In', year, 'the team', dictionary[keys], 'won the world series.')

    
#a function to report the years a given team won and how many times in total they have won
def winners_check():
    global dictionary
    print('Enter the name of the team you are curious about, years the world series was won will be displayed.')
    team = input()
    team = team.lower()
    display_team_list= team.split(" ")
    cap_team_list= []
    display_team_str= ""
    for words in display_team_list:
        convert = words.capitalize()
        cap_team_list.append(convert)
        cap_team_list.append(" ")
    display_team_str = display_team_str.join(cap_team_list)
    display_team_str = display_team_str.strip()

    win_years= []
    loser_check= []
    total_wins=0
    
    for keys in dictionary:
        if dictionary.get(keys) == display_team_str:
            win_years.append(keys)
            total_wins += 1
                             
    total_wins = len(win_years)

    if total_wins == 0:
                             print('The team you entered does not exist, or worse they are losers.  Check your spelling, or enter a better team.')
                             data_checking()
    else:
        print('The team', display_team_str, 'won the world series', total_wins, 'times in the following years:')
        for years in win_years:
            print(years, end= ' ')
        print('\n')

#a while loop to ask the user to recall as much data as they like, while also asking if they care to continue
def data_checking():
    global checking
    global data_type
while checking == 'y':
    print('enter WINNERS to search years a team won and YEARS to find out which team won in a given year.\nType QUIT to end the inquiry.')
    data_type=input()
    data_type= data_type.upper()
    while data_type != 'WINNERS' and data_type != 'YEARS' and data_type != 'QUIT':
        print('you must enter WINNERS or YEARS.')
        data_type = input()
    else:
        if data_type == 'WINNERS':
            winners_check()
            pass
        elif data_type == 'YEARS':
            years_mode()
        elif data_type == 'QUIT':
            exit
            print('Thank you for reviewing the information, it\'s always available for you.')
            input('hit enter to close')
            quit()
            

#mainline logic

data_checking()

