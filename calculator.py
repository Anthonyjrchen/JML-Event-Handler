import datetime

'''
CALCULATOR HOLIDAYS SETUP
'''
list_of_holidays = []
file = open("holidays.txt", "r")
file_data = file.read()
raw_dates = file_data.split("\n")
for date in raw_dates:
    list_of_holidays.append(datetime.date(int(date[0:4]),int(date[5:7]),int(date[8:10])))

def calculate_dates(in_year,in_month,in_day):
    return_dates = {}
    months = {
        "January": '01',
        "February": '02',
        "March": '03',
        "April": '04',
        "May": '05',
        "June": '06',
        "July": '07',
        "August": '08',
        "September": '09',
        "October": '10',
        "November": '11',
        "December": '12',
    }
    month = months[in_month]
    date = datetime.date(int(in_year),int(month), int(in_day))
    date1 = shiftDates(date - datetime.timedelta(days=121))
    date2 = shiftDates(date - datetime.timedelta(days=85))
    date3 = shiftDates(date - datetime.timedelta(days=61))
    date4 = shiftDates(date - datetime.timedelta(days=57))
    date5 = shiftDates(date - datetime.timedelta(days=50))
    date6 = shiftDates(date - datetime.timedelta(days=46))
    date7 = shiftDates(date - datetime.timedelta(days=43))
    date8 = shiftDates(date - datetime.timedelta(days=29))
    date9 = shiftDates(date - datetime.timedelta(days=22))
    date10 = shiftDates(date - datetime.timedelta(days=15))
    date11 = shiftDates(date - datetime.timedelta(days=15))
    date12 = shiftDates(date - datetime.timedelta(days=8))
    date13 = shiftDates(date - datetime.timedelta(days=8))
    date14 = shiftDates(date - datetime.timedelta(days=3))
    return_dates["date1"]= date1
    return_dates["date2"]= date2
    return_dates["date3"]= date3
    return_dates["date4"]= date4
    return_dates["date5"]= date5
    return_dates["date6"]= date6
    return_dates["date7"]= date7
    return_dates["date8"]= date8
    return_dates["date9"]= date9
    return_dates["date10"]= date10
    return_dates["date11"]= date11
    return_dates["date12"]= date12
    return_dates["date13"]= date13
    return_dates["date14"]= date14

    return return_dates

def shiftDates(date):
    if date.weekday()>=5 or date in list_of_holidays:
        while date.weekday()>=5 or date in list_of_holidays:
            date = date - datetime.timedelta(days=1)
    return date