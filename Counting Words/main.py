## Create a function that counts how many times a word is repeated
## in the given text
## You can't use language's own funcs that automatically solve it

def count_words_in_text(text):
    words_count = {}
    words = text.lower().split(" ")

    for word in words:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count.update({word: 1})

    return words_count

if __name__ == "__main__":
    words_count = count_words_in_text(input("Input text: "))
    print(words_count)