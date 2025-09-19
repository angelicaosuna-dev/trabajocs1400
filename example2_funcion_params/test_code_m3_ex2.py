# test_area_rectangulo.py
# Archivo de pruebas con pytest para la función calcular_area_rectangulo.

import pytest

# Se asume que el archivo del estudiante se llama 'area_rectangulo_estudiante.py'
# y que contiene la función `calcular_area_rectangulo`.
try:
    # TODO: Cambia 'solution_m3_ex2' por 'student_code_m3_ex2' si estás usando el código del estudiante.
    # from solution_m3_ex2 import calcular_area_rectangulo
    from student_code_m3_ex2 import calcular_area_rectangulo
except ImportError:
    # Esta función de marcador se utiliza si la importación falla
    pytest.fail("No se pudo importar la función 'calcular_area_rectangulo' del archivo 'student_code_m3_ex1.py'. Asegúrate de que el archivo exista y no tenga errores de sintaxis.")


def test_area_enteros_positivos():
    """
    Prueba el cálculo del área con números enteros positivos.
    """
    assert calcular_area_rectangulo(10, 5) == 50
    assert calcular_area_rectangulo(7, 8) == 56


def test_area_con_flotantes():
    """
    Prueba el cálculo del área con números de punto flotante (decimales).
    """
    assert calcular_area_rectangulo(2.5, 4) == 10.0
    assert pytest.approx(calcular_area_rectangulo(3.5, 2.5)) == 8.75


def test_area_con_cero():
    """
    Prueba el cálculo del área cuando una de las dimensiones es cero.
    """
    assert calcular_area_rectangulo(10, 0) == 0
    assert calcular_area_rectangulo(0, 5) == 0
    assert calcular_area_rectangulo(0, 0) == 0


def test_funcion_retorna_valor():
    """
    Verifica que la función no retorne 'None'. Esto sucede si el estudiante
    olvida o comenta la sentencia 'return'.
    """
    resultado = calcular_area_rectangulo(5, 5)
    assert resultado is not None, "La función no está devolviendo ningún valor. Revisa la sentencia 'return'."


def test_parametros_orden():
    """
    Verifica que la función funciona correctamente sin importar el orden
    de los argumentos si se nombran explícitamente.
    """
    assert calcular_area_rectangulo(largo=10, ancho=5) == 50
    assert calcular_area_rectangulo(ancho=5, largo=10) == 50


# --------------------------------------------------------------------------
# Instrucciones para usar este archivo:
#
# 1. Guarda el código del estudiante como 'area_rectangulo_estudiante.py'.
# 2. Guarda este archivo como 'test_area_rectangulo.py' en el mismo directorio.
# 3. Abre una terminal, navega a ese directorio y ejecuta 'pytest'.
# 4. Pytest encontrará y ejecutará las pruebas automáticamente.
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
