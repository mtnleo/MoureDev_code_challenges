## Create a function that's capable of encrypting and decrypting text using
## Karaca's encryption algorithm

## Step 1: Reverse the input.
## Step 2: Replace all vowels using this structure: {a: 0, e: 1, i: 2, o: 2, u: 3}
## Step 3: Add "aca" to the end of the word

class karaca:
    encrypt_dict = {"a": "0", "e": "1", "i": "2", "o": "2", "u": "3"}

    def __init__(self, text):
        self.text = text


    def _reverse_string(text):
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

    def _modify_string_by_dict(text, dict = encrypt_dict):
        length = len(text)
        text = list(text)
        i = 0

        while i < length:
            if text[i] in dict:
                text[i] = dict[text[i]]
            i += 1

        new_text = ""
        new_text = new_text.join([letter for letter in text])
        return new_text

    def _modify_string_by_dict_dec(text):
        dict_list = karaca.encrypt_dict.items()
        decrypt_dict = {value: key for key, value in dict_list}
        return karaca._modify_string_by_dict(text, decrypt_dict)
    
    def encryption(self):
        # lowercase text
        text = self.text.casefold()
        # reverse string
        text = karaca._reverse_string(text)
        # replace vowels
        text = karaca._modify_string_by_dict(text)
        # add "aca" to the end
        text  = text + "aca"

        return text

    def decryption(self):
        # get rid of "aca"
        text = self.text[:-3]
        # get the modified string
        text = karaca._modify_string_by_dict_dec(text)
        # reverse string
        text = karaca._reverse_string(text)

        return text




if __name__ == "__main__":
    text = input("Write a word to encrypt: ")
    kar = karaca(text)
    encrypted_text = kar.encryption()
    print("Encrypted text -> ", encrypted_text)
    kar_d = karaca(encrypted_text)
    decrypted_text = kar_d.decryption()
    print("Decrypted text -> ", decrypted_text)