import timeit
import matplotlib.pyplot as plt
from f36 import f36
from f36tail import f36tail
from f36iter import f36iter

# Rango de 18 a 72 porque desde 0 a 17 es un tiempo despreciable
test_inputs = list(range(18, 72))

# Comprobamos que los resultados son iguales
for n in test_inputs:
	assert f36(n) == f36tail(n) == f36iter(n)

# Se ejecuta cada funcion 1000 veces para cada n
times_f36 = [timeit.timeit(lambda: f36(n), number=1000) for n in test_inputs]
times_f36tail = [timeit.timeit(lambda: f36tail(n), number=1000) for n in test_inputs]
times_f36iter = [timeit.timeit(lambda: f36iter(n), number=1000) for n in test_inputs]

# Plot de los resultados
plt.figure(figsize=(10, 6))
plt.title('Comparación de tiempos de ejecución de distintas implementaciones de f36')
plt.plot(test_inputs, times_f36, label='recursivo')
plt.plot(test_inputs, times_f36tail, label='recursivo de cola')
plt.plot(test_inputs, times_f36iter, label='iterativo')
plt.xlabel('Tamaño de la entrada (n)')
plt.ylabel('Tiempo de ejecución (s)')
plt.legend()

# Se guarda el plot en un archivo
plt.savefig('resultados.png')

# Se muestra el plot
plt.show()