def numero_inpares():
    n_impares= 0
    cifra=0
    n_pares=0
    numero= input("Dime el numero 1000 y te dire sus impares: ")
    while numero>0:
       cifra== numero%10
       if cifra%2 ==0:
          n_pares=n_pares+1
       else:
          n_impares=n_impares+1
       numero=numero/10
    print "Tiene ", n_impares, "cifras impares y las pares no te las digo",
numero_inpares()
