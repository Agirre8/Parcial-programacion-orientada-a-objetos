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

cuenta = Cuenta()
cuenta.retirar(2000, 300)
cuenta.ingresar(2000, 445)

