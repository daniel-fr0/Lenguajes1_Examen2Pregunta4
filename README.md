# Pruebas de efiencia de las diferentes implementaciones del algoritmo Fibonacci modificado

Se implementaron 3 algoritmos del algoritmo Fab, tal como esta descrito al inicio del archivo `f36.py`.
Se cuenta con una implementación recursiva, una recursiva con cola y una iterativa.

Para cada una de las implementaciones se realizó un script de prueba que mide el tiempo de ejecución de la función para diferentes valores de entrada.


## Como ejecutar

Se requiere tener instalado python3 y la libreria matplotlib.
Este ultimo se puede instalar con el siguiente comando:

```bash
pip install matplotlib
```
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
Si se desea realizar nuevas pruebas se puede ejecutar el script `efficiency.py` con el siguiente comando:

```bash
python efficiency.py
```
Este script realiza las pruebas de los 3 algoritmos y genera la grafica `resultados.png`.
Para las pruebas se utilizan los valores de entrada del 18 al 72 y se realizan 1000 pruebas para cada valor de entrada.
Esto porque para valores menores a 18 no se realizan llamadas recursivas y para valores mayores a 72 el tiempo de ejecución es muy alto para la implementación recursiva.

## Conclusiones

Se puede observar que la implementación iterativa y la recursiva con cola tienen un tiempo de ejecución similar,
mientras que la implementación recursiva es mucho más lenta a medida que el valor de entrada aumenta,
alejandose mucho de las otras dos implementaciones en los ultimos valores que se probaron.

Esto se debe a que la implementación recursiva realiza muchas llamadas recursivas repetidas, mientras que las otras dos implementaciones no.

El hecho de que las otras dos implementaciones tengan un tiempo de ejecución similar se debe a la optimización
que realiza el interprete de python al realizar la recursión con cola, con lo cual se obtiene una ejecución similar a la iterativa.