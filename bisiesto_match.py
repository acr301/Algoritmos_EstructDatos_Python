
def bisiesto(year):
    match (year % 400, year % 100, year % 4):
        case (0, _, _):  # Divisible entre 400 → siempre bisiesto
            return True
        case (_, 0, _):  # Divisible entre 100 pero no 400 → no bisiesto
            return False
        case (_, _, 0):  # Divisible entre 4 pero no entre 100 → bisiesto
            return True
        case _:  # Cualquier otro caso
            return False


anio = int(input("que anio desea verificar si es bisiesto ?"))

print(bisiesto(anio))
