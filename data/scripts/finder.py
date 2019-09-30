import csv
import sys
import os

os.chdir('/codeload/data/ASX STK Listings')



def find_code(n): #define function
    #read csv, and split on "," the line
    csv_file = csv.reader(open('master.csv', "r"), delimiter=",")

    #loop through csv list
    for row in csv_file:
        #if current rows 2nd value is equal to input, print that row
        if n == row[0]:
            #find specific columns
            conid = row[0]
            symbol = row[1]
            sectype = row[3]
            exchange = row[4]
            name = row[9]
        
            #choose yo print
            
            #print(str(conid) + ", " + str(symbol) + ", " + str(secType) + ", " + str(exchange) + ", " + str(name))
            print('\n----------------------------------------------------')
            print("conid: " + str(conid))
            print("symbol: " + str(symbol))
            print("name: " + str(name))
            print("sectype: " + str(sectype))
            print("exchange: " + str(exchange) + "")
            print('----------------------------------------------------\n')

def find_conid(n): #define function
    #read csv, and split on "," the line
    csv_file = csv.reader(open('master.csv', "r"), delimiter=",")

    #loop through csv list
    for row in csv_file:
        #if current rows 2nd value is equal to input, print that row
        if n == row[1]:
            #find specific columns
            conid = row[0]
            symbol = row[1]
            sectype = row[3]
            exchange = row[4]
            name = row[9]
        
            #choose yo print
            
            #print(str(conid) + ", " + str(symbol) + ", " + str(secType) + ", " + str(exchange) + ", " + str(name))
            print('\n----------------------------------------------------')
            print("conid: " + str(conid))
            print("symbol: " + str(symbol))
            print("name: " + str(name))
            print("sectype: " + str(sectype))
            print("exchange: " + str(exchange) + "")
            print('----------------------------------------------------\n')

run = 'go'
while run != 'stop':
    
    #input number you want to search
    number = input('\nEnter conid or stk code to find ("ctrl c" to cancel)\n\n')
    find_code(number)
    find_conid(number)
    
    
    
