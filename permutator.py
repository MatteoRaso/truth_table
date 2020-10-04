#!/usr/bin/python

import numpy as np
import itertools

#Every possible truth combination can be represented as a vector.
#For example, if we have q and r, we can represent q being true
#and r being false as [1, 0]. This means that we can express
#every possible truth combination as a 2D array.

def permutator(num_elements: int):
    combinations = np.zeros(num_elements)
    combinations = np.array([tuple(combinations)])

    for i in range(1, num_elements + 1):
        combo = list(np.zeros(num_elements))

        for j in range(0, i):
            #Changes the macrostate of the truth combination.
            combo[j] = 1

        #Finds every microstate that coresponds to the macrostate
        #This step also turns the tuples into arrays.
        permuted = np.array(list(itertools.permutations(combo)))
        combinations = np.vstack((combinations, permuted))

    #Turns the elements back into tuples.
    data = [tuple(row) for row in combinations]
    #Gets rid of duplicate tuples.
    combinations = np.unique(data, axis = 0)
    return combinations
