def run():
    print("Hola Usuario!")
    monto = int(input("Ingresa el monto: "))
    monto_con_iva = monto*21/100 
    monto_total = monto + monto_con_iva
    print("El monto total es: " + str(monto_total))
if __name__ == "__main__":
    run()