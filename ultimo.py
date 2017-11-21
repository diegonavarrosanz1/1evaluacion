def suma_cifras():
    suma=0
    numero= input("dime un numero")
    while numero<10:
        suma= suma + numero%10
        numero= suma/10
    print "la suma de los restos del numero son", suma + numero,
suma_cifras()
