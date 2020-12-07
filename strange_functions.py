""" Let's define a function f(x) (x is a positive integer) as follows: write all digits of the decimal representation of x backwards, then get rid of the leading zeroes. For example, f(321)=123, f(120)=21, f(1000000)=1, f(111)=111.

Let's define another function g(x)=xf(f(x)) (x is a positive integer as well).

Your task is the following: for the given positive integer n, calculate the number of different values of g(x) among all numbers x such that 1≤x≤n.

Input
The first line contains one integer t (1≤t≤100) — the number of test cases.

Each test case consists of one line containing one integer n (1≤n<10100). This integer is given without leading zeroes.

Output
For each test case, print one integer — the number of different values of the function g(x), if x can be any integer from [1,n]. """


#the answer is the number of digits, it is where the change occurs, it looses a zero and
cases = int(input())

for i in range(0,cases):
    n = input()
    print(len(n))