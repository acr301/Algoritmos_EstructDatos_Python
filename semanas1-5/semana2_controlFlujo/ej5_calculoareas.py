

def superficies_menu():
    print("""
    
    ==============================================================
    CALCULO DE SUPERICIES (version 1.0)

    1. Cuadrado     lado*lado 
    2. Circulo      pi*radio*radio 
    3. Rectangulo   base*altura 
    4. Trapecio     (base1 + base2) * altura / 2 
    5. Triangulo    (base*altura)/2
    ==============================================================
          """)


PI = 3.1416

def area_cuadrado(lado):
    return lado*lado 

def area_circulo(radio):
    return PI*radio*radio 

def area_rectangulo(base,altura):
    return base*altura

def area_trapecio(base1,base2,altura):
    return (base1+base2) * altura/2 

def area_triangulo(base,altura):
    return (base*altura)/2



def main():
    while True:
        superficies_menu()
        opcion = input("escoga opcion del 1 al 5 o cualquier otra tecla para salir: \n").strip()

        match opcion:
            case '1':
                lado = int(input(" inserte medida del lado: "))
                area = area_cuadrado(lado)
                mensaje = f"su cuadrado tiene un area de {area}\n"
                print(mensaje)
            case '2':
                radio = int(input(" inserte radio del circulo:"))
                area = area_circulo(radio)

                mensaje = f"su circulo tiene un area de {area}\n"
                print(mensaje)


            case '3':
                base = int(input(" inserte base del rectangulo: "))
                altura = int(input(" inserte altura del rectangulo: "))
               

                area = area_rectangulo(base, altura)
                mensaje = f"su rectangulo tiene un area de {area}\n"
                print(mensaje)


            case '4':
                base1 = int(input(" inserte base 1 del trapecio: "))
                base2 = int(input(" inserte base 2 del trapecio: "))
                altura = int(input(" inserte altura del trapecio: \n"))


                area = area_trapecio(base1,base2,altura)
                mensaje = f"su trapecio tiene un area de {area}\n"
                print(mensaje)


            case '5':
                base = int(input(" inserte base del triangulo: "))
                altura = int(input(" inserte altura del triangulo: "))


                area = area_triangulo(base,altura)
                mensaje = f"su triangulo tiene un area de {area}\n"
                print(mensaje)


            case _:
                print("saliendo del programa")
                break

main()
