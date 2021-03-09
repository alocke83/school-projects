# FILE:2252_ALocke_Lesson05_I.py
# NAME:Glorious Encoding Software
# AUTHOR(s): Adam Locke
# DATE:29/3/2020
# PURPOSE: encode important information for purposes of the state that cannot be discussed

'try this one'
'809901819805818822805901820808805901819815822809805820901821814809815814902'

#we must enter code or decode mode
def mode_select():
    mode = input('END, CODE, or DECODE?\n')
    if mode == 'CODE':
        encode()
    elif mode == 'DECODE':
        decode()
    elif mode == 'END':
        print('All encoding work is useful in defeating enemies of the state\nBe proud to serve glorious people\'s republic.')
        exit
    else:
        print('You must enter END, CODE, or DECODE')
        init()
    

#we must ask for the string to be examined in encode mode, it checks every character and converts
def encode():
    string = input('Enter the text to be encoded:\n')
    string = string.lower()
    print(string.replace('a', '801')
        .replace('b', '802')
        .replace('c', '803')
        .replace('d', '804')
        .replace('e', '805')
        .replace('f', '806')
        .replace('g', '807')
        .replace('h', '808')
        .replace('i', '809')
        .replace('j', '810')
        .replace('k', '811')
        .replace('l', '812')
        .replace('m', '813')
        .replace('n', '814')
        .replace('o', '815')
        .replace('p', '816')
        .replace('q', '817')
        .replace('r', '818')
        .replace('s', '819')
        .replace('t', '820')
        .replace('u', '821')
        .replace('v', '822')
        .replace('w', '823')
        .replace('x', '824')
        .replace('y', '825')
        .replace('z', '826')
        .replace(' ', '901')
        .replace('.', '902')
        .replace('!', '903')
        .replace('?', '904'))
    init()

#we must have a function to examine a string in decode mode, it slices the string into 3 character segments and decodes to a string
#wait do I need to slice?  I think I've solved the crypto problem with my character maths
def decode():
    string = input('Enter the code for conversion to text:\n')
    print (string.replace('801', 'a')
    .replace('802', 'b')
    .replace('803', 'c')
    .replace('804', 'd')
    .replace('805', 'e')
    .replace('806', 'f')
    .replace('807', 'g')
    .replace('808', 'h')
    .replace('809', 'i')
    .replace('810', 'j')
    .replace('811', 'k')
    .replace('812', 'l')
    .replace('813', 'm')
    .replace('814', 'n')
    .replace('815', 'o')
    .replace('816', 'p')
    .replace('817', 'q')
    .replace('818', 'r')
    .replace('819', 's')
    .replace('820', 't')
    .replace('821', 'u')
    .replace('822', 'v')
    .replace('823', 'w')
    .replace('824', 'x')
    .replace('825', 'y')
    .replace('826', 'z')
    .replace('901', ' ')
    .replace('902', '.')
    .replace('903', '!')
    .replace('904', '?'))
    init()


#cuz I'm a fancy bitch I want it in interface, let's see if i have time

#we need a function to return to the beginning for the next input
def init():
    mode_select()
            
#mainline
def main():
    print('Welcome to coding program for glorious people\'s republic.')
    print('Reminder: Glorious Leader can read even encoded words\nmaintain compliance with thought ministry guidelines')
    init()

main()
