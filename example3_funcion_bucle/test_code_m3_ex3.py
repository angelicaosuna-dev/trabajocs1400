# test_dibujar_rectangulo.py
# Archivo de pruebas con pytest para la función dibujar_rectangulo.

import pytest

# Se asume que el archivo del estudiante se llama 'student_code_m3_ex3.py'
try:
    # TODO: Cambia 'solution_m3_ex3' por 'student_code_m3_ex3' si estás usando el código del estudiante.
    # from solution_m3_ex3 import dibujar_rectangulo
    from student_code_m3_ex3 import dibujar_rectangulo
except ImportError:
    pytest.fail(
        "No se pudo importar la función 'dibujar_rectangulo' del archivo 'solution_m3_ex3.py'.")


def test_rectangulo_simple(capsys):
    """Prueba un rectángulo simple de 5x4 con el caracter 'H'."""
    dibujar_rectangulo('H', 5, 4)
    captured = capsys.readouterr()

    # Construir la salida esperada
    fila = "H" * 5 + "\n"
    salida_esperada = fila * 4

    assert captured.out == salida_esperada


def test_rectangulo_con_otro_caracter(capsys):
    """Prueba un rectángulo de 10x3 con el caracter '*'."""
    dibujar_rectangulo('*', 10, 3)
    captured = capsys.readouterr()

    fila = "*" * 10 + "\n"
    salida_esperada = fila * 3

    assert captured.out == salida_esperada


def test_rectangulo_con_cadena_larga(capsys):
    """Prueba un rectángulo con una cadena de varios caracteres como 'ladrillo'."""
    dibujar_rectangulo('XO', 7, 2)
    captured = capsys.readouterr()

    fila = "XO" * 7 + "\n"
    salida_esperada = fila * 2

    assert captured.out == salida_esperada


def test_rectangulo_una_fila(capsys):
    """Prueba un rectángulo de una sola fila (alto = 1)."""
    dibujar_rectangulo('#', 8, 1)
    captured = capsys.readouterr()

    salida_esperada = "#" * 8 + "\n"

    assert captured.out == salida_esperada


def test_rectangulo_una_columna(capsys):
    """Prueba un rectángulo de una sola columna (ancho = 1)."""
    dibujar_rectangulo('@', 1, 5)
    captured = capsys.readouterr()

    fila = "@" + "\n"
    salida_esperada = fila * 5

    assert captured.out == salida_esperada


def test_rectangulo_vacio(capsys):
    """Prueba un rectángulo con alto 0. No debería imprimir nada."""
    dibujar_rectangulo('Z', 10, 0)
    captured = capsys.readouterr()

    assert captured.out == ""

# --------------------------------------------------------------------------
# Instrucciones para usar este archivo:
#
# 1. Guarda el código del estudiante como 'dibujar_rectangulo_estudiante.py'.
# 2. Guarda este archivo como 'test_dibujar_rectangulo.py' en el mismo directorio.
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
