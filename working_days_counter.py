from datetime import *
from dateutil.relativedelta import *
from dateutil.rrule import *
from dateutil.parser import *
import calendar

# Warehouse is working according to 1/3 shift (1 workday and 3 days off), so order must be delivered only on working days which are calculated as x+4
def get_working_days():
    START_DATE= date(2020,5,20).strftime('%d-%B-%Y')
    delivery_dates=[]
    get_delivery_slots=list(rrule(DAILY, interval=4, count=20, dtstart=parse(START_DATE)))
    for slot in get_delivery_slots:
        slotFormatted = slot.strftime('%d-%B-%Y')
        delivery_dates.append(slotFormatted)
    constant_line_in_message = "Свободные слоты на доставку:\n"
    variable_lines_in_message = "\r\n\t".join(delivery_dates[1:])
    concantenated_string = constant_line_in_message+variable_lines_in_message
    return concantenated_string
get_working_days()
