// ProjectEuler.cs
// Joe Mortillaro
// 10/1/2015

using System.Collections.Generic; // This allows Lists to be used.
using System;
using System.Linq;  

public class ProjectEuler_1to5
{
   public static void Main() {
        var problem01 = new Problem01();
        System.Console.WriteLine("Answer 01: " + problem01.Solve());

        var problem02 = new Problem02();
        System.Console.WriteLine("Answer 02: " + problem02.GetAnswer());
        
        var problem03 = new Problem03();
        System.Console.WriteLine("Answer 03: " + problem03.AnswerNumber);
        
        var problem04 = new Problem04();
        System.Console.WriteLine("Answer 04: " + problem04.getAnswer());
        
        var problem05 = new Problem05();
        System.Console.WriteLine("Answer 05: " + problem05.getAnswer());
        
        //var problem06 = new Problem06();
        //System.Console.WriteLine("Answer 06: " + problem06.getAnswer());
    }
}

public static class Tools 
{
    static public List<long> Factor(long number) {
        long x = 2;
        long y = number;
        var returnList = new List<long>();
        do {
            if (y % x == 0) {
                returnList.Add(x);
                y = y/x;
                x = 2;
            }
        } while (++x <= y/2);
 
        if (y != 1) returnList.Add(y);
        return returnList;
    }
    
    static public Dictionary<long, long> GetCount(List<long> numberList) {
        var returnDict = new Dictionary<long, long>();
        foreach (long x in numberList) {
            if (returnDict.ContainsKey(x) == true) {
                returnDict[x] += 1;
            }
            else if (returnDict.ContainsKey(x) == false) {
                returnDict.Add(x, 1);
            }
        }
        return returnDict;
    }
}

// Problem 1:
// If we list all the natural numbers below 10 that are multiples of 
// 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. 
// Find the sum of all the multiples of 3 or 5 below 1000. 
// Answer: 233168 
class Problem01 
{
    public int Solve() {
        var answerNumber = 0;
        for (var x = 1; x < 1000; ++x) {
            if  (x % 3 == 0 || x % 5 == 0) {
                answerNumber += x;
            }
        }
        return answerNumber;
    }
}

// Problem 2: 
// Each new term in the Fibonacci sequence is generated by adding the 
// previous two terms. By starting with 1 and 2, the first 10 terms 
// will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ... 
// By considering the terms in the Fibonacci sequence whose values do 
// not exceed four million, find the sum of the even-valued terms.
// Answer: 4613732
class Problem02 
{
    int answerNumber = 0;
    public int GetAnswer() {
        return answerNumber;
    }
    public Problem02() {
        answerNumber = 0;
        var fibList = new List<int>();
        var x = 0;
        var y = 1;
        var z = 1;
        while (z < 4000000) {
            z = x + y;
            x = y;
            y = z;
            if (z % 2 == 0) fibList.Add(z);
        }
        answerNumber = fibList.Sum();
    }
}

// Problem 3:
// The prime factors of 13195 are 5, 7, 13 and 29.
// What is the largest prime factor of the number 600851475143 ?
// Answer: 6857
class Problem03 
{
    public long AnswerNumber { get; set;}   
    public Problem03() {
        AnswerNumber = 0;
        var factorList = new List<long>();
        factorList = Tools.Factor(600851475143);
        long z = 1;
        
        foreach (long x in factorList) {
            z = z * x;
            if (x > AnswerNumber) {
                AnswerNumber = x;
            }
        }
    }
}

// Problem 4:
// A palindromic number reads the same both ways. The largest 
// palindrome made from the product of two 2-digit numbers is 
// 9009 = 91(99).
// Find the largest palindrome made from the product of two 3-digit 
// numbers.
// Answer: 906609
class Problem04 
{
    long answerNumber = 0;

    bool test(long n) {
        var returnValue = true;
        string s = n.ToString();
        for (int x = 0; x <= s.Length/2; ++x) {
            if (s[x] != s[s.Length - x-1]) {
                returnValue = false;
            }
        }
        return returnValue;      
    }

    public Problem04() {
        for (int y = 999; y > 0; --y) {
            for (int x = y-1; x > 0; --x) {
                if (x*y <= this.answerNumber) break;
                if (this.test(x*y) == true) {
                    this.answerNumber = x*y;
                }
            }
            if (y*(y-1) <= this.answerNumber) break;
        }
    }
    
    public int getAnswer() {
        return (int)answerNumber;
    }
}

// Problem 5:
// 2520 is the smallest number that can be divided by each of the 
// numbers from 1 to 10 without any remainder.
// What is the smallest positive number that is evenly divisible 
// by all of the numbers from 1 to 20?
// Answer: 232792560
class Problem05 
{
    long answerNumber = 1;
    
    public Problem05() {
        var factorCount = new Dictionary<long, long>();
        for (int x = 1; x <= 20; ++x) {
            var tempCount = Tools.GetCount(Tools.Factor(x));
            foreach (long i in tempCount.Keys) {
                if (factorCount.ContainsKey(i)) {
                    if (factorCount[i] < tempCount[i]) {
                        factorCount[i] = tempCount[i];
                    }
                }
                else {
                    factorCount.Add(i, tempCount[i]);
                }
            }            
        }
        foreach (long i in factorCount.Keys) {
            answerNumber *= (long) Math.Pow(i, factorCount[i]);
        }
    }
    
    public int getAnswer() {
        return (int) answerNumber;
    }
}

// Problem 6
// The sum of the squares of the first ten natural numbers is, 
// 1^2 + 2^2 + ... + 10^2 = 385
// The square of the sum of the first ten natural numbers is,
// (1 + 2 + ... + 10)^2 = 55^22 = 3025
// Hence the difference between the sum of the squares of the first ten 
// natural numbers and the square of the sum is 3025 -385 = 2640.
// Find the difference between the sum of the squares of the first one 
// hundred natural numbers and the square of the sum.
// Answer: 25164150
class Problem06 
{
    long answerNumber = 0;
    int ceiling = 10;

    public Problem06() 
    {
        // squareOfSums
        long squareOfSums = 0;
        for (int x = 1; x <= ceiling; ++x) 
        {
            squareOfSums += x;
        }
        squareOfSums = (long)Math.Pow(squareOfSums,2);
        
        // sumOfSquares
        long sumOfSquares = 0;
        for (int x = 1; x <= ceiling; ++x) 
        {
            sumOfSquares += x*x;
        }

        this.answerNumber = Math.Abs(sumOfSquares - squareOfSums);
    }
    
    public int getAnswer() {
        return (int)this.answerNumber;
    }
}




//Problem 7
//By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we 
//can see that the 6th prime is 13.
//What is the 10,001st prime number?
//Answer: 104743

//Problem 8
//Find the greatest product of five consecutive digits in the 1000-digit 
//number in text.txt.
//Answer: 40824

//text.txt contains the following:
//73167176531330624919225119674426574742355349194934
//96983520312774506326239578318016984801869478851843
//85861560789112949495459501737958331952853208805511
//12540698747158523863050715693290963295227443043557
//66896648950445244523161731856403098711121722383113
//62229893423380308135336276614282806444486645238749
//30358907296290491560440772390713810515859307960866
//70172427121883998797908792274921901699720888093776
//65727333001053367881220235421809751254540594752243
//52584907711670556013604839586446706324415722155397
//53697817977846174064955149290862569321978468622482
//83972241375657056057490261407972968652414535100474
//82166370484403199890008895243450658541227588666881
//16427171479924442928230863465674813919123162824586
//17866458359124566529476545682848912883142607690042
//24219022671055626321111109370544217506941658960408
//07198403850962455444362981230987879927244284909188
//84580156166097919133875499200524063689912560717606
//05886116467109405077541002256983155200055935729725
//71636269561882670428252483600823257530420752963450

//Problem 9:
//A Pythagorean triplet is a set of three natural numbers, a, b, and c, 
//for which, a^2 + b^2 = c^2 For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
//There exists exactly one Pythagorean triplet for which a + b + c = 1000.
//Find the product abc.
//Answer: 31875000

//Problem 10
//The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
//Find the sum of all the primes below two million.
//Answer: 142913828922
