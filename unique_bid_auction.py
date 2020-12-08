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
        print(-1)
