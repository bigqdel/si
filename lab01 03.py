"""Stwórz i wypisz wektor 30 losowych liczb od 0 do 100. Następnie program musi obliczyć i podać:
• Największą i najmniejszą liczbę z podanego wektora.
• Wektor posortowany rosnąco.
• Średnią z podanego wektora.
• Odchylenie standardowe z podanego wektora.
• Wektor znormalizowany, wg wzoru:"""
import statistics 

import random
wektor = []
wektore_norm=[]
wektor_ust=[]
for x in range(30):
  wektor.append(random.randint(1,100))
wektor_rosnoaco=wektor
wektor_rosnoaco.sort(reverse=False)
print(wektor_rosnoaco)

wektor_malejaco=wektor
wektor_malejaco.sort(reverse=True)
print(wektor_malejaco)

print("wartość max ", max(wektor),"wartosc min", min(wektor))
print("Odchylenie standardowe z podanego wektora  % s " 
                % (statistics.stdev(wektor))) 
odchystd = statistics.stdev(wektor)
#wektor znormalizowany
wek_max=max(wektor)
wek_min=min(wektor)
for x in wektor:
    x =(x-min(wektor))/(max(wektor)-min(wektor))
    wektore_norm.append(x)

#wektor ustandry
srednia= sum(wektor)/len(wektor)
print(srednia)
for val in wektor:
    val =(val-srednia)/(statistics.stdev(wektor))
    wektor_ust.append(val)


print("wektor",wektor)
print("wektor znormalizowany",wektore_norm)
print("wektor  usta", wektor_ust)
