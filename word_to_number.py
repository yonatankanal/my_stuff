letters_and_numbers = {

    "zer": "0",
    "one": "1",
    "two": "2",
    "twe": "2",
    "thr": "3",
    "thi": "3",
    "fou": "4",
    "fiv": "5",
    "fif": "5",
    "six": "6",
    "sev": "7",
    "eig": "8",
    "nin": "9",
    "ten": "10",
    "ele": "11",

}


def main():
    word = get_word()
    if word == "twelve":
        number = "12"
    else:
        number = change_to_number(word)
    print(f"Output: {number}")


def get_word():
    word = input("Input: ")
    word = word.replace("-"," ").lower()
    return word


def change_to_number(phrase):
    build_word = "0000000000000000"
    words = phrase.split(" ")
    for word in words:
        if word == "twelve":
            build_word = f"{build_word[0:5]}12"
        elif word.endswith("teen"):
            build_word = f"{build_word[0:5]}1{letters_and_numbers[word[0:3]]}"
        elif word.endswith("ty"):
            build_word = f"{build_word[0:5]}{letters_and_numbers[word[0:3]]}0"
        elif word == "hundred":
            build_word = f"{build_word[0:4]}{build_word[6]}00"
        elif word == "thousand":
            build_word = f"{build_word[3:7]}000"
        elif word == "million":
            build_word = f"{8}"
        else:
            build_word = f"{build_word[0:6]}{letters_and_numbers[word[0:3]]}"
    return int(build_word)

if __name__ == "__main__":
    main()