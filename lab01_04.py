import statistics 
import math
import random


wektor1=[]
wektor2=[]
wektor_skalarny=0
zakres =10

for x in range(10):
  wektor1.append(random.randint(0,20))
  wektor2.append(random.randint(0,20))
#print (wektor2)

#iloczyn sklarny
for i in range(zakres):
    wektor_skalarny += wektor1[i] * wektor2[i]

print ("iloczyn skalarny",wektor_skalarny)

#dlugosc wektrow 
#1
dlugosc_wek1=0

for i in range(zakres):
    dlugosc_wek1 +=wektor1[i] *wektor1[i]
dlugosc_wek1= math.sqrt(dlugosc_wek1)
print ("dlugosc", dlugosc_wek1)
#2
dlugosc_wek2=0
for i in range(zakres):
    dlugosc_wek2 +=wektor2[i] *wektor2[i]
dlugosc_wek2= math.sqrt(dlugosc_wek2)
print ("dlugosc", dlugosc_wek2)

#cosinus
cos_kat=(wektor_skalarny)/((dlugosc_wek1)*(dlugosc_wek2))

print ("cosinus",cos_kat)

#radiany
kat_na_radiany = math.acos(cos_kat)
print("kat w radianach", kat_na_radiany)

#stopnie 
stopnie= math.degrees(kat_na_radiany)
print("stopnie",stopnie)

