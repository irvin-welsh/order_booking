from datetime import *
from dateutil.relativedelta import *
from dateutil.rrule import *
from dateutil.parser import *
import calendar

def get_working_days():
    START_DATE= date(2020,5,20).strftime('%d-%B-%Y')
    delivery_dates=[]
    get_delivery_slots=list(rrule(DAILY, interval=4, count=20, dtstart=parse(START_DATE)))
    for slot in get_delivery_slots:
        slotFormatted = slot.strftime('%d-%B-%Y')
        delivery_dates.append(slotFormatted)
    return delivery_dates
