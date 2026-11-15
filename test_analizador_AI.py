from analizador import contar_frecuencias_texto


def test_frecuencias_basico():
    resultado = contar_frecuencias_texto("gatito gatito gato")
    assert resultado["gatito"] == 2
    assert resultado["gato"] == 1


def test_frecuencias_vacio():
    resultado = contar_frecuencias_texto("")
    assert resultado == {}


def test_frecuencias_mayusculas():
    resultado = contar_frecuencias_texto("MIAU miau Miau MiAu")
    assert resultado["miau"] == 4
