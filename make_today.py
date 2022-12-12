import datetime as dt
import shutil


today = dt.date.today()
day_of_month_int = today.day
dom_2_digit = '{:02d}'.format(day_of_month_int)
print(dom_2_digit)

shutil.copytree('./base/', './{}/'.format(dom_2_digit))

