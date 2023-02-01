# Happy New Year

import os 
import time
from random import randint

for i in range(1,85):
    print('')

s = ''

for i in range(1,1000):
    count=randint(1,100)
    while(count > 0):
        s += ' '
        count -= 1
    
    if(i%10 == 0):
        print(s+ "Happy New Year")
    elif(i%17 ==0):
        print(s+'2023')
    else:
        print(s+'*')

    s=''
    time.sleep(0.3)


