class MetodoPagoBase():
    def procesar_pago():
        pass

class MetodoPagoAutomatico(MetodoPagoBase):
    def procesar_pago(self, cantidad):
        pass

class MetodoPagoManual(MetodoPagoBase):
    def procesar_pago(self, cantidad):
        pass


#Metodos de pago automáticos
class PagoTarjeta(MetodoPagoAutomatico):
    def __init__(self, num_tarjeta):
        self.num_tarjeta = num_tarjeta
    
    def procesar_pago(self, cantidad):
        print(f"Procesando el pago automatico de {cantidad} usando tarjet: {self.num_tarjeta}")

class PagoPayPal(MetodoPagoAutomatico):
    def __init__(self, cuenta_Paypal):
        self.cuenta_Paypal = cuenta_Paypal

    def procesar_pago(self, cantidad):
        print(
            f"Procesando el pago automatico de {cantidad} usando la cuenta PayPal: {self.cuenta_Paypal}")
        
class PagoBitcoin(MetodoPagoAutomatico):
    def __init__(self, direccion_bitcoin):
        self.direccion_bitcoin = direccion_bitcoin

    def procesar_pago(self, cantidad):
        print(f"Procesando el pago automatico de {cantidad} usando la transaccion bitcoin: {self.direccion_bitcoin}")

#Metodo de pago manual

class PagoCheque(MetodoPagoManual):
    def __init__(self, num_cheque):
        self.num_cheque = num_cheque

    
    def procesar_pago(self, cantidad):
        print(f"Procesando pago manual de la {cantidad} usando cheque: {self.num_cheque}")


def realizar_pago_automatico(metodo_pago:MetodoPagoAutomatico, cantidad):
    metodo_pago.procesar_pago(cantidad)

def realizar_pago_manual(metodo_pago:MetodoPagoManual, cantidad):
    metodo_pago.procesar_pago(cantidad)


#Instanciar clases
pago_tarjeta = PagoTarjeta("1234 4567 5678")
pago_paypal = PagoPayPal("cuenta_example@example.com")
pago_bitcoin = PagoBitcoin("hggfjyj76esdf322")
pago_cheque = PagoCheque("1010293847")

realizar_pago_automatico(pago_tarjeta, 700)
realizar_pago_automatico(pago_paypal, 700)
realizar_pago_automatico(pago_bitcoin, 700)
realizar_pago_manual(pago_cheque, 700)

