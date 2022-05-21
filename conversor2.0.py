menu = """
Bienvenido al conversor de monedas 

1 - Pesos Argentinos 
2 - Pesos Colombianos 
3 - Pesos Mexicanos 

Elige una opción: """

opcion = input(menu)

if opcion == "1":
    #BLOQUE DE CÓDIGO
    pesos = input("Cuantos pesos argentinos tenes? ")
    pesos = float(pesos)
    valor_dolar = 200
    dolares = pesos / valor_dolar
    dolares = round(dolares, 4)
    dolares = str(dolares)
    print ("Tenes $" + dolares + " dolares")
    #FIN BLOQUE DE CÓDIGO 
elif opcion == "2":
    #BLOQUE DE CÓDIGO
    pesos = input("Cuantos pesos mexicanos tenes? ")
    pesos = float(pesos)
    valor_dolar = 4000
    dolares = pesos / valor_dolar
    dolares = round(dolares, 4)
    dolares = str(dolares)
    print ("Tenes $" + dolares + " dolares")
    #FIN BLOQUE DE CÓDIGO 
elif opcion == "3":
    #BLOQUE DE CÓDIGO
    pesos = input("Cuantos pesos colombianos tenes? ")
    pesos = float(pesos)
    valor_dolar = 30
    dolares = pesos / valor_dolar
    dolares = round(dolares, 4)
    dolares = str(dolares)
    print ("Tenes $" + dolares + " dolares")
    #FIN BLOQUE DE CÓDIGO 
else:
    print("Ingresa la opción correcta")
    
 