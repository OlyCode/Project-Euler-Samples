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
from math import sqrt

#####################################################################
#####################################################################
####   Project Euler   ##############################################
#####################################################################
#####################################################################


# Problem 59
# Each character on a computer is assigned a unique code and the preferred
# standard is ASCII (American Standard Code for Information Interchange).
# For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
# A modern encryption method is to take a text file, convert the bytes to
# ASCII, then XOR each byte with a given value, taken from a secret key.
# The advantage with the XOR function is that using the same encryption
# key on the cipher text, restores the plain text; for example,
# 65 XOR 42 = 107, then 107 XOR 42 = 65.
# For unbreakable encryption, the key is the same length as the plain text
# message, and the key is made up of random bytes. The user would keep the
# encrypted message and the encryption key in different locations, and
# without both "halves", it is impossible to decrypt the message.
# Unfortunately, this method is impractical for most users, so the modified
# method is to use a password as a key. If the password is shorter than the
# message, which is likely, the key is repeated cyclically throughout the
# message. The balance for this method is using a sufficiently long password
# key for security, but short enough to be memorable.
# Your task has been made easy, as the encryption key consists of three
# lower case characters. Using cipher1.txt, a file containing the encrypted
# ASCII codes, and the knowledge that the plain text must contain common
# English words, decrypt the message and find the sum of the ASCII values
# in the original text.

def solveProblem59():
    def getNums(charactersList):
        returnList = []
        for x in range(len(charactersList)):
            returnList.append(ord(charactersList[x]))
        return returnList
    def getChars(numbersList):
        returnList = []
        for x in range(len(numbersList)):
            returnList.append(chr(numbersList[x]))
        return "".join(returnList)
    def test(testWord, testString):
        matchCount = 0
        for x in range(len(testString)-len(testWord)+1):
            if testWord[0] == testString[x]:
                if all(testWord[y] == testString[x+y] for y in range(len(testWord))):
                    matchCount += 1
        return matchCount
    def cipher(passKey, passList):
        returnTemp = []
        for x in range(len(passList)):
            if type(passKey) == type(str()):
                passKey = getNums(passKey)
            if type(passList) == type(str()):
                passList = getNums(passList)
            returnTemp.append(passKey[x%len(passKey)]^passList[x])
        return returnTemp
        
    try:
        f = open('cipher.txt','r')
    except IOError:
        return 0
    line = f.read()
    f.close()
    line = line.split(',')
    line[-1] = line[-1][:-1]
    for x in range(len(line)):
        line[x] = int(line[x])

    testCode = cipher([100,101,102],"this is a the the the test code")
    answerNumber = 0

    for x in range(97,123):
        for y in range(97,123):
            for z in range(97,123):
                if test(getNums('the'),cipher([x,y,z],line)) >= 1:
                    if test(getNums('and'),cipher([x,y,z],line)) >= 1:
                        if test(getNums('that'),cipher([x,y,z],line)) >= 1:
                            #print x,y,z
                            temp = cipher([x,y,z],line)
                            answerNumber = sum(temp)
                            print "\n", getChars(temp), "\n"
    print "\nThe solution to problem 59 is: %i" % answerNumber

solveProblem59()
