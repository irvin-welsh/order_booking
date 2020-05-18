from datetime import *
from dateutil.relativedelta import *
from dateutil.rrule import *
from dateutil.parser import *
import calendar
import sqlite3

connection=sqlite3.connect("working_dates.db")
crsr = connection.cursor()
#
# def getDataFromDB():
#     for rows in crsr.execute('SELECT * FROM delivery_slots'):
#         cc_rows=crsr.fetchall()
#     working_dates=[cc_rows]
#     return working_dates

# Warehouse is working according to 1/3 shift (1 workday and 3 days off), so order must be delivered only on working days which are calculated as x+4
def get_working_days():
    current_date = date.today()
    start_date = date(2020,5,20)
    global delivery_dates
    delivery_dates=[]
    get_delivery_slots=list(rrule(DAILY, interval=4, count=100, dtstart=parse(str(start_date))))
    for slot in get_delivery_slots:
        slotFormatted = [slot.strftime('%d-%B-%Y')]
        # tpl = tuple(slotFormatted)
        delivery_dates.append(slotFormatted)
    return delivery_dates

def db_params():
    params = [(k) for k in delivery_dates]
    crsr.execute('''CREATE TABLE IF NOT EXISTS delivery_slots (Delivery_Slots TEXT);''')
    for param in params:
        z=tuple(param)
        crsr.execute('INSERT INTO delivery_slots VALUES (?)', z)
    connection.commit()

get_working_days()
db_params()
