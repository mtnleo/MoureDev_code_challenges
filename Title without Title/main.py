## Create a function that does the exact same thing as Title()
## without using it

def title_v2(text):
    text = text.split(" ")

    for i in range(0, len(text) - 1):
        word = text[i]
        word = word[0].upper() + word[1:]
        text[i] = word

    new_text = " ".join(text)

    return new_text

if __name__ == "__main__":

    new_text = title_v2(input("Write your text to be titled here: "))
    print(new_text)


