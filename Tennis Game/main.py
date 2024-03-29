## Write a program that shows the score throughout a tennis game, and who won
## The program will receive a sequence made of "P1" (Player 1) or "P2" (Player 2),
## depending on who won each point

## Score is -> "love" (NULL), 15, 30, 40, "Deuce" (Draw), advantage.
"""
For example, given this sequence: [P1, P1, P2, P2, P1, P2, P1, P1], the program would show:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   Deuce
 *   40 - 30
 *   Deuce
 *   Advantage P1
 *   P1 has Won
"""

def show_result(points):
    p1 = points[0]
    p2 = points[1]


    if p1 == 0:
        p1 = "Love"
    elif p1 == 40 and p2 == 40:
        p1 = "Advantage"
    elif p1 >= 50 and p2 <= 40:
        p1 = "Winner P1"

    if p2 == 0:
        p2 = "Love"
    elif p2 == 40 and p1 == 40:
        p2 = "Advantage"
    elif p2 >= 50 and p1 <= 40:
        p2 = "Winner P2"


    if p1 == p2:
        print("Deuce")
    else:
        if p1 != "Advantage" and p2 != "Advantage":
            print(f"{p1} - {p2}")
        elif p1 == "Advantage":
            print(f"{p1} P1")
        elif p2 == "Advantage":
            print(f"{p2} P2")
        elif p1 == "Winner":
            print(p1)
            return True
        else:
            print(p2)
            return True


    return False # if no one won

def tennis_match(game):
    points = [0, 0] # one position per each player

    for player in game:
        if player == "P1" and points[0] != 30:
            points[0] += 15
        elif player == "P1" and points[0] > 15:
            points[0] += 10
            if points[0] > 40 and points[1] > 40:
                points[1] -= 10

        if player == "P2" and points[1] != 30:
            points[1] += 15
        elif player == "P2" and points[1] > 15:
            points[1] += 10
            if points[1] > 40 and points[1] > 40:
                points[0] -= 10
        

        res = show_result(points)
        if res:
            return res

if __name__ == "__main__":
    game = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]

    tennis_match(game)

