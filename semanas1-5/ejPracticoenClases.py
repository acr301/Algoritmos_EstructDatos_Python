"""

introducir un entero impar n entre 1 y 19

serie numerica 1 + 3 + 5 + ... + n 



"""


R = range(1,21,2)

def suma_rango(r_buscado):
    suma = 0
    for i in r_buscado:
        suma += i
    return suma

def multiplicacion_rango(r_buscado):
    producto = 1
    for i in r_buscado:
        producto *= i
    return producto

def encontrar_rango(n_buscado):
    r_buscado = range(0,0)
    for i in R:
        if i == n_buscado:
            r_buscado = range(1,i+1,2)
    return r_buscado

def main():

    n_buscado = int(input(" inserte el numero impar entre 1 y 19 a buscar: "))
    if n_buscado % 2 == 0 or n_buscado > 19:
        return print("entrada invalida")


    r_buscado = encontrar_rango(n_buscado)

    print(suma_rango(r_buscado))
    print(multiplicacion_rango(r_buscado))

main()

