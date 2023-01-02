## Create a function that gets two arrays, a boolean; and returns an array
"""
- If the boolean is true, it'll look and return for the elements
  common to both arrays (and operation)
- If the boolean is false, it'll search for and return the elements
  that are different in both arrays (symmetric difference)
"""

def get_sets(arr1, arr2, and_operation):
    and_list = []
    sym_dif_list = []

    for i in arr1:
        for j in arr2:
            if i == j:
                and_list.append(i)

    if and_operation == True:
        return and_list
    else:
        arr3 = arr1 + arr2
        for i in arr3:
            found = False
            for j in and_list:
                if i == j:
                    found = True
            if found == False:
                sym_dif_list.append(i)

        return sym_dif_list
    

if __name__ == "__main__":
    arr1 = [2, 4, 6, 8, 10]
    arr2 = [1, 3, 6, 8, 11]

    new_list = get_sets(arr1, arr2, and_operation=True)

    print("New list -> ", new_list)