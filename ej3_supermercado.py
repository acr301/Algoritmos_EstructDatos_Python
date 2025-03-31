
DESCUENTO_NORMAL = 0.10
DESCUENTO_MAS_DE_3_12 = 0.15
PRECIO_UNITARIO = 10



def supermercado_menu():
        print(
            '''
            SUPERMERCADO
            
            1. comprar Limones
                precio unidad = C$ 10.00
                ahora con descuento del 10% 
                al comprar mas de 3 docenas, 15% y una unidad obsequio por cada docena


            2. salir

            '''
        )

"""
SUPERMERCADO 
----
Monto Compra: C$ {monto_compra}
Monto Descuento: C$ {monto_descuento}
Monto a Pagar: C$ {monto_pagar}
Unidades obsequiadas: {unidades_obsequio} 
"""

def descuento_normal(monto_compra):
    monto_descuento = monto_compra * DESCUENTO_NORMAL
    return monto_descuento


# si 12 % unidades > 3
def descuento_extra(monto_compra):
        monto_descuento = monto_compra * DESCUENTO_MAS_DE_3_12
        return monto_descuento

def calcular_docenas(unidades):
    return unidades % 12

def supermercado_facturacion(unidades):
    monto_compra = unidades*PRECIO_UNITARIO
    return monto_compra

def main():
    while True:
        supermercado_menu()
        opcion = input("escoga opcion (1/2): ").strip()

        match opcion:
            case "1":
                unidades = int(input("cuantas unidades desea comprar?: "))
                monto_compra = supermercado_facturacion(unidades)



                unidades_obsequio = 0

                monto_descuento = descuento_normal(monto_compra)
                monto_pagar = (unidades*PRECIO_UNITARIO) - monto_descuento 
                total_limones = unidades


                if unidades > 36: 
                    unidades_obsequio = unidades // 12 - 3
                    monto_descuento = descuento_extra(monto_compra)
                    monto_pagar = (unidades*PRECIO_UNITARIO) - monto_descuento
                    total_limones = unidades + unidades_obsequio



                factura = f"""
                ---------------------------------

                SUPERMERCADO 
                ----
                Monto Compra: C$ {monto_compra}
                Monto Descuento: C$ {monto_descuento}
                Monto a Pagar: C$ {monto_pagar}
                Unidades obsequiadas: {unidades_obsequio} 
                

                Total Limones : {total_limones}
                ---------------------------------
                """

                print(factura)

                
            case "2":
                "gracias, buen dia"
                break
            case _:
                print("opcion invalida")

main()



