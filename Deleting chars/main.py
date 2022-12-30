## Create a function that gets two strings as parameters (str1, str2)
## and prints out 2 other string (out1, out2)
## - out1 will have all characters that are present in str1
##   but aren't in str2
## - out2 will have all characters that are present in str2
##   but aren't in str1
def delete_chars_lists(str1, str2):
    list1 = list(str1)
    list2 = list(str2)

    out1 = "".join([letter for letter in list1 if letter not in list2])
    out2 = "".join([letter for letter in list2 if letter not in list1])

    print("Out 1 -> ", out1)
    print("Out 2 -> ", out2)

def delete_chars_sets(str1, str2):
    set1 = set(str1)
    set2 = set(str2)

    out1 = set1 - set2
    out2 = set2 - set1
    print("Out 1 -> ", out1)
    print("Out 2 -> ", out2)

if __name__ == "__main__":
    print("Sets' approach -------------------")
    delete_chars_sets("abcde", "ubcopi")
    print("Lists' approach -------------------")
    delete_chars_lists("abcde", "ubcopi")