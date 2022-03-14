import numpy
import datetime

t1 = datetime.datetime.now()

lim = 10000000
array = numpy.zeros(lim)
array[0] = 1

nth_prime = 10001

count = 0 
num = 0 

for i in array :
    num += 1 
    
    if i == 0 :
        count += 1 

        if count == nth_prime :  
            break 

        highest_multiple = int(lim/num)+1

        for j in range(2, highest_multiple):
            array[(num*j)-1] = 1

t2 = datetime.datetime.now()

print(num, t2-t1)