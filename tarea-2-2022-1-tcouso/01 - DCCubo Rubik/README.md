# Dependencias
Para poder ejecutar el programa necesitas la librería `RCube`. Puedes instalarla con pip con el siguiente comando:
```
pip install rubik-cube
```
La librería pandas fue empleada para el análisis de datos de la simulación. Puede instalarse con el siguiente comando:
```
pip install pandas
```
# Ejecución
* Para ejecutar el programa debes correr el módulo `main.py`. Solo necesitas modificar los archivos `astar.py` y `heuristics.py`.

* Puedes evaluar tu algoritmo utilizando los cubos de ejemplo para inicializar un cubo que están en el archivo de texto `cubos_ejemplo.txt`.

* En el archivo `main.py` puedes ver que se crea un archivo de texto llamado `parsed.txt`. Esto es para utilizar el visualizador 3D mostrado en la cápsula correspondiente.

# Consideraciones
Las heurísticas fueron implementadas en el módulo `heuristics.py`. Las tres heurísticas fueron implementadas en base a la funcion `corner_distances`, del módulo `heuristics_utilities.py`. Dicha función retorna un iterable de todas las distancias entre las esquinas de un cubo y el cubo resuelto.

Para efectos de la comparación de las tres heurísticas implementadas (no fue implementado el bonus) se armó el set de cubos `cubos_testeo.txt`. El archivo `main.py` fue modificado para resolver los cubos de dicho archivo con las tres heurísticas implementadas. Los datos de ejecución de dichos cubos son almacenados en los archivos `min.csv`, `max.csv` y `sum.csv`.

Si se quiere ver al detalle el análisis de los datos de las soluciones a los cubos de testeo, puede referirse al notebook `testcubes-analysis.ipynb`.

Por último, las demostraciones solicitadas y la comparación de las heurísticas en los cubos de ejemplo se encuentran detalladas en el archivo `respuestas.pdf`.

