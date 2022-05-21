def conversor(tipo_pesos, valor_dolar):
    pesos = input("Cuantos pesos" + tipo_pesos + " tenes?")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 4)
    dolares = str(dolares)
    print ("Tenes $" + dolares + " dolares")
menu = """
Bienvenido al conversor de monedas 

1 - Pesos Argentinos 
2 - Pesos Colombianos 
3 - Pesos Mexicanos 

Elige una opción: """

opcion = input(menu)

if opcion == "1":
    conversor("argentinos", 200)
elif opcion == "2":
    conversor("colombianos", 4000)
elif opcion == "3":
    conversor("mexicanos", 30)
else:
    print("Ingresa la opción correcta")
    