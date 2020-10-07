#!/usr/bin/python

def biconditional(q, r):
    if q and r:
        answer = True

    elif not q and not r:
        answer = True

    else:
        answer = False

    return answer
