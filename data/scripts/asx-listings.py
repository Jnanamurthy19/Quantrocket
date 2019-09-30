import pytz
import sys
import os
from quantrocket.master import collect_listings, download_master_file
from datetime import datetime
import glob
import time

#Collect listings from IB
collect_listings(exchanges="ASX", sec_types=["STK"])

#Wait 30mins, for listings to finish collecting
time.sleep(1800)

#Make a file containing all ASX listings
download_master_file(exchanges="ASX", sec_types="STK", filepath_or_buffer="/codeload/data/ASX STK Listings/asx-listings-d.csv")



datestring = datetime.strftime(datetime.now(pytz.timezone('Australia/Sydney')), '%Y-%m-%d')


#change directory so os.rename works properly
os.chdir('/codeload/data/ASX STK Listings')


#Rename file to contain todays date
for f in glob.glob('asx-listings-d.csv'):
    new_filename = f.replace("d",datestring)
    os.rename(f,new_filename)