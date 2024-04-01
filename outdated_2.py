def main():
    invalid_date = True
    while invalid_date:
        my_date = get_date()
        formatted_date = format_date(my_date)
        invalid_date = is_valid_date(formatted_date)
    print(formatted_date)


def get_date():
    while True:
        date = input("Date (month/day/year): ")
        try:
          month,day,year = date.split("/")
        except ValueError:
            try:
                month,day,year = date.replace(",","").split(" ")
                month = month.title()
            except (KeyError, ValueError):
                continue
        return (month,day,year)


def format_date(users_date):
    month,day,year = users_date
    if month.isalpha():
        month_numbers = {"January": "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12"}
        month = month_numbers[month]
        return (f"{day}-{month}-{year}")
    else:
        if len(month) == 1:
            month = "0" + month
        if len(day) == 1:
            day = "0" + day
        return (f"{day}-{month}-{year}")


def is_valid_date(any_date):
    month,day,year = any_date.split("-")
    if int(month) < 1 or 12 < int(month) or int(day) < 1 or 31 < int(day) or int(year) < 0 or 2022 < int(year):
        return True
    else:
        return False


main()