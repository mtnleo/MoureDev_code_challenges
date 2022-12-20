## Create a function that gets text as a parameter, and shows one word each line,
## creating an asterisk frame for the whole text
"""  'This is the challenge cool would look like'
 *************
 * This      *
 * is        *
 * the       *
 * challenge *
 * cool      *
 *************
 """

def print_frame_text(spaced_words, longest_word):
    print("*" * (longest_word + 5)) #prints the asterisk line, adding up 5 more for the frame distance
    for word in spaced_words:
        print("*", word)
    print("*" * (longest_word + 5)) #prints the asterisk line, adding up 5 more for the frame distance

def frame_text(text):
    text = text.split(" ")
    longest_word = 0

    for word in text: #check for the longest word
        if len(word) > longest_word:
            longest_word = len(word)

    spaced_words = list(map(lambda word: word + (" " * ((longest_word + 1) - len(word)) + "*"), text))
    print(spaced_words)

    print_frame_text(spaced_words, longest_word)


if __name__ == "__main__":
    to_frame_text = input("Write a text to frame: ")
    frame_text(to_frame_text)