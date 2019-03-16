import statistics 
import math
import random


w1=[]
w2=[]

zakres =10

for x in range(zakres):
  w1.append(random.randint(0,20))
  w2.append(random.randint(0,20))

#iloczyn sklarny
def vec_scal(x,y):
    wek_skal=0
    for i in range(len(x)):
        wek_skal += x[i] * y[i]
    return wek_skal

#dlugosc wektrow 
def vec_lec(x,y):
  wek_dl1=0
  for i in range(len(x)):
    wek_dl1 += x[i] *x[i]
  wek_dl1= math.sqrt(wek_dl1)

  wek_dl2 =0
  for i  in range(len(y)):
    wek_dl2 +=y[i] *y[i]
  wek_dl2= math.sqrt(wek_dl2)
  return wek_dl1,wek_dl2


#cosinus
def vec_cos(x,y):
  wek_cos=0
  vec_lec2=vec_lec(x,y)
  wek_cos= (vec_scal(x,y))/(vec_lec2[0]*vec_lec2[1])
  return wek_cos


#radiany
def vec_ang_rad(x,y):
  wek_kat_rad=0
  wek_kat_rad= math.acos(vec_cos(x,y))
  return wek_kat_rad

#stopnie 
def vec_ang_deg(x,y):
  wek_kat_stopnie=0
  wek_kat_stopnie=math.degrees(vec_ang_rad(x,y))
  return wek_kat_stopnie


print("iloczyn skalarny :",vec_scal(w1,w2),"dlugoc wektorw",vec_lec(w1,w2))
print("cosinus ",vec_cos(w1,w2))
print("radiany", vec_ang_rad(w1,w2))
print("stopnie", vec_ang_deg(w1,w2))