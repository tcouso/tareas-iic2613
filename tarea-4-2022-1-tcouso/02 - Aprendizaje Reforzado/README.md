# Dependencias

Para poder ejecutar la interfaz gráfica necesitarás la librería Pygame, puedes instalarla con:
```
pip install pygame
```
# Ejecución

La tarea se ejecuta desde el módulo ```QAgent.py```.  
- La función ```train``` se emplea para entrenar al agente, y recibe como parámetro un string, que indica el alias que se le dá al archivo .csv donde se almacenan las métricas de desempeño del agente. Para el correcto funcionamiento de tal funcion, debe crearse un directorio con nombre ```data``` para almacenar los archivos generados.

- La función ```play``` ejecuta instancias de juego con el agente ya entrenado, con el objetivo de visualizar el desempeño de este.

# Almacenamiento de Q-table

- La función ```format_q_table``` crea la q table en el formato solicitado, y la funció ```save_q_table``` guarda dicha tabla en un archivo .csv con nombre ```q_table.csv```.

# Respuestas a preguntas escritas

- Las respuestas a las preguntas de las actividades 1, 2 y 4 se encuentran en el archivo ```Parte_2_T4_IA.pdf```.