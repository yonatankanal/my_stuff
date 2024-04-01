def main():
    correct_answers = questions()
    line = do_you_know_me(correct_answers)
    print(line)


def questions():
    correct_answers = 0

    guess = input("What is my favorite color? green (1) yellow (2) blue (3) pink (4) ")
    if guess == "3":
        correct_answers += 1

    guess = input("How many siblings do I have? ")
    if guess == "4":
        correct_answers += 1

    guess = input("What year am I planning on graduating high school? ")
    if guess == "2024":
        correct_answers += 1

    guess = input("What is the most points I've scored in a HS Bball game? 7 (1). 11 (2). 15 (3). 19 (4)")
    if guess == "3":
        correct_answers += 1

    guess = input("What month is my birthday in? (1 = Jan, 2 = Feb, 3 = Mar, etc..) ")
    if guess == "5":
        correct_answers += 1

    guess = input("Chocolate (1) or Vanilla (2)?")
    if guess  == "2":
        correct_answers += 1

    guess = input("What is my middle name?")
    if guess.lower() == "uziel":
        correct_answers += 1

    return correct_answers

def do_you_know_me(correct_answers):
    if correct_answers == 0:
        return "0/7. You don't know me at all. Sorry. You failed."
    elif correct_answers == 1:
        return "1/7. You barely know me. I don't think I could consider you my friend."
    elif correct_answers == 2:
        return "2/7. Eh. Work on it."
    elif correct_answers == 3:
        return "3/7. You did okay but I would barely consider you my friend."
    elif correct_answers == 4:
        return "4/7. You're at that point where I may talk to you, but only to say 'good morning'."
    elif correct_answers == 5:
        return "5/7. Not bad. Could've been better but I can't really complain."
    elif correct_answers == 6:
        return "6/7. Pretty good! Not perfect but I respect the hard effort."
    elif correct_answers == 7:
        return "7/7. You are a true friend! You have officially earned my friendship!"

if __name__ == "__main__":
    main()