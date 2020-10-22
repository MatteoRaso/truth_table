#!/usr/bin/python

#Isolates the variables from the parsed string.

def isolate_variables(string):
    string = string.replace("and", ",")
    string = string.replace("xor", ",")
    string = string.replace("or", ",")
    string = string.replace("biconditional", "")
    string = string.replace("conditional", "")
    string = string.replace("(", "")
    string = string.replace(")", "")

    return string
