def cambiavocales():
    texto= raw_input("dime una texto")
    for cont in range (0,len(texto),1):
        if texto[cont]=='a'or texto[cont]=='e'or texto[cont]=='i'or texto[cont]=='o':
           print 'u',
        else:
           print texto[cont],
cambiavocales()
