## Create a function that gets a binary number (int)
## and returns its decimal value

def bin_to_dec(bin_num):
    bin_num = str(bin_num)
    bin_num_list = [num for num in bin_num] # make it a list

    i = len(bin_num_list) - 1 # get the power of the numbers
    dec_num = 0

    for number in bin_num_list:
        dec_num = dec_num + int(number) * (2 ** i)
        i -= 1

    return dec_num


if __name__ == "__main__":
    bin_num = int(input("Write a binary number to convert to decimal: "))
    dec_num = bin_to_dec(bin_num)
    print("In binary -> ", bin_num, "\nIn decimal -> ", dec_num)