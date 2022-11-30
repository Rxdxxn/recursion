"""Pe insula a naufragiat un om. Aici se afla doar un singur magazin.
Acest magazin e deschis in toate zilele, in afara de duminica. 
Luand in considerare ca azi e luni, aflati daca omul va supravietui
Care este minimul de zile, in care trebuie sa cumpere produse pentru supratietuire?

Verificare. Pentru valorile 10, 16, 2, raspunsul este de 2 zile. 2 zile el trebuie sa cumpere produse, astfel incat sa supravietuiasca toate zilele.
            Pentru valorile 10, 20, 30 raspunsul este `nu va supravietui`. Cantitatea de produse necesare in fiecare zi e mai inalt decat numarul de produse posibile de procurat """

s = int(input("Numarul total de zile care ar trebui sa supravietuiasca = "))
n = int(input("Maximul de produse ce pot fi procurate zilnic = "))
m = int(input("Maximul de produse ce este nevoie zilnic = "))

def supravietuire(zile_total, max_mancare, max_zi):
    if (((max_mancare*6)<(max_zi*7) and zile_total>6) or max_zi>max_mancare):
        return print("Nu poate supravietui")
    else:
        zile = (max_zi*zile_total)/max_mancare

        if ((max_zi*zile_total)%max_mancare)!= 0:
            zile += 1
        return print("Va supravietui", round(zile), "zile")
supravietuire(s, n, m)
