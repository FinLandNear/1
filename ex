'''
sdfsdf
'''

import openpyxl
import time

from datetime import datetime
from openpyxl import load_workbook
wb = load_workbook('C:/Users/Alexandr/Desktop/engineers_club_bot/txlc_coe2.xlsx')
ws = wb.active
a = 1
f = 'F'
num = 0
while num != None:
    a = a + 1
    st = f + str(a)
    num = ws[st].value
print (num)
print (st)
ws[st]= datetime.now()
wb.save('C:/Users/Alexandr/Desktop/engineers_club_bot/txlc_coe2.xlsx')
