#!/usr/bin/python

import csv

from operators.xor import *
from operators.conditional import *
from operators.biconditional import *

from parser import *
from permutator import *
from isolate_variables import *

string = input("Type in your statement: ")
string = parser(string)

variables = isolate_variables(string)

command = "f = lambda " + variables + ": " + string
exec(command)

variables = variables.replace(",", "")
variables = variables.replace(" ", "")

truth_input = permutator(len(variables))
fields = list(variables) + [string]

truth_output = []

#Not the most efficent design, but fairly minor compared to how laggy
#permutator.py can be past 7 variables. Still might want to redesign it.
for i in range(0, len(truth_input)):
    statement = ''
    for j in range(0, len(truth_input[i])):
        statement += str(truth_input[i][j])
        #We don't want a trailing comma
        if j != (len(truth_input[i]) - 1):
            statement += ', '

    exec("value = f(" + statement + ")")
    truth_output.append(value)

#We need it as an array instead of a list to get the transpose.
truth_output = np.array([truth_output])
#Combines our two arrays
final_results = np.column_stack((truth_input, truth_output.T))
np.savetxt("truth.csv", final_results, delimiter=',', fmt='%d')
