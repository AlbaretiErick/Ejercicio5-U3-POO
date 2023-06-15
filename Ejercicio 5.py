from zope.interface import Interface, implementer
from zope.interface.exceptions import Invalid
class PosicionInvalidaException(Exception):
    pass

class IColeccion(Interface):
    def insertarElemento(elemento, posicion):
        pass
    def agregarElemento(elemento):
        pass
    def mostrarElemento(posicion):
        pass

@implementer(IColeccion)
class Coleccion:
    def __init__(self):
        self.data = []
    def insertarElemento(self, elemento, posicion):
        if posicion < 0 or posicion > len(self.data):
            raise PosicionInvalidaException("La posición no es válida")
        self.data.insert(posicion, elemento)
    def agregarElemento(self, elemento):
        self.data.append(elemento)
    def mostrarElemento(self, posicion):
        if posicion < 0 or posicion >= len(self.data):
            raise PosicionInvalidaException("La posición no es válida")
        elemento = self.data[posicion]
        print(elemento)

coleccion = Coleccion()
try:
    coleccion.insertarElemento("Elemento 1", 0)
    coleccion.insertarElemento("Elemento 2", 1)
    coleccion.insertarElemento("Elemento 3", 2)
except PosicionInvalidaException as e:
    print(e)
coleccion.agregarElemento("Elemento 4")
try:
    coleccion.mostrarElemento(1)
except PosicionInvalidaException as e:
    print(e)