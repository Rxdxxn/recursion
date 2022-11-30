#Moș Crăciun pregătește cadourile pentru acest an. El trebuie să dea cadouri identice la n copii. 
# Pentru aceasta, a vizitat m magazine (posibil online) și pentru fiecare magazin a aflat prețul 
# cadoului în acel magazin și numărul de cadouri disponibile în acel magazin.
#Determinati suma minimă necesară pentru a cumpăra cele n cadouri. Dacă nu se pot cumpăra cele n cadouri afișați mesajul imposibil.
def mos_craciun(pret, n, volum_max):
    index = list(range(len(pret)))
    raport = [pi/num for pi, num in zip(pret, n)]
    index.sort(key=lambda i: raport[i], reverse=True)
    pret_max = 0
    fr = [0]*len(pret)
    for i in index:
        if n[i] >= volum_max:
            fr[i] = 1
            pret_max += pret[i]
            volum_max -= n[i]
        else:
            fr[i] = volum_max/n[i]
            pret_max += pret[i]*volum_max/n[i]
            break
    return pret_max, fr

m = int(input('Introduceti numarul de magazine: '))
pret = input('Introduceti pretul la cadouri din {} magazine prin tasta space: '.format(m)).split()
pret = [int(pi) for pi in pret]
d = input('Introduceti volumul a {} obiecte prin tasta space: '.format(m)).split()
n = [int(vi) for vi in n]
volum_max = int(input('Introduceti volum maxim al rucsacului: '))
 
pret_max, fr = mos_craciun(pret, n, volum_max)
print('Pretul maxim de obiecte ce incap in rucsac: ', pret_max)
print('The fractions in which the items should be taken:', fr)