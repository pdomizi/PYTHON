def run():
    print("Hola Usuario!")
    numero_a = int(input("Ingresa el primer numero: "))
    numero_b = int(input("Ingresa el segundo numero:"))
    numero_c = int(input("Ingresa el tercer numero: "))
    suma = numero_a + numero_b + numero_c
    promedio = suma/3
    print("Usuario, la suma de los numeros es: " + str(suma))
    print("Y su promedio es: " + str(promedio))
    
if __name__ == "__main__":
    run()