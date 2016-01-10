# -*- coding: utf-8 -*-
#
#!Python 2.6
#
#Project Euler
#
#by Joe Mortillaro
#7/24/2011

import time
import copy
import math 
from math import sqrt

#############################################################
####    Project Euler    ####################################
#############################################################

# Problem 75
# It turns out that 12 cm is the smallest length of wire
# that can be bent to form an integer sided right angle
# triangle in exactly one way, but there are many more
# examples.
# 12 cm: (3,4,5)
# 24 cm: (6,8,10)
# 30 cm: (5,12,13)
# 36 cm: (9,12,15)
# 40 cm: (8,15,17)
# 48 cm: (12,16,20)
# In contrast, some lengths of wire, like 20 cm, cannot
# be bent to form an integer sided right angle triangle,
# and other lengths allow more than one solution to be
# found; for example, using 120 cm it is possible to form
# exactly three different integer sided right angle triangles.
# 120 cm: (30,40,50), (20,48,52), (24,45,51)
# Given that L is the length of the wire, for how many
# values of L ≤ 1,500,000 can exactly one integer sided
# right angle triangle be formed?
#
# Notes:
# if (a,b,c) is in S, then k(a,b,c) is in S.
# if k(a,b,c) is in S, then (a,b,c) is in S.
# if k|a & k|b then k|c   and   if k|b & k|c then k|a
# a^2 + b^2 = c^2
# sqrt(a^2 + b^2) = c
# a^2 + b^2 = c^2

def solveProblem75():
    def simpleTest(n):
        returnList = []
        if n % 2 == 1: return returnList
        c = n/2
        for b in range(1,c):
            a = n - b - c
            if a <= 0: break
            if a < b:
                if a*a + b*b == c*c:
                    returnList.append([a,b,c])
        return returnList
    def gcd(a,b):
        if b == 0: return a
        if a == 0: return b
        if a > b: return gcd(a-b,b)
        else: return gcd(b-a,a)
    def makeTriple(m,n):
        #generates all primitive Pythagorean triples
        #calls gcd(a,b)
        # N = m**2 - n**2 + 2*m*n + m**2 + n**2
        # if n = 1, then N = 2*m**2 + 2*m
        # ==> m = -1/2 + sqrt(4 + 8*N)/4
        if m <= n: return []
        if gcd(m,n) != 1: return []
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2
        temp = [a,b,c]
        temp.sort()
        return temp
    def test(x,y):
        #uses makeTriple and modifies answerList
        def add(A, B):
            [a,b,c] = A
            [d,e,f] = B
            return [a+d, b+e, c+f]
        addTemp = temp = makeTriple(x,y)
        if temp == []: return 0
        n = sum(temp)
        x = n
        while x < ceiling:
            if addTemp not in answerList[x]:
                answerList[x].append(addTemp)
            addTemp = add(addTemp, temp)
            x += n
        return 0

    #parameters
    ceiling = 1500001 #not inclusive
    answerNumber = 0

    answerList = []
    for x in range(ceiling):
        answerList.append([])

    for x in range(2, int(math.sqrt(4 + 8*ceiling)/4)):
        for y in range(1,x):
            test(x,y)

    for x in range(len(answerList)):
        if len(answerList[x]) == 1: 
            answerNumber += 1

    print "The solution to problem 75 is: " + str(answerNumber) + "."
    
solveProblem75()
