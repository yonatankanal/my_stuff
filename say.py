import cowsay
import sys

def main():
    what_to_say = input("What to say: ")
    who_to_say = input("Who to say: ").strip()
    who_can_say = ["cow", "trex", "dragon", "pig", "daemon", "ghostbusters", "cat", "dog", "mouse"]
    if who_to_say not in who_can_say:
        sys.exit(f"Please enter one of the following as who to say: {who_can_say}")
    if who_to_say == "cow":
        cowsay.cow(what_to_say)
    if who_to_say == "trex":
        cowsay.trex(what_to_say)
    if who_to_say == "dragon":
        cowsay.dragon(what_to_say)
    if who_to_say == "pig":
        cowsay.pig(what_to_say)
    if who_to_say == "daemon":
        cowsay.daemon(what_to_say)
    if who_to_say == "ghostbusters":
        cowsay.ghostbusters(what_to_say)

if __name__ == "__main__":
    main()