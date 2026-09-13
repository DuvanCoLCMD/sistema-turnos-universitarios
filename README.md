Aplicación de sistema de turnos universitarios utilizando una estructura de datos tipo cola.
# Sistema de Turnos Universitarios

## 1. Nombre de la aplicación

**Sistema de Turnos Universitarios**

## 2. Descripción no técnica del problema

En una universidad es necesario organizar la atención de los estudiantes de manera ordenada. Cuando varios estudiantes necesitan realizar una consulta o recibir atención, se debe respetar el orden en el que llegaron para evitar confusiones y garantizar una atención justa.

El problema consiste en organizar a los estudiantes que esperan atención y determinar quién debe ser atendido en cada momento.

## 3. Descripción de la solución

La aplicación permite registrar estudiantes en una lista de espera, consultar cuál es el siguiente estudiante que debe ser atendido y atender los turnos respetando el orden de llegada.

También se controlan situaciones especiales, como intentar atender cuando no hay estudiantes esperando o intentar agregar un estudiante cuando la capacidad máxima de la cola ya fue alcanzada.

## 4. Estructura de datos seleccionada

La estructura de datos utilizada es una **cola (Queue)**.

La cola trabaja bajo el principio **FIFO (First In, First Out)**, que significa "primero en entrar, primero en salir".

Por ejemplo, si los estudiantes llegan en este orden:

1. Andrés Castor
2. Angela Gómez
3. Carlos Rodríguez

El orden de atención será:

1. Andrés Castor
2. Angela Gómez
3. Carlos Rodríguez

## 5. Justificación técnica de la elección

Se seleccionó una cola porque el problema requiere mantener el orden de llegada de los estudiantes.

La aplicación utiliza diferentes operaciones para controlar la estructura:

* `agregar_turno()`: agrega un estudiante al final de la cola.
* `atender_turno()`: atiende y retira al estudiante que está en el frente.
* `siguiente_turno()`: permite consultar quién será atendido próximamente.
* `mostrar_cola()`: muestra los estudiantes que están esperando.
* `esta_vacia()`: verifica si la cola no contiene estudiantes.
* `esta_llena()`: verifica si se alcanzó la capacidad máxima.

La implementación utiliza una lista de Python como almacenamiento interno y las variables `frente`, `final` y `cantidad` para controlar el estado de la cola.

## 6. ¿Qué ocurriría al utilizar otra estructura?

Si se utilizara una estructura como una pila (Stack), el comportamiento sería diferente porque una pila utiliza el principio LIFO (Last In, First Out), es decir, el último estudiante en ingresar sería el primero en ser atendido.

Esto no sería adecuado para un sistema de turnos, porque podría provocar que los estudiantes que llegan primero tengan que esperar más tiempo mientras los nuevos estudiantes son atendidos antes.

Por esta razón, una cola resulta más apropiada para este problema.

## 7. Instrucciones para ejecutar el programa

### Requisitos

* Tener instalado Python 3.

El programa mostrará en la consola el registro de estudiantes, la consulta del siguiente turno, la atención de estudiantes y diferentes casos límite.

## 8. Casos de prueba utilizados

### Caso 1: Registrar estudiantes

Se registran:

* Andres Castor
* Angela Gómez
* Carlos Rodríguez

Se verifica que los estudiantes aparezcan en el orden correcto.

### Caso 2: Consultar el siguiente turno

Se utiliza `siguiente_turno()` para comprobar cuál es el primer estudiante de la cola.

Resultado esperado:

**Andres Castor**

### Caso 3: Atender estudiantes

Se atienden dos estudiantes consecutivamente.

Resultado esperado:

1. Andres Castor
2. Angela Gómez

Después queda:

**Carlos Rodríguez**

### Caso 4: Intentar atender una cola vacía

Después de atender a todos los estudiantes se intenta realizar otra atención.

Resultado esperado:


No hay estudiantes para atender. La cola está vacía.
```

### Caso 5: Llenar la cola

Se agregan cinco estudiantes, que corresponde a la capacidad máxima definida.

Resultado esperado:

La cola queda llena con cinco estudiantes.

### Caso 6: Intentar agregar cuando la cola está llena

Se intenta agregar un sexto estudiante.

Resultado esperado:

No se puede agregar el turno. La cola está llena.
```

## 9. Limitaciones y posibles mejoras

Una de las limitaciones de la aplicación es que la capacidad de la cola está definida previamente y no puede aumentar automáticamente.

Otra limitación es que los datos de los estudiantes solamente se manejan durante la ejecución del programa y no se almacenan permanentemente.

Como posibles mejoras se podrían implementar:

* Una interfaz gráfica.
* Almacenamiento de los estudiantes en una base de datos.
* Capacidad dinámica de la cola.
* Registro de información adicional de cada estudiante.
* Sistema de identificación de turnos.
* Menú interactivo para que el usuario pueda seleccionar las diferentes operaciones.

## 10. Video de demostración

En el enlace se encuentra el video donde se explica el funcionamiento del programa 

https://youtu.be/gwgiXlfNM0g
https://youtu.be/gwgiXlfNM0g

## Autor

**Duvan Felipe Ardila Losada**

**Ingeniería de Software**


