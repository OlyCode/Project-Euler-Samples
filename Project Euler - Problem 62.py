# -*- coding: utf-8 -*-
#
#!Python 2.6
#
#Project Euler
#
#by Joe Mortillaro
#7/24/2011

from decimal import *
import time
import copy
import math 
from math import sqrt

#############################################################
####    Project Euler    ####################################
#############################################################

# Problem 62
# The cube, 41063625 = (345**3), can be permuted to produce two
# other cubes: 56623104 = (384**3) and 66430125 = (405**3).
# In fact, 41063625 is the smallest cube which has exactly three
# permutations of its digits which are also cube.
# Find the smallest cube for which exactly five permutations of
# its digits are cube.

def solveProblem62():

    #parameters
    testCeiling = 10**5
    
    def testIfPermutations(passA,passB):
        A = str(passA)
        B = str(passB)
        if len(A) != len(B):
            return False
        for x in range(9):
            if A.count(str(x)) != B.count(str(x)):
                return False
        return True

    def makeHash(passA):
        A = str(passA)
        returnList = []
        for x in range(10):
            returnList.append(A.count(str(x)))
        return returnList

    def subroutine(testCeiling, testLength):
        hashTable = []
        hashCounts = []
        x = 0
        while x <= testCeiling: 
            temp = makeHash(x**3)
            if temp in hashTable:
                hashCounts[hashTable.index(temp)] += 1
                if hashCounts[hashTable.index(temp)] >= testLength:
                    return temp
            else:        
                hashTable.append(makeHash(x**3))
                hashCounts.append(1)
            x += 1

    answerTemp = subroutine(10**12, 5)
    answerNumber = 0
    x = 0
    while x <= testCeiling: 
        temp = makeHash(x**3)
        if temp == answerTemp:
            answerNumber = x**3
            break
        x += 1

    print "The solution to problem 62 is: " + str(answerNumber) + "."

solveProblem62()
