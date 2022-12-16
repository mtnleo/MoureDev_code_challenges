## Create a function that gets a text, and returns the most repeated vowel
## If vowel_count == 0, returns None

def count_most_repeated_vowel(text):
    text = text.lower()
    vowels = ("a", "e", "i", "o", "u")
    most_repeated = ["", 0]

    for vowel in vowels:
        count = text.count(vowel)
        if count > most_repeated[1]:
            most_repeated[0] = vowel
            most_repeated[1] = count

    return most_repeated

most_repeated = count_most_repeated_vowel(input("Write something: "))
print(most_repeated)