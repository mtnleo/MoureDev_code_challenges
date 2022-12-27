## Write a program that prints numbers 1 to 100
## (both included and adding a new line in each print)
## swapping as it shows:
"""
- Multiples of 3, with 'fizz'
- Multiples of 5, with 'buzz'
- Multiples of 3 and 5, with 'fizzbuzz'
"""

def fizz_buzz():
    text = ""
    for i in range(0, 101):
        text = str(i) + " "
        if i % 3 == 0:
            text = text + "fizz"
        if i % 5 == 0:
            text = text + "buzz"
        
        print(text)

if __name__ == "__main__":
    fizz_buzz()