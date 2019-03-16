import math
import random
import matplotlib
import matplotlib.pyplot as plt 


#import numpy as np

w1=[]
os_x=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
os_y=[]
zakres =100
for x in range(zakres):
  w1.append(random.randint(0,20))


for i in os_x:
    count =w1.count(i)
    os_y.append(count)
 

#note that it is 'a range' to position it nicely on x axis
#ypos=np.arange(len(os_x))

plt.bar(os_x, os_y, width=0.4, label='Wystapienia', color='red')
#plt.bar(ypos+0.2, Printers, width=0.2, label='Printers', color='green')
#give title
plt.title('ilosc wystapeni liczb')
plt.xticks(os_x)
plt.xlabel('liczba')
plt.ylabel('wysatapienie')
#plt.plot(ypos, Year) will remove the numbers along the y-axis
#shows legend
plt.legend()
#show to show the graph
plt.show()
#savefig to save the figure in png with name 'graph'
plt.savefig('graph')
"""
print (w1)
print (os_y)
print (os_x)
"""