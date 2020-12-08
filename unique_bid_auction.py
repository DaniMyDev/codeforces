""" There is a game called "Unique Bid Auction". You can read more about it here: https://en.wikipedia.org/wiki/Unique_bid_auction (though you don't have to do it to solve this problem).

Let's simplify this game a bit. Formally, there are n participants, the i-th participant chose the number ai. The winner of the game is such a participant that the number he chose is unique (i. e. nobody else chose this number except him) and is minimal (i. e. among all unique values of a the minimum one is the winning one).

Your task is to find the index of the participant who won the game (or -1 if there is no winner). Indexing is 1-based, i. e. the participants are numbered from 1 to n.

You have to answer t independent test cases.

Input
The first line of the input contains one integer t (1≤t≤2⋅104) — the number of test cases. Then t test cases follow.

The first line of the test case contains one integer n (1≤n≤2⋅105) — the number of participants. The second line of the test case contains n integers a1,a2,…,an (1≤ai≤n), where ai is the i-th participant chosen number.

It is guaranteed that the sum of n does not exceed 2⋅105 (∑n≤2⋅105).

Output
For each test case, print the answer — the index of the participant who won the game (or -1 if there is no winner). Note that the answer is always unique. """
# test cases
t = int(input())

for i in range(t):

    # participants
    n = int(input())
    a = input().replace(' ', '')
    a_copy = a

    winner = 999999

    size = len(a)
    j = 0

    while size >= 1:

        if a.count(a[j]) == 1 and int(a[j]) < winner:
            winner = int(a[j])

        # delete repeated elements
        a = a.replace(a[j], '')
        size = len(a)
        j = 0

    winner_index = a_copy.find(str(winner))
    if winner_index != -1:
        print(winner_index+1)
    else:
        print(winner_index)
