## Create a function that prints the next 30 leap-years
## from the one given

def calculate_leap_years(given_year):
    year = given_year / 4
    year = year - int(year) # to get only the decimal part

    if year == 0.25:
        given_year += 3
    elif year == 0.5:
        given_year += 2
    elif year == 0.75:
        given_year += 1
    else:
        given_year += 4

    for i in range(0, 30):
            print(f"{i + 1} -> {given_year}")
            given_year += 4


if __name__ == "__main__":
    calculate_leap_years(int(input("Select your starting year: ")))