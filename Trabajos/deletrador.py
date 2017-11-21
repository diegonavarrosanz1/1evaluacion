def deletrador():
    nombre= raw_input("dime una palabra")
    print "la palabra tiene", len(nombre), "letras"
    vocales=u
    for cont in range (0,len(nombre),1):
        if nombre[cont]=='a'or nombre[cont]=='e'or nombre[cont]=='i'or nombre[cont]=='o'or nombre[cont]=='u':
            vocales= vocales+1
    print "de las cuales", vocales, "son vocales y ", len(nombre) - vocales, "consonante"
deletrador()

        
    
    
