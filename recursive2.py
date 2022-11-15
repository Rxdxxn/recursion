def recursiv_putere(m,n):
    if (n==0):
        return 1
    else:
        return m * recursiv_putere(m,n-1) 
A=int(input("Introduceti primul numar:"))
B=int(input("Introduceti al doilea numar:"))
print(A,"**",B,"=",recursiv_putere(A,B))