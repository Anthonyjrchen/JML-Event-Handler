import datetime
from dateutil.relativedelta import *

'''
CALCULATOR HOLIDAYS SETUP
'''
list_of_holidays = []
file = open("holidays.txt", "r")
file_data = file.read()
raw_dates = file_data.split("\n")
for date in raw_dates:
    list_of_holidays.append(datetime.date(int(date[0:4]),int(date[5:7]),int(date[8:10])))

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
months2 = {
    "1": 'Jan',
    "2": 'Feb',
    "3": 'Mar',
    "4": 'Apr',
    "5": 'May',
    "6": 'Jun',
    "7": 'Jul',
    "8": 'Aug',
    "9": 'Sep',
    "10": 'Oct',
    "11": 'Nov',
    "12": 'Dec',
}

def calculate_dates(in_year,in_month,in_day):
    return_dates = {}
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
    # this is minuses the days from the trial date, then sees if it is a weekend or holiday then keeps shifting backwards until it isnt. ( this is correct for most besides notice to produce and the reminders for notice of objection)
    # notice to produce finds 3 WORKDAYS before the trial date

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
    return_dates["rm1_date1"] = shiftDates(date1 - relativedelta(months=1))
    return_dates["rm2_date1"] = shiftDates(date1 - datetime.timedelta(weeks=2))
    return_dates["rm3_date1"] = shiftDates(date1 - datetime.timedelta(weeks=1))
    return_dates["rm4_date1"] = shiftDates(date1 - datetime.timedelta(days=1))

    return_dates["rm1_date2"] = shiftDates(date2 - relativedelta(months=1))
    return_dates["rm2_date2"] = shiftDates(date2 - datetime.timedelta(weeks=2))
    return_dates["rm3_date2"] = shiftDates(date2 - datetime.timedelta(weeks=1))
    return_dates["rm4_date2"] = shiftDates(date2 - datetime.timedelta(days=1))

    return_dates["rm1_date3"] = shiftDates(date3 - relativedelta(months=2))
    return_dates["rm2_date3"] = shiftDates(date3 - relativedelta(months=1))
    return_dates["rm3_date3"] = shiftDates(date3 - datetime.timedelta(weeks=2))
    return_dates["rm4_date3"] = shiftDates(date3 - datetime.timedelta(weeks=1))
    return_dates["rm5_date3"] = shiftDates(date3 - datetime.timedelta(days=1))

    return_dates["rm1_date4"] = shiftDates(date4 - relativedelta(months=1))
    return_dates["rm2_date4"] = shiftDates(date4 - datetime.timedelta(weeks=1))

    return_dates["rm3_date5"] = shiftDates(date5 - relativedelta(months=1))
    return_dates["rm4_date5"] = shiftDates(date5 - datetime.timedelta(weeks=1))

    return_dates["rm1_date6"] = shiftDates(date6 - relativedelta(months=1))
    return_dates["rm2_date6"] = shiftDates(date6 - datetime.timedelta(weeks=2))
    return_dates["rm3_date6"] = shiftDates(date6 - datetime.timedelta(weeks=1))
    return_dates["rm4_date6"] = shiftDates(date6 - datetime.timedelta(days=1))

    return_dates["rm1_date7"] = shiftDates(date7 - relativedelta(months=1))
    return_dates["rm2_date7"] = shiftDates(date7 - datetime.timedelta(weeks=2))
    return_dates["rm3_date7"] = shiftDates(date7 - datetime.timedelta(weeks=1))
    return_dates["rm4_date7"] = shiftDates(date7 - datetime.timedelta(days=1))

    return_dates["rm1_date8"] = shiftDates(date8 - relativedelta(months=4))
    return_dates["rm2_date8"] = shiftDates(date8 - relativedelta(months=3))
    return_dates["rm3_date8"] = shiftDates(date8 - relativedelta(months=2))
    return_dates["rm4_date8"] = shiftDates(date8 - relativedelta(months=1))
    return_dates["rm5_date8"] = shiftDates(date8 - datetime.timedelta(weeks=2))
    return_dates["rm6_date8"] = shiftDates(date8 - datetime.timedelta(weeks=1))

    return_dates["rm1_date9"] = shiftDates(date9 - relativedelta(months=1))
    return_dates["rm2_date9"] = shiftDates(date9 - datetime.timedelta(weeks=2))
    return_dates["rm3_date9"] = shiftDates(date9 - datetime.timedelta(weeks=1))
    return_dates["rm4_date9"] = shiftDates(date9 - datetime.timedelta(days=1))

    return_dates["rm1_date10"] = shiftDates(date10 - relativedelta(months=1))
    return_dates["rm2_date10"] = shiftDates(date10 - datetime.timedelta(weeks=2))
    return_dates["rm3_date10"] = shiftDates(date10 - datetime.timedelta(weeks=1))

    return_dates["rm1_date11"] = shiftDates(date11 - relativedelta(months=1))
    return_dates["rm2_date11"] = shiftDates(date11 - datetime.timedelta(weeks=2))
    return_dates["rm3_date11"] = shiftDates(date11 - datetime.timedelta(weeks=1))
    
    return_dates["rm1_date12"] = shiftDates(date12 - relativedelta(months=1))
    return_dates["rm2_date12"] = shiftDates(date12 - datetime.timedelta(weeks=2))
    return_dates["rm3_date12"] = shiftDates(date12 - datetime.timedelta(weeks=1))

    return_dates["rm1_date13"] = shiftDates(date13 - relativedelta(months=1))
    return_dates["rm2_date13"] = shiftDates(date13 - datetime.timedelta(weeks=2))
    return_dates["rm3_date13"] = shiftDates(date13 - datetime.timedelta(weeks=1))

    return_dates["rm1_date14"] = shiftDates(date14 - relativedelta(months=1))
    return_dates["rm2_date14"] = shiftDates(date14 - datetime.timedelta(weeks=2))
    return_dates["rm3_date14"] = shiftDates(date14 - datetime.timedelta(weeks=1))
    return return_dates

def shiftDates(date):
    if date.weekday()>=5 or date in list_of_holidays:
        while date.weekday()>=5 or date in list_of_holidays:
            date = date - datetime.timedelta(days=1)
    return date