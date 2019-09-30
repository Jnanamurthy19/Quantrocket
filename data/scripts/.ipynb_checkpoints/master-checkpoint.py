import pytz
import sys
import os
from datetime import datetime

datestring = datetime.strftime(datetime.now(pytz.timezone('Australia/Sydney')), '%Y-%m-%d')
today_listings = "asx-listings-" + datestring + ".csv"


os.chdir('/codeload/data/ASX STK Listings')


with open(today_listings, 'r') as t1, open('master.csv', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

with open('master.csv', 'a') as outFile:
#    outFile.write('\n')
    for line in fileone[1:]:
        if line not in filetwo:
            outFile.write(line)