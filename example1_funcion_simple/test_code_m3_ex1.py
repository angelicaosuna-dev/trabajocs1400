# test_lanzar_dado.py
# Archivo de pruebas con pytest para la función lanzar_dado.

import pytest
import random

# Se asume que el archivo del estudiante se llama 'lanzar_dado_estudiante.py'
try:
    # TODO: Cambia 'solution_m3_ex1' por 'student_code_m3_ex1' si estás usando el código del estudiante.
    # from solution_m3_ex1 import lanzar_dado
    from student_code_m3_ex1 import lanzar_dado
except ImportError:
    pytest.fail(
        "No se pudo importar la función 'lanzar_dado' del archivo 'lanzar_dado_estudiante.py'.")


def test_tipo_de_retorno():
    """
    Verifica que la función devuelve un número entero (int).
    """
    resultado = lanzar_dado()
    assert isinstance(
        resultado, int), f"El valor devuelto debería ser un entero, pero fue de tipo {type(resultado)}."


def test_rango_del_resultado():
    """
    Llama a la función muchas veces para verificar que el resultado
    siempre está dentro del rango esperado [1, 6].
    """
    resultados_posibles = [1, 2, 3, 4, 5, 6]
    for _ in range(100):  # Llama a la función 100 veces
        resultado = lanzar_dado()
        assert resultado in resultados_posibles, f"El resultado {resultado} está fuera del rango esperado (1-6)."


def test_retorna_un_valor():
    """
    Verifica que la función no devuelve None.
    """
    assert lanzar_dado() is not None, "La función no está devolviendo ningún valor. Revisa la sentencia 'return'."


def test_usa_random_randint(monkeypatch):
    """
    Prueba avanzada: Verifica que la función está utilizando `random.randint`.
    `monkeypatch` nos permite "engañar" a una función para que se comporte
    como queremos durante una prueba.
    """
    # Haremos que `random.randint` siempre devuelva 5
    monkeypatch.setattr(random, 'randint', lambda a, b: 5)

    resultado = lanzar_dado()
    assert resultado == 5, "La función no parece estar usando `random.randint` para devolver su resultado."


# --------------------------------------------------------------------------
# Instrucciones para usar este archivo:
#
# 1. Guarda el código del estudiante como 'lanzar_dado_estudiante.py'.
# 2. Guarda este archivo como 'test_lanzar_dado.py' en el mismo directorio.
# 3. Abre una terminal, navega a ese directorio y ejecuta 'pytest'.
# --------------------------------------------------------------------------
# make this module executable
if __name__ == "__main__":
    # If the tests pass, print a success message
    if pytest.main([__file__]) == 0:
        print("✅ Pruebas pasadas para el ejercicio de variables.")
    # If the tests fail, print an error message
    else:
        print("❌ Error en el código")
        print("Este módulo no se puede ejecutar directamente. Usa pytest para correr las pruebas.")
