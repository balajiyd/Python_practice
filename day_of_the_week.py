from datetime import datetime

def day_of_the_week(date_str):
    try:
        date_object = datetime.strptime(date_str, "%d/%m/%Y" )

        day_of_week = date_object.weekday()

        days_of_week = ["monday", "tuesday", "Wednesday", "Thrusday", "Friday", "saturday", "Sunday"]

        print(f"The day of the week for{date_str} is {days_of_week[day_of_week]}")

    except ValueError:
        print('Invalid>>')

date_input = input("Enter DD/MM/YYYY")
day_of_the_week(date_input)
