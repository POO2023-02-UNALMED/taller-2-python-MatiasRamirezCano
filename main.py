class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    def cambiarColor(self, color):
        colores = ['rojo','verde','amarillo','negro','blanco']
        if color in colores:
            self.color = color

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self. registro = registro
    def cambiarRegistro(self, registro):
        self.registro = registro
    def asignarTipo(self, tipo):
        if (tipo == 'electrico' or tipo == 'gasolina'):
            self.tipo = tipo

class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
    def verificarIntegridad(self):
        if self.registro == self.motor.registro:
            for i in range(asientos.len):
                if asientos[i].registro != self.registro:
                    return('Las piezas no son originales')
            return('Auto original')
        else:
            return('Las piezas no son originales')
    def cantidadAsientos(self):
        numAsientos = 0
        for i in range(asientos.len):
            if isinstance(asiento[i], Asiento):
                numAsientos += 1
        return numAsientos