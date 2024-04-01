import numpy as np
import datetime
from datetime import date
from pyluach import parshios,dates
import re
import yaml
import pprint

yaml.dump("tikun.yaml")
review_days = 6
days_per_week_learning = 6



list_o_parshios = {
    "Bereishis": [241, 19],
    "Noach": [230, 24],
    "Lech Lecha": [215, 12],
    "Va'eira": [255, 23],
    "Chayei Sarah": [170, 26],
    "Toldos": [173, 34],
    "Vayeitzei": [235, 23],
    "Vayishlach": [237, 18],
    "Vayeishev": [190, 20],
    "Mikeitz": [204, 24],
    "Vayigash": [179, 19],
    "Vayechi": [149, 26],
    "Shemos": [215, 22],
    "Vayeira": [222, 21],
    "Bo": [206, 24],
    "Beshalach": [216, 25],
    "Yisro": [138, 21],
    "Mishpatim": [185, 24],
    "Terumah": [155, 19],
    "Tetzaveh": [179, 27],
    "Ki Sisa": [245, 20],
    "Vayakhel": [211, 27],
    "Pekudei": [159, 27],
    "Vayakhel, Pekudei": [370, 27],
    "Vayikra": [215, 23],
    "Tzav": [170, 20],
    "Shemini": [157, 27],
    "Tazria": [128, 26],
    "Metzora": [159, 23],
    "Tazria, Metzora": [287, 26],
    "Acharei Mos": [154, 37],
    "Kedoshim": [109, 14],
    "Acharei Mos, Kedoshim":  [263, 37],
    "Emor": [215, 23],
    "Behar": [99, 24],
    "Bechukosai": [131, 17],
    "Behar, Bechukosai": [230, 24],
    "Bamidbar": [263, 21],
    "Nasso": [311, 32],
    "Beha'aloscha": [240, 22],
    "Shelach": [198, 21],
    "Korach": [184, 23],
    "Chukas": [159, 32],
    "Balak": [178, 23],
    "Chukas, Balak": [337, 32],
    "Pinchas": [280, 21],
    "Mattos": [190, 30],
    "Masei": [189, 16],
    "Mattos, Masei": [379, 30],
    "Devarim": [197, 22],
    "Va'eschanan": [250, 22],
    "Eikev": [232, 51],
    "Re'eh": [258, 36],
    "Shoftim": [192, 36],
    "Ki Seitzei": [213, 22],
    "Ki Savo": [261, 33],
    "Nitzavim": [72, 42],
    "Vayeilech": [112, 30],
    "Nitzavim, Vayeilech": [184, 42],
    "Haazinu": [92, 19],
    "Vezos Habracha": [70, 26],
}


def main():
    start_day = get_date()
    shabbasim = find_shabbos(start_day)
    parshios = which_parshios(shabbasim)
    parshios_and_lines = how_many_lines(parshios)
    lines_per_day = how_much_time(parshios_and_lines,start_day)
    print(make_string(lines_per_day))
    which_parsha,lines_known,start_line = lein_which_one(lines_per_day)
    what_to_print, parsha_dict = updated_lines(which_parsha,parshios,lines_known,start_line)
    print(what_to_print)
    cal,end_date = calendar(parsha_dict,start_day)
    print_cal(cal,end_date)


#Get the date that the person is starting to learn the parsha on (default is today's date)
def get_date():
    bad_date = True
    while bad_date:
        what_day = input("\nWhat day are you starting to learn the parsha? (YYYY-MM-DD) If you're starting today just hit ENTER: ")
        if what_day:
            try:
                what_day = datetime.datetime.strptime(what_day, "%Y-%m-%d")
                bad_date = False
            except ValueError:
                print("Please enter a date in the valid format.")
        else:
            what_day = date.today()
            break
    return what_day


# find the next 10 shabbasim for todays date
def find_shabbos(start_day):
    day_of_week = datetime.datetime.weekday(start_day)
    days_till_shabbos = 5 - day_of_week
    if days_till_shabbos > 0:
        first_shabbos = start_day + datetime.timedelta(days = days_till_shabbos)
    else:
        first_shabbos = start_day + datetime.timedelta(days = review_days)
    a_shabbos = {"date": first_shabbos}
    all_shabbasim = [a_shabbos]
    i = 0
    while i < 9:
        first_shabbos = first_shabbos + datetime.timedelta(days = 7)
        a_shabbos = {"date": first_shabbos}
        all_shabbasim.append(a_shabbos)
        i += 1
    return all_shabbasim


#find which parshios are on those ten shabbasos
def which_parshios(shabbasim):
    i = 0
    parshios_and_dates = []
    for _ in shabbasim:
        shabbos_date = shabbasim[i]["date"]
        shabbos_date = datetime.datetime.strftime(shabbos_date, "%Y-%m-%d")
        year,month,day = shabbos_date.split("-")
        hebrew_shabbos_date = dates.GregorianDate(int(year),int(month),int(day))
        parsha = parshios.getparsha_string(hebrew_shabbos_date, israel = False)
        a_parsha = {"name": parsha,"date": shabbos_date}
        parshios_and_dates.append(a_parsha)
        i += 1
    return parshios_and_dates


#Reference dictionary at top to find lines per parsha
def how_many_lines(parshios):
    i = 0
    for _ in parshios:
        if parshios[i]["name"] in list_o_parshios.keys():
            lines = list_o_parshios[parshios[i]["name"]][0]
            parshios[i]["lines"] = lines
        else:
            if parshios[i]["name"]:
                raise ValueError(f"{parshios[i]['name']} is not in list_o_parhios. Check spelling.")
            else:
                parshios[i]["lines"] = "This Shabbos is a Yom Tov and therefore there is not a parsha for this date.\n"
        i += 1

    return parshios


def how_much_time(parshios,start_day):
    i = 0
    for _ in parshios:
        parsha_date = datetime.datetime.strptime(parshios[i]["date"], "%Y-%m-%d")
        today = datetime.date.strftime(start_day, "%Y-%m-%d")
        real_today = datetime.datetime.strptime(today, "%Y-%m-%d")
        days_till_parsha = parsha_date - real_today
        days_to_learn = days_till_parsha - datetime.timedelta(days = (i * (7-days_per_week_learning) + 6))
        parshios[i]["days to learn"] = days_to_learn.days
        try:
            if days_to_learn.days > 0:
                lines_per_day = np.round_(parshios[i]["lines"] / days_to_learn.days, decimals = 1)
            else:
                lines_per_day = "too many"
            parshios[i]["lines per day"] = lines_per_day
        except TypeError:
            parshios[i]["lines per day"] = "N/A"
        i += 1

    return parshios


def make_string(parshios):
    i = 0
    what_to_print = "\n"
    for _ in parshios:
        if parshios[i]["lines per day"] == "too many":
            if parshios[i]["name"] != None:
                what_to_print += f"There is not enough time to learn {parshios[i]['name']}\n"
            else:
                what_to_print += "This Shabbos is a Yom Tov and therefore there is not a parsha for this date.\n"
        else:
            if parshios[i]["lines per day"] == "N/A":
                what_to_print += parshios[i]["lines"]
            else:
                what_to_print += f"To learn {parshios[i]['name']} you will have to learn {parshios[i]['lines per day']} lines per day.\n"
        i += 1
    return what_to_print


def lein_which_one(parshios):

    available_parshios= []
    for dict in parshios:
        parsha = dict["name"]
        available_parshios.append(parsha)

    which_parsha = ""
    while which_parsha not in available_parshios:
        which_parsha = input("Which parsha do you want to learn (case sensitive)? ")
        if which_parsha not in available_parshios:
            print("Please select one of the parshios in the list above.")

    lines_known = input(f"\nHow many lines (enter a number) have you already learned for {which_parsha} (rishon contains {list_o_parshios[which_parsha][1]} lines)? ")

    start_line = 0
    if lines_known:
        start_line = (int(lines_known) + 1)
    else:
        lines_known = 0

    return which_parsha,lines_known,start_line


def updated_lines(which_parsha,parshios,lines_known,start_line):
    for parsha in parshios:
        if parsha["name"] == which_parsha:
            parsha_dict = dict(parsha)
    if lines_known != 0 and lines_known != None:
        place_holder = input("\nHow many days would you like to review what you have already learned? ")
        review_days = place_holder
    else:
        review_days = 0
    parsha_dict["review days"] = int(review_days)
    parsha_dict["lines known"] = int(lines_known)
    lines_to_learn = int(list_o_parshios[which_parsha][0]) - int(lines_known)
    days_left = parsha_dict["days to learn"] - int(review_days)
    lines_per_day = np.round_(lines_to_learn / days_left, decimals = 1)
    parsha_dict["lines per day"] = lines_per_day
    what_to_print = f"\nTo learn {parsha_dict['name']} you will have to learn {parsha_dict['lines per day']} lines per day."

    parsha_dict["start line"] = start_line

    return what_to_print, parsha_dict


def calendar(parsha_dict,start_day):
    #Find the Sunday before the start day
    Sunday_before = start_day.day - start_day.weekday() - 1

    Sundays_date = start_day.replace(day = Sunday_before)
    year,month,day = parsha_dict["date"].split("-")
    end_date = (f"{month}-{day}")

    date_nums = get_date_info(parsha_dict,start_day,Sundays_date,end_date)

    return date_nums,end_date


def get_date_info(parsha_dict,start_day,Sundays_date,end_date):

    start_line = parsha_dict["start line"]

    date_nums = {}
    review = False
    if parsha_dict["start line"]:
        start_end = [start_line,(start_line + np.round(parsha_dict["lines per day"], decimals = 1))]
    else:
        start_end = [0,np.round(parsha_dict["lines per day"], decimals = 1)]
    i = 0

    while str(f"0{Sundays_date.month}-{Sundays_date.day}") != str(end_date):
        if i >= (start_day.weekday() + 1):
            if ((i-6)%7) == 0 or review == True:
                date_nums[f"{Sundays_date.month}/{Sundays_date.day}"] = "Review"
            else:
                date_nums[f"{Sundays_date.month}/{Sundays_date.day}"] = [int(start_end[0]),int(start_end[1])]
                if start_end[1] + parsha_dict["lines per day"] <= parsha_dict["lines"]:
                    start_end[0] += parsha_dict["lines per day"]
                    start_end[1] += parsha_dict["lines per day"]
                else:
                    start_end[0] = start_end[1]
                    start_end[1] = parsha_dict["lines"]
                    date_nums[f"{Sundays_date.month}/{Sundays_date.day}"] = [int(start_end[0]),int(start_end[1])]
                    review = True
        else:
            date_nums[f"{Sundays_date.month}/{Sundays_date.day}"] = "Nothing"
        Sundays_date += datetime.timedelta(days = 1)
        i += 1
    date_nums[f"{Sundays_date.month}/{Sundays_date.day}"] = "GL"

    return date_nums


def print_cal(cal_array,end_date):

    day_of_week = 0
    for day in cal_array:
        if day_of_week % 7 == 0:
            print("\n ---------------- ---------------- ---------------- ---------------- ---------------- ---------------- ----------------")
            print("|", end = "")
        items = list(cal_array.items())
        spaces_to_add = 17 - len(f' {day} ({items[day_of_week][1][0]}-{items[day_of_week][1][1]}) |')
        if items[day_of_week] != "Review":
            print(f' {day} ({items[day_of_week][1][0]}-{items[day_of_week][1][1]}) {" " * spaces_to_add}|', end='')
        else:
            print(f"{day} (items[day_of_week])")
        day_of_week += 1
    while day_of_week % 7 != 0:
        print("                |",end = "")
        day_of_week += 1

    print("\n ---------------- ---------------- ---------------- ---------------- ---------------- ---------------- ----------------")


if __name__ == "__main__":
    main()