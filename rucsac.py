def rucsac(pret, volum, volum_max):
    index = list(range(len(pret)))
    raport = [pi/vi for pi, vi in zip(pret, volum)]
    index.sort(key=lambda i: raport[i], reverse=True)
    pret_max = 0
    fr = [0]*len(pret)
    for i in index:
        if volum[i] <= volum_max:
            fr[i] = 1
            pret_max += pret[i]
            volum_max -= volum[i]
        else:
            fr[i] = volum_max/volum[i]
            pret_max += pret[i]*volum_max/volum[i]
            break
    return pret_max, fr
 
 
n = int(input('Introduceti numarul de obiecte: '))
pret = input('Introduceti pretul a {} obicete prin tasta space: '.format(n)).split()
pret = [int(pi) for pi in pret]
volum = input('Introduceti volumul a {} obiecte prin tasta space: '.format(n)).split()
volum = [int(vi) for vi in volum]
volum_max = int(input('Introduceti volum maxim al rucsacului: '))
 
pret_max, fr = rucsac(pret, volum, volum_max)
print('Pretul maxim de obiecte ce incap in rucsac: ', pret_max)
print('The fractions in which the items should be taken:', fr)



