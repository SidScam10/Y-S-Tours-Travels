import csv
import sys
import time
def slowprint(s):
    s=s+'\n'
    for i in s:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.01)
slowprint('----------------------------𝖄&𝕾 𝕿𝖔𝖚𝖗𝖘 𝖆𝖓𝖉 𝕿𝖗𝖆𝖛𝖊𝖑𝖘--------------------------------')
import services
name=input("Enter customer name:")
import transportation
import packages
import discounts
from transportation import *
from discounts import *
from packages import *
def printrow(a,e):
    print('{:35}{:10}'.format(a,e))
customer=["Name of customer",name]
pep=['Number of people travelling',per]
dur=["Duration of stay",day]
destination=['Destination',place]
transportation=['Transport',trans]
transprice=['Transportation Price',travprice]
package=['Package type',packtyp]
indpack=['Individual Package Price',packprice]
totpackprice=['Total Package Price',totalpackprice]
distyp=['Discount Type',distyp]
indis=['Individual Discount',perdis]
discount=['Total Discount',disc]
fintrav=travprice-disc
finaltransprice=['Final Travel Price after discount',fintrav]
total=totalpackprice+fintrav
pertot=total/per
perbill=['Price for each individual',pertot]
totalbill=['Total Price for whole trip',total]
with open ('receit.csv','w',newline='') as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(customer)
    csv_writer.writerow(pep)
    csv_writer.writerow(dur)
    csv_writer.writerow(destination)
    csv_writer.writerow(transportation)
    csv_writer.writerow(transprice)
    csv_writer.writerow(package)
    csv_writer.writerow(indpack)
    csv_writer.writerow(totpackprice)
    csv_writer.writerow(distyp)
    csv_writer.writerow(indis)
    csv_writer.writerow(discount)
    csv_writer.writerow(finaltransprice)
    csv_writer.writerow(perbill)
    csv_writer.writerow(totalbill)
slowprint('-'*70)
slowprint('𝕱𝖎𝖓𝖆𝖑 𝕽𝖊𝖈𝖊𝖎𝖕𝖙')
slowprint('-'*70)
with open('receit.csv','r') as f:
    csvreader=csv.reader(f)
    for row in csvreader:
             printrow(row[0],row[1])
slowprint('-'*70)
        
    

    
