""" An elephant decided to visit his friend. It turned out that the elephant's house is located at point 0 and his friend's house is located at point x(x > 0) of the coordinate line. In one step the elephant can move 1, 2, 3, 4 or 5 positions forward. Determine, what is the minimum number of steps he need to make in order to get to his friend's house.

Input
The first line of the input contains an integer x (1 ≤ x ≤ 1 000 000) — The coordinate of the friend's house.

Output
Print the minimum number of steps that elephant needs to make to get from point 0 to point x. """

coordenate = int(input())

moves = 0

if coordenate >= 5:
    moves += coordenate / 5
    coordenate %= 5

if coordenate >= 4:
    moves += coordenate / 4
    coordenate %= 4

if coordenate >= 3:
    moves += coordenate / 3
    coordenate %= 3

if coordenate >= 2:
    moves += coordenate / 2
    coordenate %= 2

if coordenate >= 1:
    moves += coordenate / 1
    coordenate %= 1

print(int(moves))