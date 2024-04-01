import random
import sys

def main():
    sport = which_sport()
    which_q = random.randint(1,2)
    if which_q == 1:
        specifics = facial_hair()
    else:
        specifics = winner_picker()
    player = which_player(sport,specifics)
    print(f"You are most like {player}.")

def which_sport():
    activity = input("Which do you like to do most in this list: \n1. Running\n2. Sitting on a couch\n3. Jumping/falling\n4. Hitting people.\n")
    if activity == "1":
        sport = input("Do you also like kicking a ball around (1) or do you just like running (2)? ")
        if sport == "1":
            sport = "1.1"
        if sport == "2":
            distance = input("Do you like running long (1), medium (2), or short (3)? ")
            sport = f"2.{distance}"
    elif activity ==  "2":
        list_o_insults = ["Get a life bozo!","Now that's just sad.","Stop being lazy and get on the court!","Buddy, you're fat and there's a reason","www.WeightWatchers.com: That should help."]
        number = random.randint(0,4)
        print(list_o_insults[number])
        sys.exit()
    elif activity  == "3":
        sport = input("Do you like falling down a mountain at high speeds (1) or trying to throw a ball through a circle many feet away (2)? ")
        if sport == "1":
            ski_or_snowboard = input("Would you prefer to do so on one (1) or two (2) sticks? ")
            if ski_or_snowboard == "1":
                sport = "3.1"
            elif ski_or_snowboard == "2":
                sport = "3.2"
        else:
            sport = "3.3"
    elif activity == "4":
        sport = input("Do you want to hit people wearing pads(1) or not wearing pads(2)? ")
        sport = f"4.{sport}"
    return sport

def winner_picker():
    Good_or_bad = input("Do you like players who are very good (1), very bad (2), or somewhere in the middle (3)? ")
    return f"1.{Good_or_bad}"

def facial_hair():
    facial_hair = input("What is your preferred type of facial hair: Big Beard (1), No facial hair (2), Goatee (3). ")
    return f"2.{facial_hair}"

def which_player(sport,specifics):
    if f"{sport}.{specifics}" == "1.1.1.1":
        return "Christiano Ronaldo
    if f"{sport}.{specifics}" == "1.1.1.2":
        print("Soccer player who's bad")
    if f"{sport}.{specifics}" == "1.1.1.3":
        return "Christian Pulisic"
    if f"{sport}.{specifics}" == "1.1.2.1":
        return "Olivier Giroud"
    if f"{sport}.{specifics}" == "1.1.2.2":
        print("Soccer player with no facial hair")
    if f"{sport}.{specifics}" == "1.1.2.3":
        print("Soccer player with a goatee")
    if f"{sport}.{specifics}" == "2.1.1.1":
        return "Usain Bolt"
    if f"{sport}.{specifics}" == "2.1.1.2":
        print("100m runner who's bad")
    if f"{sport}.{specifics}" == "2.1.1.3":
        print("100m runner who's medium")
    if f"{sport}.{specifics}" == "2.1.2.1":
        print("100m runner with big beard")
    if f"{sport}.{specifics}" == "2.1.2.2":
        print("100m runner with no facial hair")
    if f"{sport}.{specifics}" == "2.1.2.3":
        print("100m runner with goatee")
    if f"{sport}.{specifics}" == "2.2.1.1":
        print("1 mile runner who's good")
    if f"{sport}.{specifics}" == "2.2.1.2":
        print("1 mile runner who's medium")
    if f"{sport}.{specifics}" == "2.2.1.3":
        print("1 mile runner who's bad")
    if f"{sport}.{specifics}" == "2.2.2.1"
    if f"{sport}.{specifics}" == "2.2.2.2"
    if f"{sport}.{specifics}" == "2.2.2.3"
    if f"{sport}.{specifics}" == "2.3.1.1"
    if f"{sport}.{specifics}" == "2.3.1.2"
    if f"{sport}.{specifics}" == "2.3.1.3"
    if f"{sport}.{specifics}" == "2.3.2.1"
    if f"{sport}.{specifics}" == "2.3.2.2"
    if f"{sport}.{specifics}" == "2.3.2.3"
    if f"{sport}.{specifics}" == "3.1.1.1"
    if f"{sport}.{specifics}" == "3.1.1.2"
    if f"{sport}.{specifics}" == "3.1.1.3"
    if f"{sport}.{specifics}" == "3.1.2.1"
    if f"{sport}.{specifics}" == "3.1.2.2"
    if f"{sport}.{specifics}" == "3.1.2.3"
    if f"{sport}.{specifics}" == "3.2.1.1"
    if f"{sport}.{specifics}" == "3.2.1.2"
    if f"{sport}.{specifics}" == "3.2.1.3"
    if f"{sport}.{specifics}" == "3.2.2.1"
    if f"{sport}.{specifics}" == "3.2.2.2"
    if f"{sport}.{specifics}" == "3.2.2.3"
    if f"{sport}.{specifics}" == "3.3.1.1"
    if f"{sport}.{specifics}" == "3.3.1.2"
    if f"{sport}.{specifics}" == "3.3.1.3"
    if f"{sport}.{specifics}" == "3.3.2.1"
    if f"{sport}.{specifics}" == "3.3.2.2"
    if f"{sport}.{specifics}" == "3.3.2.3"

if __name__ == "__main__":
    main()