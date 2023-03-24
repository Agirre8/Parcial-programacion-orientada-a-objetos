class Cuenta:
    def __innit__(self):
        self.id = None
        self.titular = None
        self.apetura = None
        self.numeroCuenta = None
        self.saldo = None

        
    
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


cuenta = Cuenta()
cuenta.retirar(2000, 300)
cuenta.ingresar(2000, 445)
cuenta.transferir(2000, 300)
