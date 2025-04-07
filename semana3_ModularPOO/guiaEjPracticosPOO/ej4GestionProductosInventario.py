"""
Diseñar una clase Producto que incluya atributos como código, nombre, precio y
cantidad en stock. Además, los estudiantes deberán implementar una clase
Inventario que administre una colección de objetos Producto, incorporando
métodos para agregar, buscar, actualizar y eliminar productos. Este ejercicio
permite modelar situaciones reales de gestión de ventas y refuerza el concepto
de encapsulación y manejo de colecciones en programación orientada a objetos.

"""

# Composicion : Inventario tiene (contiene) objetos de Producto

class Producto:
    def __init__(self, codigo, nombre, precio, cantidadEnStock):
        self.codigo = codigo 
        self.nombre = nombre
        self.precio = precio
        self.cantidadEnStock = cantidadEnStock

    def mensaje(self):
        return f"""
        Producto = {self.codigo}
        Nombre = {self.nombre}
        Precio = {self.precio}
        Stock = {self.cantidadEnStock}
        """


class Inventario:
    def __init__(self):
        # lista de objetos de Producto
        self.productos = []


    # es composicion ya que estos metodos acceden a los atributos de la clase Producto
    def agregar_producto(self, producto):
        self.productos.append(producto)

    def buscar_producto(self,codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None


    # pasamos los nuevos como "None" porque asi hace los agumentos opcionales, y si no es modificado
    # queda bien perfectamente como un valor Nulo
    def actualizar_producto(self, codigo, nuevo_nombre=None, nuevo_precio=None, nuevo_cantidadEnStock=None):
        

        # reutilizamos buscar_producto (modularmente, para saber cual producto modificar)
        producto = self.buscar_producto(codigo)
        

        # si hay un objeto Producto es True, si es None es False
        if producto:

            # notese como usamos comparadores de identidad, None es un mismo objeto 
            # singleton (unico) para todas las comparaciones,
            # entonces is not None compara que ocupen el mismo 
            # espacio en memoria (comparacion de referencia, no de valor)
            if nuevo_nombre is not None:
                producto.nombre = nuevo_nombre
            if nuevo_precio is not None:
                producto.precio = nuevo_precio
            if nuevo_cantidadEnStock is not None:
                producto.cantidadEnStock = nuevo_cantidadEnStock
            return True 
        return False

    def eliminar_producto(self,codigo):
        producto = self.buscar_producto(codigo)
        if producto:
            self.productos.remove(producto)
            return True
        return False

