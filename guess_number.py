def main():
    criteria()
    print("Thank you for playing!")

def criteria():
    print("You are thinking of a number between (min) and (max). Both must be positive integers.")
    min = int(input("Minimum number: "))
    max = int(input("Maximum number: ")) + 1
    wrong = True
    while wrong:
        truth, number = guess(min, max)
        if truth.lower() == "yes":
            wrong = False
        elif truth.lower() == "higher":
            min = number
        elif truth.lower() == "lower":
            max = number

def guess(min, max):
    number = int((min + max) / 2)
    truth = input(f"Is {number} your number (write 'yes', 'higher', or 'lower')? ")
    return truth, number

if __name__ == "__main__":
    main()