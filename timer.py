from datetime import date
from datetime import datetime
from datetime import timedelta
import numpy
import time


def main():
    inspection()
    timer()

def inspection():
    number = 0
    while number <= 15:
        print(f"\r{number}", end="")
        time.sleep(1)
        number += 1
        if not input():
            continue
        else:
            break
    print("\n")

def timer():
    start = input("Press enter to start: ")
    tic = datetime.now()

    end = input("Press enter to end: ")
    toc = datetime.now()
    duration = toc - tic


    minutes = int(duration.total_seconds() // 60)
    seconds = str(duration.seconds).zfill(2)
    microseconds = round(duration.microseconds / 1000)

    what_to_print = f"{int(minutes)}:{seconds}.{microseconds}"

    print(what_to_print)

    with open("Rubiks_times.csv", "a") as file:
        file.write(f"{date.today()},{what_to_print}\n")


if __name__ == '__main__':
    main()