#Discounts module
from transportation import *
import sys
import time
def slowprint(s):
    s=s+'\n'
    for i in s:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.01)
slowprint("-----------------------------------------𝕯𝖎𝖘𝖈𝖔𝖚𝖓𝖙𝖘-----------------------------------------")
print('->Family/friends discount is applicable to 2 or 2+ members')
print('->Business discounts applicable only if company details and team travelling is provided')
print("Enter applicable travelling method:")
slowprint("1) 𝕭𝖚𝖘𝖎𝖓𝖊𝖘𝖘")
slowprint("2) 𝕱𝖆𝖒𝖎𝖑y")
slowprint("3) 𝕷𝖔𝖓𝖊 𝕿𝖗𝖆𝖛𝖊𝖑𝖑𝖊𝖗")
ch=int(input("Enter choice:"))
perdis=0
disc=0
if ch==1:
    if per>=2:
        print("Please enter business details:")
        bus=input("Enter company:")
        print("11% Business discount applicable on each individual")
        ch2=input('Apply discount? Y/N')
        if ch2=='Y' or ch2=='y':
            if trans=="Airplane":
                perdis=costa*2*11/100
            else:
                perdis=costcs*2*11/100
            dis=perdis*per
            distyp="Business"
            print('Discount Applied')
    else:
        print('Business discount not applicable')
elif ch==2:
    if per>=2:
        print("8% Family discount applicable on each individual")
        ch2=input('Apply discount? Y/N')
        if ch2=='Y' or ch2=='y':
            if trans=="Airplane":
                perdis=costa*2*8/100
            else:
                perdis=costcs*2*8/100
            disc=perdis*per
            distyp="Family"
            print('Discount Applied')
    else:
        print('Family discount not applicable')
elif ch==3:
    if per==1:
        distyp="No Discount"
        print("No discount applicable on travel")
        perdis=0
        disc=0
