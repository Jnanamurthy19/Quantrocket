import pandas as pd
import os

os.chdir('/codeload/data/ASX STK Listings')


def find_conid(n): #define function
            
            df = pd.read_csv('master.csv', index_col = "ConId")          
            row = df.loc[int(entry)].copy()
           
     
            print('\n----------------------------------------------------')
            print("conid: " + entry)
            print("symbol: " + str(row[0]))
            print("name: " + str(row[8]))
            print("sectype: " + str(row[2]))
            print("exchange: " + str(row[3]))
            print("sector: " + str(row[12]))
            print("industry: " + str(row[13]))
            print("date delisted: " + str(row[34]))
            print('----------------------------------------------------\n')
 
def find_code(n): #define function
            
            df = pd.read_csv('master.csv', index_col = "Symbol")          
            row = df.loc[entry].copy()
           
     
            print('\n----------------------------------------------------')
            print("conid: " + str(row[0]))
            print("symbol: " + str(entry))
            print("name: " + str(row[8]))
            print("sectype: " + str(row[2]))
            print("exchange: " + str(row[3]))
            print("sector: " + str(row[12]))
            print("industry: " + str(row[13]))
            print("date delisted: " + str(row[34]))
            print('----------------------------------------------------\n')
 
        

run = 'go'
while run == 'stop':
    
    #input number you want to search
    entry = input('\nEnter conid or stk code to find ("ctrl c" to cancel)\n\n')
    if len(entry) > 4:#meaning it's a conid
        find_conid(entry)
    
    else:
        find_code(entry)
    