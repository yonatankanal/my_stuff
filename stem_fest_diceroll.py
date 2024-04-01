import random as r

def main():
    number = how_many()
    numbers, percentages = roll_die(number)
    string = show_results(numbers,percentages)
    print(string)

def how_many():
    while True:
        number = input("How many times should the die be rolled? ")
        try:
            return int(number)
        except ValueError:
            continue

def roll_die(number):
    numbers = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        }
    for _ in range (number):
        num = r.randint(1,6)
        numbers[num] += 1
    percentages = {
        1: round(numbers[1]/number*100, 2),
        2: round(numbers[2]/number*100, 2),
        3: round(numbers[3]/number*100, 2),
        4: round(numbers[4]/number*100, 2),
        5: round(numbers[5]/number*100, 2),
        6: round(numbers[6]/number*100, 2),
    }

    return numbers, percentages

def show_results(numbers,percentages):
    string = "\n"
    i = 1
    for _ in range (6):
        string += f"{i} was rolled {numbers[i]} times to make up {percentages[i]}% of the rolls.\n"
        i += 1
    return string


if __name__ == "__main__":
    main()