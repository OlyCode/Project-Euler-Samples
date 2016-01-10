# -*- coding: utf-8 -*-
#
#!Python 2.6
#
#Project Euler
#
#by Joe Mortillaro
#7/24/2011
#


from decimal import *
import time
import copy
import math 
from math import sqrt


#############################################################
####    Project Euler    ####################################
#############################################################


#Problem 64
#All square roots are periodic when written as continued
#fractions and can be written in the form:
#sqrt(N) = a_0 + (1/(a_1 + (1/(a_2 + 1/(a_3 + . . .
#For example, let us consider √23:
#sqrt(23) = 4 + sqrt(23) — 4 = 4 + (1/(1/(sqrt(23)-4)))
#     = 4 + 1/(1 + ((sqrt(23) - 3)/7))
#If we continue we would get the following expansion:
#sqrt(23) = 4 + (1/(1 + (1/(3 + (1/(1 + (1/(8 + ...
#
#The first ten continued fraction representations of
#(irrational) square roots are:
#√2=[1;(2)], period=1
#√3=[1;(1,2)], period=2
#√5=[2;(4)], period=1
#√6=[2;(2,4)], period=2
#√7=[2;(1,1,1,4)], period=4
#√8=[2;(1,4)], period=2
#√10=[3;(6)], period=1
#√11=[3;(3,6)], period=2
#√12= [3;(2,6)], period=2
#√13=[3;(1,1,1,1,6)], period=5
#
#Exactly four continued fractions, for N ≤ 13, have an odd period.
#How many continued fractions for N ≤ 10000 have an odd period?
#
#Notes:
#(C(A + B))                         ==>  [C,A,B] = N
#(1(0 + b))                         ==>  [1,0,b] = D
#
# bC(A - (B - Ib/C))                ==>  [bC, A, Ib/C]
#((CA)**2 - (C(B - Ib/C))**2        ==>  [C**2, 0


def solveProblem64():
    #note: numbers shall be [coeff, root, constant]

    def getFractionPeriod(n):

        if math.sqrt(n) % 1 == 0: return 0
        
        def GCD(a,b):
            ceiling = min(a,b)
            tempGCD = ceiling
            for x in range(0, ceiling):
                if a % (ceiling-x) == 0 and b % (ceiling -x) == 0:
                    return ceiling-x
                         
        def getNext(ND):
            N = ND[0]
            D = ND[1]
            
            if D[1] != 0: return "error"

            tempN = [N[0]*D[2], N[1], -N[2]] 
            tempD = [1, 0, N[0]**2 * N[1] - (N[0]*N[2])**2]
            tempG = GCD(tempN[0],tempD[2])
            tempN[0] = tempN[0]/tempG
            tempD[2] = tempD[2]/tempG
            tempI = int((tempN[0]*(math.sqrt(tempN[1])+tempN[2]))/ \
                              (tempD[0]*(math.sqrt(tempD[1])+tempD[2])))
            tempN[2] -= tempI*tempD[2]
            #return [tempI,[tempN, tempD]]
            return [tempN, tempD]

        def getFirst(number):
            temp = int(math.sqrt(number))
            #return [temp, [[1,number,-temp],[1,0,1]]]
            return [[1,number,-temp],[1,0,1]]

        checkList = [getFirst(n)]
        checkTest = 0
        while True:
            checkTest = getNext(checkList[-1])
            if checkTest in checkList: break
            checkList.append(checkTest)

        return len(checkList)

    answerNumber = 0
    for x in range(2,10001):
        temp = getFractionPeriod(x)
        if temp % 2 == 1:
            answerNumber += 1
    
    print "The solution to problem 64 is: " + str(answerNumber) + "."

solveProblem64()
