# Tarea-1 Tomás Couso Coddou
Repositorio para la Tarea 1 del curso IIC2613 - Inteligencia Artificial (2022-1).

## Comentarios Generales

Se resolvió la totalidad de la tarea con excepcíon del bonus, que no fue implementado. Al mismo tiempo, en los casos 5 y 8 de DCCajas se observa un comportamiento suboptimal. En el caso 5, uno de los robots llega a la meta y se mantiene ahí, pero el otro (que no lleva caja) realiza movimientos sin motivo alguno. En el caso 8, dos robots ejecutan la acción de esperar en una ocasión, cuando al no hacerlo llegarían un instante antes a la meta. Más allá de esos dos casos, el comportamiento de los robots es aparentemente óptimo.

## Ejecución

Para ejecutar DCClue y visualizar el resultado en el archivo ``output.txt``, se debe ejecutar desde el directorio ``01 - DCClue`` el siguiente comando:

``./run.sh -n <prob_number>``

Donde `<prob_number>` corresponde al número de problema que se quiere ejecutar.

Para visualizar el resultado en consola, se debe ejecutar el siguiente comando:

``./run_model.sh -n <prob_number>``

Para ejecutar DCCajas y visualizar el resultado en el archivo ``robot.html``, se debe ejecutar desde el directorio ``02 - DCCajas`` el siguiente comando:

``./run.sh -n <prob_number>``

Para visualizar el resultado en consola, se debe ejecutar el siguiente comando:

``./run_model.sh -n <prob_number>``

## Preguntas escritas

La respuesta de la pregunta "IA y un mundo mejor", y la descripción de la lógica utilizada al optimizar el resultado de DCCajas se encuentran en el directorio raíz, en el archivo ``respuestas.pdf``.
