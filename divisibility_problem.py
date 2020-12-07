""" You are given two positive integers a and b. In one move you can increase a by 1 (replace a with a+1). Your task is to find the minimum number of moves you need to do in order to make a divisible by b. It is possible, that you have to make 0 moves, as a is already divisible by b. You have to answer t independent test cases.

Input
The first line of the input contains one integer t (1≤t≤104) — the number of test cases. Then t test cases follow.

The only line of the test case contains two integers a and b (1≤a,b≤109).

Output
For each test case print the answer — the minimum number of moves you need to do in order to make a divisible by b. """

cases = int(input())

for i in range(0,cases):
    case = input()
    tmp = case.split(' ')
    a = int(tmp[0])
    b = int(tmp[1])
    mod = a%b
    if mod != 0:
        moves = b - mod
    else:
        moves = mod
    print(moves)