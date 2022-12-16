## Where's the robot?!
## Calculate where a robot will be (its final coords), if he's in a grid
## represented by the x and y axis
## - The robot starts at (0, 0)
## - To make him move, we send the function an integer array (+/- ints) that
##   indicates the walking sequence of the robot
## # For example: [10, 5, -2] he moves 10 steps forward, stops, then 5 steps fwd, stops, then 2 steps backwards
## # Thus, the final coords would be [-5, 12]
## - The first steps are done in the Y axis, moving towards the positive
##   part of the Y axis
## - The robot has a bug, however, that makes him turn 90 degrees counter-clockwise
##   every time he stops

def is_neg(number, signed):
    if signed == True:
        number = number * (-1)
        signed = False
    else:
        signed = True

    return number, signed

def get_robot_pos(steps):
    coords = [0, 0] # initial coords
    x_turn = False # kind of like a semaphore

    x_neg = True     # because he starts walking to the negative part of x
    y_neg = False    # "" to the positive part of y

    for walk in steps: # we change the coordinate he's modifying per iteration
        if x_turn == False:
            y = walk

            y, y_neg = is_neg(y, y_neg)
            
            coords[1] += y
            x_turn = True
        else:
            x = walk

            x, x_neg = is_neg(x, x_neg)

            coords[0] += x
            x_turn = False

    return coords

if __name__ == "__main__":
    steps = [3, -4, 2, -2, 1, 2]

    coords = get_robot_pos(steps)
    print("The final coordinates of the robot are -> ", coords)
