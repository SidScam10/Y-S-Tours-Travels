#packages module
import sys
import time
from transportation import *
def slowprint(s):
    s=s+'\n'
    for i in s:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.01)
slowprint('-------------------------------------------------𝕻𝖆𝖈k𝖆𝖌𝖊𝖘----------------------------------------------------------')
print("All prices shown below are per head")
print("Economical base packages include hotel stay and complementary breakfast")
print("Luxury package include base package services + complementary dinner and a rented vehicle for travel")
day=int(input("Enter duration of stay in days:"))
costebp=0
costlbp=0
if dest==1:
    slowprint('𝕯𝖚𝖇𝖆𝖎')
    print('1) Ecomical base package = 50,000 Rs')
    print('2) Luxry base package = 100,000 Rs')
    costebp=50000
    costlbp=100000
if dest==2:
    slowprint('𝕾𝖎𝖓𝖌𝖆𝖕𝖔𝖗𝖊')
    print('1) Economical base package = 75,000 Rs')
    print('2) Luxury base package = 125,000 Rs')
    costebp=75000
    costlbp=125000
if dest==3:
    slowprint('𝕹𝖊𝖜 𝖄𝖔𝖗k')
    print('1) Economical base package = 100,000 Rs')
    print('2) Luxury base package = 150,000 Rs')
    costebp=100000
    costlbp=150000
if dest==4:
    slowprint('𝕰𝖚𝖗𝖔𝖕𝖊')
    print('1) Economical base package = 150,000 Rs')
    print('2) Luxury base package = 200,000 Rs')
    costebp=150000
    costlbp=200000
if dest==5:
    slowprint('𝕽𝖚𝖘𝖘𝖎𝖆')
    print('1) Economical base package = 130,000 Rs')
    print('2) Luxury base package = 180,000 Rs')
    costebp=130000
    costlbp=180000
if dest==6:
    slowprint('𝕬𝖚𝖘𝖙𝖗𝖆𝖑𝖎𝖆')
    print('1) Economical base package = 100,000 Rs')
    print('2) Luxury base package = 150,000 Rs')
    costebp=100000
    costlbp=150000
if dest==7:
    slowprint('𝖀𝖓𝖎𝖙𝖊𝖉 𝕶𝖎𝖓𝖌𝖉𝖔𝖒')
    print('1) Economical base package = 120,000 Rs')
    print('2) Luxury base package = 170,000 Rs')
    costebp=120000
    costlbp=170000
pack=int(input('Enter package:'))
if pack==1:
    packprice=costebp+15000*day
    packtyp="Economical base package"
if pack==2:
    packprice=costlbp+15000*day
    packtyp="Luxury base package"
totalpackprice=packprice*per
