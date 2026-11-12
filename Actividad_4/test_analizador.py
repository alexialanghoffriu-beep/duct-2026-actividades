from analizador import contar_frecuencias

def test_frecuencias_basico():
    resultado = contar_frecuencias("sol luna sol")
    assert resultado["sol"] == 2
    assert resultado["luna"] == 1

def test_frecuencias_vacio():
    resultado = contar_frecuencias("")
    assert resultado == {}

def test_frecuencias_mayusculas():
    resultado = contar_frecuencias("Sol sol SOL")
    # TODO: completa la asercion que verifica que las tres variantes de
    # "sol" (con distintas mayusculas) se cuentan como la MISMA palabra,
    # gracias al .lower() de la funcion. El resultado deberia tener
    # "sol": 3
    assert resultado["sol"] == 3
def test_frecuencias_numeros():
    resultado = contar_frecuencias("123 12 23 1 2 3 123")
    assert resultado ["12"] == 1
    assert resultado ["23"] == 1
    assert resultado ["123"] == 2
    assert resultado ["1"] == 1
    assert resultado ["2"] == 1
    assert resultado ["3"] == 1