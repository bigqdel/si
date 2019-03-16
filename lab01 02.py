"""
Zadanie 2
Rozpocznij program wpisując swoje imię i nazwisko jako jeden łańcuch znaków (możesz go zapisać
pod jakąś zmienną). Następnie:
• Używając odpowiedniej komendy, rozbij ten string na dwa: imię i nazwisko i zapisz pod
innymi zmiennymi.
• Używając odpowiedniej komendy, podaj długość twojego imienia.
• Używając odpowiedniej komendy, podaj nazwisko wypisane wyłącznie małymi literami.
"""
print('podaj imie i nazwisko')
imie_nazwisko = input() 
#print(imie_nazwisko)
imie,nazwisko=imie_nazwisko.split(" ")
print(len(imie)," ",nazwisko.lower())