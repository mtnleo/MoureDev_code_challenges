## Create a program that gets a text and transforms it from
## natural language to 'hacker language' (aka "leet" or "1337")
## Use the table shown here (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
## with the alphabet and the leet numbers

LEET_DICT = {"a": "4",
             "b": "8",
             "c": "[",
             "d": ")",
             "e": "3",
             "f": "|=",
             "g": "6",
             "h": "#",
             "i": "1",
             "j": "_|",
             "k": "|<",
             "l": "1",
             "m": "|V|",
             "n": "^/",
             "o": "0",
             "p": "|*",
             "q": "9",
             "r": "|2",
             "s": "5",
             "t": "7",
             "u": "(_)",
             "v": "\/",
             "w": "VV",
             "x": "><",
             "y": "j",
             "z": "2",
             " ": " "}

def natural_to_hacker_language(text):
    list_text = list(text)

    hacker_text = "".join(list(map(lambda letter: LEET_DICT.get(letter.lower()), list_text)))

    print("Text converted to hacker_text -> ", hacker_text)

    return hacker_text

if __name__ == "__main__":
    text = input("Write here the text you want to get converted to hacker language: ")
    hacker_text = natural_to_hacker_language(text)