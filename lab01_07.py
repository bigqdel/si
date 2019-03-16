import csv
import pandas as pd
#import numpy as np

#platki = open('cereal.csv',)
#platki_czytacz= csv.reader(platki)

#platki_lista=list(platki_czytacz)

dane=pd.read_csv('cereal.csv')
print(dane)#wyswietlanie csv po wczytaniu przez "pande"
print(dane.dtypes)#wyswietlanie typow danych
print(dane.iloc[[1]])#wuswietla wiersz (tutaj o nuemrze jeden)
print(dane['protein'])#wuswietla kolumne o podanej nazwie 
#print(platki_lista)


