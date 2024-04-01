import re

def main():
    number = get_number()
    sigfigs = bad_zeroes(number)
    print(f"There are {sigfigs} sigfigs in {number}.")

def get_number():
    bad_number = True
    while bad_number:
        number = input("Number: ")
        if _ := re.search(r"^[0-9]+(\.[0-9]+)?$", number):
            break
        else:
            continue
    return number


def bad_zeroes(number):
    number = str(number)
    if "." in number:
        return len(number) - 1
    else:
        zeroes = 0
        for digit in number[::-1]:
            if digit != "0":
                break
            zeroes += 1
        return len(number)-zeroes

if __name__ == "__main__":
    main()