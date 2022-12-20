## Create a program that can draw a square or a triangle using only asterisks "*"
## The user will have to type in the size of the sides, and what shape to draw

def draw_square(size):
    print("", "*" * size)
    for i in range (0, size - 2):
        print("*", " " * (size - 2), "*")
    
    print("", "*" * size)

def draw_triangle(size):
    i = 0
    j = size
    while i < size:
        if i == 0:
            print("*")
            pass
        elif
        i+=1
        j-=1
        

if __name__ == "__main__":
    draw_square(5)