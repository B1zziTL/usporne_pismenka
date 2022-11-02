#premenne
slova = 0
kompresia = ''
vysledok = ''

#vstup od pouzivatela a jeho rozdelenie
povodny_oznam = input('Zadaj oznam: ')
oznam = povodny_oznam.split()

for slovo in oznam: #prechadzanie slov z vstupu
    #pocitanie slov
    slova += 1

    #prepisanie kazdeho druheho slova velkymi pismenami do vystupu
    if not slova % 2 == 0:
        slovicko = slovo.upper()
        kompresia += slovicko
    else:
        kompresia += slovo

def dekompresia(kompresia): #funkcia na spatnu dekompresiu
    #globalna premenna
    global vysledok
    
    #zadefinovanie velkeho pismena
    velke = kompresia[0].isupper()

    for i in kompresia: #prechadzanie pismen z kompresovaneho oznamu
        #podmienka ak je pismeno male, tak sa zmeni na velke 
        if not i.isupper() == velke:
            vysledok += ' '
            velke = i.isupper()
        vysledok += i.upper()

#privolanie funkcie
dekompresia(kompresia)

#vypisanie udajov
print('Oznam pozostáva z',slova,'slov.')
print('Skompresovaný oznam:',kompresia)
print('Dekompresovaný oznam:',vysledok)
