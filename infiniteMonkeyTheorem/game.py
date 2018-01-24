# pylint: disable=missing-docstring
from __future__ import print_function
import random

def best_character(beststring, goal, i):
    if beststring[i] == goal[i]:
        return True
    else:
        return False

def generator(beststring, goal):
    alphabets = "abcdefghijklmnopqrstuvwxyz "
    res = ""
    leng = len(goal)
    if beststring != "":
        for i in range(leng):
            if best_character(beststring, goal, i):
                res = res + beststring[i]
            else:
                res = res + alphabets[random.randrange(27)]
    else:
        for i in range(leng):
            res = res + alphabets[random.randrange(27)]

    return res

def scorer(goal, teststring):
    score = 0
    leng = len(goal)
    for i in range(leng):
        if goal[i] == teststring[i]:
            score = score + 1
    return score/len(goal)

def game():
    goal = "methinks it is like a weasel"
    beststring = ""
    bestscore = 0
    newstring = generator(beststring, goal)
    score = scorer(goal, newstring)
    times = 1
    while score < 1:
        if score > bestscore:
            bestscore = score
            beststring = newstring
            print("Score = %f String = %s Times = %i" %(score, newstring, times))
        newstring = generator(beststring, goal)
        score = scorer(goal, newstring)
        times = times + 1
        if score == 1:
            print()
            print()
            print("Score = %f String = %s Times = %i" %(score, newstring, times))

game()
