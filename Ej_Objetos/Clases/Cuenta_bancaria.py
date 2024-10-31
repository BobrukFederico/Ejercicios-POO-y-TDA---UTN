class Cuenta_bancaria:
    def __init__(self, titular: str, saldo: float):
        self.titular = titular
        self.__saldo = saldo

    def obtener_saldo(self):
        print(f"Tu saldo es de: {self.__saldo} $")

    def depositar_saldo(self, saldo_depositado: float):
        if saldo_depositado > 0:
            print("Se deposito exitosamente")
            self.__saldo += saldo_depositado
            return self.__saldo
        else:
            print("Error. Tiene que depositar mas de 0")
    
    def retirar_saldo(self, cantidad_retirar: float):
        if cantidad_retirar <= self.__saldo:
            print("Se retiro exitosamente")
            self.__saldo -= cantidad_retirar
            return self.__saldo
        else:
            print("No se puede retirar, porque el saldo es negativo")
    
    @property
    def saldo(self):
        return self.__saldo