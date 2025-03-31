


"""
131 < el primero y el ultimo del string sean el mismo 
"""
def capicua_menu():
    print(
        '''
        capicua de tres cifras
        1. nueva
        2. salir
        '''
    )

def capicua(numero):
    if len(numero) > 3 or len(numero) < 3:
        return "debe insertar un numero de 3 cifras"
    elif numero[0] == numero[2]:
        return True
    return False

def main():
    while True:
        capicua_menu()
        opcion = input("escoga opcion (1/2): ").strip()

        match opcion:
            case '1':
                numero = input("inserte un numero de 3 cifras: ")
                print(capicua(numero))
            case '2':
                print("saliendo del programa... ")
                break
            case _:
                print("opcion invalida")
                continue



main()
