TARIFFA_BASE = 5.95
IVA = 10
TARIFFA_LITRO = 0.04
SPESA_POSTALE = 0.85



def tariffa_base(numero):
    return numero * TARIFFA_BASE


def tariffa_raccolta(numero):
    return numero * TARIFFA_LITRO

def somma(n1,n2):
    return n1+n2

def prezzo_iva(numero):

    return (numero * IVA)/100   