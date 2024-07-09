
def validar_rut(rut: str) -> bool:

    rut = rut.replace(".", "").upper()
    if not '-' in rut:
        return False
    numero, dv = rut.split("-")
    if not numero.isdigit():
        return False
    numero = int(numero)
    
    def calcular_dv(n: int) -> str:
        suma = 0
        multiplicador = 2
        while n > 0:
            suma += (n % 10) * multiplicador
            n = n // 10
            multiplicador += 1
            if multiplicador == 8:
                multiplicador = 2
        dv = 11 - (suma % 11)
        if dv == 11:
            return '0'
        elif dv == 10:
            return 'K'
        else:
            return str(dv)
    
    return calcular_dv(numero) == dv