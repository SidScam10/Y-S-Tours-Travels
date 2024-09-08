#Transportation module
import time
import sys
def slowprint(s):
    s=s+'\n'
    for i in s:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.01)
slowprint('----------------------------------𝕿𝖗𝖆𝖓𝖘𝖕𝖔𝖗𝖙𝖆𝖙𝖎𝖔𝖓-----------------------------------')
dest=int(input('Enter desired destination number:'))
print('Modes of transport available:')
costa=0
costcs=0
if dest==1:
    slowprint('𝕯𝖚𝖇𝖆𝖎')
    place="Dubai"
    print('1) Airplane - 50,000 Rs per head')
    print('2) Cruise ship - 75,000 Rs per head')
    costa=50000
    costcs=75000
if dest==2:
    slowprint('𝕾𝖎𝖓𝖌𝖆𝖕𝖔𝖗𝖊')
    place='Singapore'
    print('1) Airplane - 40,000 Rs per head')
    costa=40000
if dest==3:
    slowprint('𝕹𝖊𝖜 𝖄𝖔𝖗k')
    place="New York"
    print('1) Airplane - 75,000 Rs per head')
    print('2) Cruise ship - 100,000 Rs per head')
    costa=75000
    costcs=100000
if dest==4:
    slowprint('𝕰𝖚𝖗𝖔𝖕𝖊')
    place="Europe"
    print('1) Airplane - 75,000 Rs per head')
    print('2) Cruise ship - 100,000 Rs per head')
    costa=75000
    costcs=100000
if dest==5:
    slowprint('𝕽𝖚𝖘𝖘𝖎𝖆')
    place="Russia"
    print('1) Airplane - 60,000 Rs per head')
    costa=60000
if dest==6:
    slowprint('𝕬𝖚𝖘𝖙𝖗𝖆𝖑𝖎𝖆')
    place="Australia"
    print('1) Airplane - 80,000 Rs per head')
    print('2) Cruise ship - 110,000 Rs per head')
    costa=80000
    costcs=110000
if dest==7:
    slowprint('𝖀𝖓𝖎𝖙𝖊𝖉 𝕶𝖎𝖓𝖌𝖉𝖔𝖒')
    palce="United Kingdom"
    print('1) Airplane - 85,000 Rs per head')
    print('2) Cruise ship - 100,000 Rs per head')
    costa=85000
    costcs=100000
print('*All prices shown are for a two way trip*')
trans=int(input('Enter transportation method:'))
per=int(input("Enter number of people travelling:"))
if trans==1:
    travprice=costa*per*2
    trans="Airplane"
if trans==2:
    travprice=costcs*per*2
    trans="Cruise Ship"

