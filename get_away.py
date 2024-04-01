def main():
    name = get_good_name()
    what_to_print = format_string(name)
    print(what_to_print)


def get_good_name():
    good_name = True
    while good_name:
        name = input("What's your name? ")
        if name:
            return name
        continue


def format_string(name):
    for letter in name:
        if letter.isalpha() or letter.isspace():
            continue
        else:
            return f"You have a weird name {name}."
    if name.lower().strip() == "yoni":
        return "Welcome Master"
    elif name.lower().strip() == "yoni kanal":
        return "Welcome Master"
    elif name.lower().strip() == "yonatan":
        return "Welcome Master"
    elif name.lower().strip() == "yonatan kanal":
        return "Welcome Master"
    else:
        return f"{name.upper()} GET AWAY FROM MY COMPUTER!!!!!!!!!"

if __name__ == "__main__":
    main()