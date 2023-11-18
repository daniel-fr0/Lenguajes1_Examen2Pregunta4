# Pruebas de efiencia de las diferentes implementaciones del algoritmo Fibonacci modificado

Se implementaron 3 algoritmos del algoritmo Fab, tal como esta descrito al inicio del archivo `f36.py`.
Se cuenta con una implementación recursiva, una recursiva con cola y una iterativa.

Para cada una de las implementaciones se realizó un script de prueba que mide el tiempo de ejecución de la función para diferentes valores de entrada.


## Como ejecutar

Para ejecutar el script de prueba de una implementación se debe ejecutar el siguiente comando:

```bash
python <archivo>
```

Donde `<archivo>` puede ser `f36.py` para la implementación recursiva,
`f36tail.py` para la implementación recursiva con cola o `f36iter.py` para la implementación iterativa.

Cada uno imprime en pantalla los primeros 72 valores de la secuencia de `f36`.


## Resultados

Se cuenta con una grafica que muestra el tiempo de ejecución de cada una de las implementaciones para diferentes valores de entrada.
Esta grafica se encuentra en el archivo `resultados.png`.

## Conclusiones

Se puede observar que la implementación iterativa y la recursiva con cola tienen un tiempo de ejecución similar,
mientras que la implementación recursiva es mucho más lenta a medida que el valor de entrada aumenta,
alejandose mucho de las otras dos implementaciones en los ultimos valores que se probaron.

Esto se debe a que la implementación recursiva realiza muchas llamadas recursivas repetidas, mientras que las otras dos implementaciones no.

El hecho de que las otras dos implementaciones tengan un tiempo de ejecución similar se debe a la optimización
que realiza el interprete de python al realizar la recursión con cola, con lo cual se obtiene una ejecución similar a la iterativa.