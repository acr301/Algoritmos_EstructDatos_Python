"""
    fijo 100 bicicleta
    motos y carros pagan 30 cor x km
    camioneros pagan 30 cor x km + 25 cor x ton
"""

def moto_carro_importe(km):
    return 30*km

def camion_importe(km,ton):
    return (30*km) + (25*ton)

def calcular_importe(vehiculo_a_circular):
    vehiculos = ["bicicleta","moto","carro","camion"]

    for vehiculo in vehiculos:
        if vehiculo_a_circular == "moto" or vehiculo_a_circular == "carro":
            km = int(input("cuantos km recorrera su vehiculo ligero?\n"))
            return moto_carro_importe(km)
        elif vehiculo_a_circular == "camion":
            km = int(input("cuantos km recorrio con su camion?\n"))
            ton = int(input("cuantas tonealdas pesa su camion?\n"))
            return camion_importe(km,ton)
        elif vehiculo_a_circular == "bicicleta":
            return 100
        else:
            return 0


#to-do funcion que agarre km/ton

def main():
    while True:
        print("\n--- Calculadora de Importes ---")
        print("1. Agregar vehículo")
        print("2. Salir")
        opcion = input("Seleccione una opción (1/2): ")

        if opcion == "1":
            vehiculo = input("¿Qué vehículo? (bicicleta/moto/carro/camion): ").lower()
            importe = calcular_importe(vehiculo)
            print(f"El importe a pagar es: {importe} cordobas")
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")



main()
