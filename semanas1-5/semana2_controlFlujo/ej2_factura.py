
IVA = 0.15
DESCUENTO = 0.12

# si el subtotal (precio de venta por cantidad es mayor de 1000), 12% descuento


def nueva_factura_menu():
        print(
            '''
            facturas
            1. nueva 
            2. salir
            '''
        )

"""
producto cantidad precio 
producto2 cantidad precio
 
----
subtotal        
descuento 
total 


"""

# el iva se aplica al valor del producto previo al descuento 

IVA = 0.15
DESCUENTO = 0.12


def calcular_precio(cantidad, precio_unidad):
    precio = (cantidad * precio_unidad)
    return precio

def aplicar_iva(precio_sin_iva):
    return precio_sin_iva + (precio_sin_iva * IVA)

def calcular_total(subtotal):
    if subtotal > 1000:
        return subtotal - (subtotal * DESCUENTO)
    else:
        return aplicar_iva(subtotal)





def main():
    while True:
        nueva_factura_menu()
        opcion = input("escoga opcion (1/2): ").strip()

        match opcion:
            case "1":
                producto = input("inserte nombre del producto: \n")
                precio_unidad = float(input("inserte el precio unitario: \n"))
                cantidad = int(input("inserte la cantidad: \n"))

                precio = calcular_precio(cantidad, precio_unidad)
                precio_con_iva = aplicar_iva(precio)
                total = calcular_total(precio_con_iva)

                if (total != precio_con_iva):
                    descuento = "12% aplicado"

                descuento = "no aplica ningun descuento"
                    

                factura = f"""
                ---------------------------------
                FACTURA          
                ---------------------------------
                Producto: {producto}
                Cantidad: {cantidad}
                Precio Unitario: ${precio_unidad:}

                ---------------------------------
                Subtotal: ${precio}
                IVA (15%): ${precio_con_iva}
                Descuento: {descuento}
                ---------------------------------
                TOTAL: ${total}
                ---------------------------------
                """

                print(factura)

                
            case "2":
                "gracias, buen dia"
                break
            case _:
                print("opcion invalida")




main()
