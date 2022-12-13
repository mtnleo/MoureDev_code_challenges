## Create a function that's capable of encrypting and decrypting text using
## Karaca's encryption algorithm

## Step 1: Reverse the input.
## Step 2: Replace all vowels using this structure: {a: 0, e: 1, i: 2, o: 2, u: 3}
## Step 3: Add "aca" to the end of the word

encrypt_dict = {"a": "0", "e": "1", "i": "2", "o": "2", "u": "3"}

def revert_string(text):
    text = list(text)
    i = 0
    j = -1
    while i < int(len(text) / 2):
        aux = text[i]
        text[i] = text[j]
        text[j] = aux

        i += 1
        j -= 1

    new_text = ""
    new_text = new_text.join([letter for letter in text])
    return new_text

def modify_string_by_dict(text):
    length = len(text)
    text = list(text)
    i = 0

    while i < length:
        if text[i] in encrypt_dict:
            text[i] = encrypt_dict[text[i]]
        i += 1

    new_text = ""
    new_text = new_text.join([letter for letter in text])
    return new_text
    


def encryption(text):
    # lowercase text
    text = text.casefold()
    print("Lowercase -> ", text)
    # revert string
    text = revert_string(text)
    print("Revert -> ", text)
    # replace vowels
    text = modify_string_by_dict(text)
    print("Replace with dict -> ", text)
    # add "aca" to the end
    text  = text + "aca"
    print("Add 'aca' -> ", text)

    return text



if __name__ == "__main__":
    text = "apple"
    print(encryption(text))