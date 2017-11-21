def cadenas_2():
    palabra= raw_input("dime una palabra")
    for cont in range(0, len(palabra),1):
        if palabra[cont]== 'a':
            suma=suma+1
    print"en la palabra", palabra, "hay", suma, "letra"
cadenas_2()
