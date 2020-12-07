""" Scrooge McDuck keeps his most treasured savings in a home safe with a combination lock.
Each time he wants to put there the treasures that he's earned fair and square, he has
to open the lock.

The combination lock is represented by n rotating disks with digits from 0 to 9 written
on them. Scrooge McDuck has to turn some disks so that the combination of digits on the
disks forms a secret combination. In one move, he can rotate one disk one digit forwards
or backwards. In particular, in one move he can go from digit 0 to digit 9 and vice versa.
What minimum number of actions does he need for that? """


# get user input
disks = int(input())
original = input()
correct = input()


if len(original) == disks and len(correct) == disks:

    moves = 0

    for d in range(disks):

        # get the difference and apply abs
        diff = abs(int(original[d]) - int(correct[d]))
        #check if greater than 5 (to decide up or down moves)
        if diff > 5:
            diff = 10 - diff
        moves += diff

    print(moves)

else:

    print('wrong size input, check your input!')