"""

DAY  = 24 hours
HOUR = 1080 chalakim
MONTH = 29 days 12 hours 793 chalakim (from beg of night of day thirty)
A NORMAL year is 354 days 8 hours 876 chalakim
A MEUBAR year is 383 days 21 hours 589 chalakim
SOLAR year is 365 day six hours (maybe slightly less)
The FIRST MOLAD was Monday (2 days) 5 hours 204 chalakim
After the four weeks in lunar MONTH, the LEFTOVER is 1 day 12 hours 793 chalakim
After NORMAL LUNAR YEAR the LEFTOVER is 4 days 8 hours 876 chalakim
After MEUBAR LUNAR YEAR the LEFTOVER is 5 days 21 hours 589 chalakim
The LEFTOVER from MACHZOR is 2 days 16 hours 595 chalakim
MEUBAR year in MACHZOR are 3, 6, 8, 11, 14, 17, 19

"""

import pprint
import re


def main():
    start,end = start_and_end()
    dates = get_dates(start,end)
    new_dates = find_first_molad(dates)
    if len(dates) > 1:
        new_dates = find_all_molads(new_dates)
    year_to_letters(new_dates)
    new_dates = number_to_day(new_dates)
    print_all_molads(new_dates)


def chalakim_adder(first,second):
    # Set the default amount to one
    days,hours,chalakim,amount = first
    days2,hours2,chalakim2,amount2 = second
    total_chalakim = amount*(chalakim + 1080*hours + 25920*days) + amount2*(chalakim2 + 1080*hours2 + 25920*days2)

    final_days = int(total_chalakim / 25920)
    final_hours = int((total_chalakim - final_days * 25920) / 1080)
    final_chalakim = total_chalakim - (final_days * 25920 + final_hours * 1080)

    return [final_days % 7, final_hours, final_chalakim]


def get_dates(start,end):
    # Convert all the variables from strings to integers
    start_year,start_month = start.split(",")
    end_year,end_month = end.split(",")
    info = [start_year,start_month,end_year,end_month]
    info = [int(i) for i in info]
    start_year,start_month,end_year,end_month = info

    # Make a list of every month in the given range
    holder_year = start_year
    holder_month = start_month
    months = []
    while holder_year < end_year:
        while holder_month <= months_in_year(holder_year):
            months.append({"Year":holder_year,"Month":holder_month})
            holder_month += 1
        holder_year += 1
        holder_month = 1
    while holder_month <= end_month:
        months.append({"Year":holder_year,"Month":holder_month})
        holder_month += 1

    return months


def start_and_end():
  # Get the dates the user wants the molad for
    bad_start = True
    while bad_start:
        # Get the first date
        start = input("Input the start year and month (year,month number) --> ")

        # Verify the first date
        if start:
            if _ := re.fullmatch(r"^[1-9][0-9]{0,3},[0-9]|(1[0123])$",start):
                bad_start = False
            else:
                print("Please input a date in the proper format.")
        else:
            # Set the date equal to the current date
            # start = <script src="https://www.hebcal.com/etc/hdate-en.js" crossorigin="anonymous">
            #         </script>
            ...
    bad_end = True
    while bad_end:
        # Get end date
        end = input("Input the end year and month (year,month number) --> ")
        if end:
            if _ := re.fullmatch(r"^[1-9][0-9]{0,3},[0-9]|(1[0123])$",end):
                bad_end = False
            else:
                print("Please input a date in the proper format.")
        else:
            # Set the date equal to the current date
            # start = <script src="https://www.hebcal.com/etc/hdate-en.js" crossorigin="anonymous">
            #         </script>
            ...
    return start,end


def months_in_year(year):
    year_in_machzor = year % 19
    months_per_year = {
        0: 13, 1:12, 2:12, 3:13, 4:12, 5:12, 6:13, 7:12, 8:13, 9:12, 10:12, 11:13, 12:12, 13:12, 14:13, 15:12, 16:12, 17:13, 18:12
        }
    return months_per_year[year_in_machzor]


def find_first_molad(dates):
    # Find the total machzorim extra and add it to the time of the first molad
    completed_machzorim = int(dates[0]["Year"] / 19)
    first = [2,5,204,1]
    second = [2,16,595,completed_machzorim]
    fir_a_mac = chalakim_adder(first,second)

    # Find the extra from the previous years in that machzor
    years_into_machzor = dates[0]["Year"] % 19
    i = 1
    years_extra = [0,0,0,1]
    extra_per_year = {12:[4,8,876,1],13:[5,21,589,1]}
    while i < years_into_machzor:
        years_extra = chalakim_adder(years_extra,extra_per_year[months_in_year(i)])
        years_extra.append(1)
        i += 1
    mac_a_yer = chalakim_adder([fir_a_mac[0],fir_a_mac[1],fir_a_mac[2],1],[years_extra[0],years_extra[1],years_extra[2],1])

    # Find the extra from the previous months in that year
    previous_months = dates[0]["Month"] - 1
    mon_ext = chalakim_adder([0,0,0,1],[1,12,793,previous_months])
    extra_in_all = chalakim_adder([mon_ext[0],mon_ext[1],mon_ext[2],1],[mac_a_yer[0],mac_a_yer[1],mac_a_yer[2],1])

    dates[0]["Molad"] = extra_in_all

    return dates


def find_all_molads(dates):
    # Find the molad for every month
    molad = dates[0]["Molad"]
    i = 1
    while i < len(dates):
        molad = chalakim_adder([molad[0],molad[1],molad[2],1],[1,12,793,1])
        dates[i]["Molad"] = molad
        i += 1
    # Turn the molad into hours, minutes, and seconds
    dates = numbers_to_times(dates)
    pprint.pprint(dates)
    return dates


def numbers_to_times(dates):
    for i in dates:
        days,hours,chalakim = i["Molad"]
        total_chalakim = days*25920 + hours*1080 + chalakim
        days = int(total_chalakim/25920)
        hours = int((total_chalakim - days*25920)/1080)
        minutes = int((total_chalakim - days*25920 - hours*1080)/18)
        chalakim = (total_chalakim - days*25920 - hours*1080 - minutes*18)
        if hours < 6:
            days = (days-1)%7
            hours += 18
        else:
            hours -= 6
        if hours < 12:
            i["Meridiem"] = "AM"
        elif hours == 12:
            i["Meridiem"] = "PM"
        else:
            i["Meridiem"] = "PM"
            hours -= 12
        i["Molad"] = [days,hours,minutes,chalakim]

    return dates


def year_to_letters(dates):
    for date in dates:
        number_year = date["Year"]
        letter_year = ""
        letter_year = hebrew_date(number_year)
        date["Letter Year"] = letter_year
    print("This is what dates looks like after adding letter year.")


def hebrew_date(year: int):
    if year == 0:
        return ""
    list_o_values = (("י'",10000),("ט'",9000),("ח'",8000),("ז'",7000),("ו'",6000),("ה'",5000),("ד'",4000),("ג'",3000),("ב'",2000),("א'",1000),("ת",400),("ש",300),("ר",200),("ק",100),("צ",90),("פ",80),("ע",70),("ס",60),("נ",50),("מ",40),("ל",30),("כ",20),("י",10),("ט",9),("ח",8),("ז",7),("ו",6),("ה",5),("ד",4),("ג",3),("ב",2),("א",1))
    i = 0
    while year < list_o_values[i][1]:
        i += 1
    letter = list_o_values[i][0]
    if year > 0:
        return (letter + hebrew_date(year - list_o_values[i][1]))



def number_to_day(dates):
    numbers_and_days = {0:"Shabbos",1:"Sunday",2:"Monday",3:"Tuesday",4:"Wednesday",5:"Thursday",6:"Friday"}
    for i in dates:f
        i["Molad"][0] = numbers_and_days[i["Molad"][0]]

    return dates


def print_all_molads(dates):
    Peshuta_date_number_to_hebrew_name = {1:"תשרי", 2:"חשון", 3:"כסלו", 4:"טבת", 5:"שבט",6:"אדר", 7:"ניסן", 8:"אייר", 9:"סיון", 10:"תמוז", 11:"אב",12:"אלול"}
    Meubar_date_number_to_hebrew_name = {1:"תשרי", 2:"חשון", 3:"כסלו", 4:"טבת", 5:"שבט", 6:"אדר א", 7:"אדר ב", 8:"ניסן", 9:"אייר", 10:"סיון", 11:"תמוז", 12:"אב",13:"אלול"}
    for i in dates:
        if months_in_year(i["Year"]) == 12:
            print(f"The Molad for {Peshuta_date_number_to_hebrew_name[i['Month']]} {i['Letter Year']} is {i['Molad'][0]} at {i['Molad'][1]}:{str(i['Molad'][2]).zfill(2)} {i['Meridiem']} and {i['Molad'][3]} chalakim.")
        elif months_in_year(i["Year"]) == 13:
            print(f"The Molad for {Meubar_date_number_to_hebrew_name[i['Month']]} {i['Letter Year']} is {i['Molad'][0]} at {i['Molad'][1]}:{str(i['Molad'][2]).zfill(2)} {i['Meridiem']} and {i['Molad'][3]} chalakim.")




if __name__ == "__main__":
    main()