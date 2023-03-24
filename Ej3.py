import random as rd

class Cuenta:
    def __innit__(self):
        self.id = None
        self.titular = None
        self.apetura = None
        self.vencimiento = None
        self.numeroCuenta = None
        self.saldo = None

    def setearCuenta(self): 
        print("----------------------------") 
        print("Creando cuenta bancaria...")  
        print("----------------------------")   
        self.id  = 119274557823
        self.titular  = input("Introduzca su nombre: ")
        self.apertura  = 2
        self.vencimiento = 28
        print("Datos de la cuenta: \n ID de la cuenta: {}\n Titular de la cuenta: {}\n Fecha de apertura: {} de noviembre de 2017 \n Fecha de vencimiento: {} de octubre de 2025".format((self.id), (self.titular), (self.apertura), (self.vencimiento)))

    
    def retirar(self, saldo, retirar):
        self.saldo = saldo
        self.retirar = retirar
        if saldo > retirar:
            saldo = saldo - retirar
            print("Ha retirado {} euros, su saldo ahora es de {} euros".format((retirar), (saldo)))
        else:
            print("Saldo insuficiente")

    def ingresar(self, saldo, ingresar):
        self.saldo = saldo
        self.ingresar = ingresar
        saldo = saldo + ingresar
        print("Ha ingresado {} euros, su saldo ahora es de {} euros".format((ingresar), (saldo)))

    def transferir(self, saldo, transferir):
        self.saldo = saldo
        self.transferir = transferir
        numeroCuenta2 = input("Ingrese el número de cuenta al que le va ha transferir el dinero: ")

        if saldo > transferir:
            saldo = saldo - transferir
            print("Ha transferido {} euros a la siguiente cuenta bancaria: {}, su saldo ahora es de {} euros".format((transferir), (numeroCuenta2), (saldo)))
        else:
            print("Saldo insuficiente")


class PlazoFijo(Cuenta):
    def __innit__(self):
        super().__innit__()

    def retirarFijo(self, fecha, vencimiento):
        self.fecha = fecha
        self.vencimiento = vencimiento
        
        if fecha < vencimiento:
            print("Dinero transferido con exito")
        else:
            print("Dinero transferido con una comisión del 5 porciento")
