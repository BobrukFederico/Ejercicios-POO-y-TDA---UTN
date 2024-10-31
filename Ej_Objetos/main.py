from Clases.Libro import *
from Clases.Rectangulo import *
from Clases.Calculadora import *
from Clases.Animal import *
from Clases.Gato import *
from Clases.Perro import *
from Clases.Cuenta_bancaria import *

libro_1 = Libro(1, "Deep Work", "Cal Newport", 2019)

libro_1.retornar_descripcion()


rectangulo_1 = Rectangulo(5,6)

area_rectangulo = rectangulo_1.calcular_area()

print(area_rectangulo)

calculadora = Calculadora(10,5)

sumar = calculadora.sumar()
print(sumar)

animal = Animal("Fede")

perro = Perro("Fede")

gato = Gato("Simon")

perro.caminar()

perro.ladrar()

gato.caminar()

gato.maullar()


cuenta_bancaria = Cuenta_bancaria("Fede", 1000)

cuenta_bancaria.obtener_saldo()
cuenta_bancaria.depositar_saldo(200)
cuenta_bancaria.obtener_saldo()
cuenta_bancaria.retirar_saldo(700)
cuenta_bancaria.obtener_saldo()
cuenta_bancaria.retirar_saldo(700)
cuenta_bancaria.obtener_saldo()

#print(cuenta_bancaria.__saldo)
print(cuenta_bancaria.titular)