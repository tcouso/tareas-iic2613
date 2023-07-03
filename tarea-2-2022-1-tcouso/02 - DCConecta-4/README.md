# Dependencias
La librería pandas fue empleada para el análisis de datos de la simulación. Puede instalarse con el siguiente comando:
```
pip install pandas
```

# Ejecución
Para ejecutar el programa debes correr el módulo `main.py`. Solo necesitas modificar los archivos `minimax.py` y `score.py`.

# Consideraciones

El módulo `main.py`fue modificado para aleatorizar las primeras jugadas de cada agente y para entregar un diccionario listo para ser transformado en una dataframe de pandas.

Para correr las simulaciones, debe ejecutarse el módulo `simulate.py`, procurando de asignar a la variable `N` la cantidad deseada de juegos a simular. Los resultados de la simulación se almacenan en el archivo `N-simulations.csv`.
Para ver más detalles del análisis llevado a cabo con los datos de la simulación de 100 juegos, puede revisarse el notebook `simulation-analysis.ipynb`.

Las respuestas sobre la comparación de rendiimento de las dos funciones de evaluación implementadas (el bonus no fue implementado) puede encontrarse en el archivo `estudio.pdf`.