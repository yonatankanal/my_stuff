from datetime import date
import datetime
import re


def main():
    days_old, birthday,real_today,seconds_old = days_since_birthday()
    days_till_next_birthday = days_till_birthday(birthday,days_old,real_today)
    print(f"You are {days_old} days old.\nYou are apprx {'{:,}'.format(seconds_old)} seconds old.\nThere are {days_till_next_birthday} days until your next birthday.")

def days_since_birthday():
    bad_birthday = True
    today = date.today()
    while bad_birthday:
        birth_day = input("What is the date of the day you were born (YYYY-MM-DD)? ")
        if yes := re.search(r"(0[0-9]{3})|(1[0-9]{3})|(20[0-1][0-9])|(202[0-2])(?:-|/)(?:[0][0-9])|(?:[1][0-2])(?:-|/)(?:[0-2][0-9])|(?:3[0-1])", birth_day):
            bad_birthday = False
        else:
            print("Please enter the date in the correct format.")
            continue
    real_birthday = datetime.datetime.strptime(birth_day, "%Y-%m-%d")
    fake_today = datetime.datetime.strftime(today, "%Y-%m-%d")
    real_today = datetime.datetime.strptime(fake_today, "%Y-%m-%d")
    time_since_birth = real_today - real_birthday
    seconds_old = time_since_birth.days * 86400
    return time_since_birth.days,birth_day,real_today,seconds_old

def days_till_birthday(birthday,days_old,real_today):
    year,month,day = birthday.split("-")
    years_old = int((int(days_old) / 365))
    year = int(year) + years_old + 1
    next_birthday = datetime.datetime.strptime(f"{year}-{month}-{day}", "%Y-%m-%d")
    time_till_birthday = next_birthday - real_today
    return time_till_birthday.days


if __name__ == "__main__":
    main()