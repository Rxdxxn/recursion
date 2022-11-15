def iterativ_putere(m,n):
    p=1
    for i in range(1,n+1):
        p*=m
    return p
A=int(input("Introduceti primul numar:"))
B=int(input("Introduceti al doilea numar:"))
print(A,"**",B,"=",iterativ_putere(A,B))
        