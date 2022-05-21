
def conversacion(mensaje):
    print("Hola")
    print("Como estas?")
    print(mensaje)
    print("Adios")

opcion = int(input("Elige una opción: 1 - 2 - 3"))

if opcion == 1:
    conversacion("Elegiste la 1")
elif opcion == 2:
    conversacion("Elegiste la 2")
elif opcion == 3:
    conversacion("Elegiste la 3")
else:
    print("Escribe la opción correcta")