def polindrom():
    rev=0
    n=int(input('Vvedite seloe chislo: '))
    a=n
    while n>0:
        d=n%10
        rev=rev*10+d
        n=n//10
    if a==rev:
        return True
    else:
        return False
print(polindrom())