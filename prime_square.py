""" Sasha likes investigating different math objects, for example, magic squares. But Sasha understands that magic squares have already been studied by hundreds of people, so he sees no sense of studying them further. Instead, he invented his own type of square — a prime square.

A square of size n×n is called prime if the following three conditions are held simultaneously:

all numbers on the square are non-negative integers not exceeding 105;
there are no prime numbers in the square;
sums of integers in each row and each column are prime numbers.
Sasha has an integer n. He asks you to find any prime square of size n×n. Sasha is absolutely sure such squares exist, so just help him!

Input
The first line contains a single integer t (1≤t≤10) — the number of test cases.

Each of the next t lines contains a single integer n (2≤n≤100) — the required size of a square.

Output
For each test case print n lines, each containing n integers — the prime square you built. If there are multiple answers, print any. """

cases = int(input())

#we can just fill the square with 1 or zero, depends on the size (odd or even)
#if even, we just need to change the principal diagonal to 0

for c in range(0,cases):
    size = int(input())
    matrix = [[1 for i in range(size)] for j in range(size)]

    if size%2==0 and size!=2:
        for i in range(0,size):
            matrix[i][i] = 0
    
    for i in range(0,size):
        for j in range(0,size):
            print(str(matrix[i][j]), end=" ")
        print('\n')