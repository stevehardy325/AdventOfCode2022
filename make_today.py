import datetime as dt
import shutil


today = dt.date.today()
day_of_month_int = today.day
dom_2_digit = '{:02d}'.format(day_of_month_int)
print(dom_2_digit)
'''shutil.copyfile('base_example.txt', '{}_example.txt'.format(dom_2_digit))
shutil.copyfile('base_input.txt', '{}_input.txt'.format(dom_2_digit))
with open('base_pt1.py') as base_py_fobj:
    base_py_str = base_py_fobj.read()
    print(base_py_str)
    formatted_py_str = base_py_str.format(day_str=dom_2_digit)
    with open('{}_pt1.py'.format(dom_2_digit), 'w') as new_py_fobj:
        new_py_fobj.write(formatted_py_str)'''
shutil.copytree('./base/', './{}/'.format(dom_2_digit))

