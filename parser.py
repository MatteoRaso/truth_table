#!/usr/bin/python

#Parses the function that the user inputs (as a string) and
#returns it. As there are some operations that can't be expressed
#as a single character in standard notation (like the biconditional),
#I had to create my own special notation.

#and - ^
#or - v
#xor - x
#conditional - >
#biconditional - $

#This means that the user will not be able to use these characters
#as variable names. While I'm a bit uncomfortable with restricting
#v and x, I understand that these aren't common letters or variable
#names when dealing with truth tables. It shouldn't inconvenience the
#end user whatsoever, but I'll obviously make a warning about this anyways.

def parser(string):
    #It's easier to prevent extra spaces from being present
    #if remove them all at the beginning and add them to
    #the function as we go along.
    string = string.replace(' ', '')
    string = string.replace('^', ' and ')
    string = string.replace('v', ' or ')
    #The last three are functions, not operators, so they have to
    #be properly parsed, not handled by a search-and-replace.
    done = False
    while not done:
        if 'x' not in string:
            done = True

        else:
            i = string.index('x')
            string = string.replace(string[i - 1] + string[i] + string[i + 1], 'xor(' + string[i - 1] + ',' + string[i + 1] + ')')

    done = False
    while not done:
        if '>' not in string:
            done = True

        else:
            i = string.index('>')
            string = string.replace(string[i - 1] + string[i] + string[i + 1], 'conditional(' + string[i - 1] + ',' + string[i + 1] + ')')

    done = False
    while not done:
        if '$' not in string:
            done = True

        else:
            i = string.index('$')
            string = string.replace(string[i - 1] + string[i] + string[i + 1], 'biconditional(' + string[i - 1] + ',' + string[i + 1] + ')')

    #The string sometimes ends up with a random '()' for some reason.
    string = string.replace('()', '')
    return string
