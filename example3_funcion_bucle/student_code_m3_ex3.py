# --------------------------------------------------------------------------
#          FUNCIÓN PARA DIBUJAR UN RECTÁNGULO CON UN CARACTER
# --------------------------------------------------------------------------
# Descripción:
# El objetivo es crear una función que dibuje en la consola un rectángulo
# de un ancho y alto específicos, utilizando una cadena de texto dada.
#
# Instrucciones para el estudiante:
# 1. Completa la función `dibujar_rectangulo`.
# 2. La función debe aceptar tres argumentos: `caracter`, `ancho` y `alto`.
# 3. La función no debe devolver nada (no usar `return`), solo debe imprimir
#    directamente en la consola.
# 4. Usa un bucle `for` que se repita `alto` veces para dibujar cada fila.
# 5. En cada iteración del bucle, imprime una línea que consista en el
#    `caracter` repetido `ancho` veces. Puedes multiplicar una cadena por
#    un entero para repetirla (ej. `'H' * 5` produce `'HHHHH'`).
# --------------------------------------------------------------------------

def dibujar_rectangulo(caracter, ancho, alto):
    """
    Dibuja un rectángulo en la consola.

    Args:
      caracter (str): La cadena de texto para usar como "ladrillo".
      ancho (int): El número de veces que se repetirá el caracter en cada fila.
      alto (int): El número de filas que tendrá el rectángulo.
    """
    # TODO: Paso 1. Crea un bucle que se ejecute `alto` veces.
    #         Usa `range(alto)` para controlar el número de filas.
    # for i in range( ... ):
    # TODO: Paso 2. Dentro del bucle, imprime la fila.
    #         La fila es el `caracter` repetido `ancho` veces.
    # print( ... )
    for i in range(alto): # Borra 'pass' cuando escribas tu código
        print(caracter * ancho)


# --- Bloque para probar tu función ---
# Este código es para que pruebes tu función. No se calificará.
if __name__ == "__main__":
    print("Ejemplo 1: Rectángulo de 5x4 con 'H'")
    dibujar_rectangulo('H', 5, 4)

    print("\nEjemplo 2: Rectángulo de 10x3 con '*'")
    dibujar_rectangulo('*', 10, 3)

    print("\nEjemplo 3: Rectángulo de 7x2 con 'XO'")
    dibujar_rectangulo('XO', 7, 2)
