# ¿Cuáles son los tres verbos de API?

### ¿Qué es una API REST?

Como hemos mencionado previamente, una API REST es una interfaz de comunicación entre sistemas de información que usa el protocolo de transferencia de hipertexto (hypertext transfer protocol o HTTP, por su siglas en inglés) para obtener datos o ejecutar operaciones sobre dichos datos en diversos formatos, como pueden ser XML o JSON.

## ¿Qué son los verbos HTTP?

Son aquellos verbos propios del protocolo HTTP que fueron tomados para definir operaciones muy puntuales y específicas sobre los recursos de la API.

Los verbos Http involucrados en un sistema REST son GET, POST, PUT, PATCH y DELETE.

### GET

GET es el que usamos para consultar un recurso. Una de las principales características de una petición GET es que no debe causar efectos secundarios en el servidor, no deben producir nuevos registros, ni modificar los ya existentes. A esta cualidad la llamamos idempotencia, cuando una acción ejecutada un número indefinido de veces, produce siempre el mismo resultado.

Ejemplo de uso de GET con https://jsonplaceholder.typicode.com/ y Postman:

<figure><img src=".gitbook/assets/image (20).png" alt=""><figcaption></figcaption></figure>

### POST

Las peticiones con POST son sólo para crear recursos nuevos. Cada llamada con POST debería producir un nuevo recurso.

Normalmente, la acción POST se dirige a una recurso que representa una colección, para indicar que el nuevo recurso debe agregarse a dicha colección, por ejemplo POST /cursos para agregar un nuevo recurso a la colección cursos.

Si queremos crear un nuevo post, pudiéramos tener una URI /posts. Lo que es importante en estos casos, es recordar que la URI no debe decir qué acción estamos ejecutando,no debe indicar de /posts/create etc. El verbo PUT dice qué haremos, y la URI, sobre qué recurso se harán las modificaciones.

Ejemplo de uso de POST:

<figure><img src=".gitbook/assets/image (21).png" alt=""><figcaption></figcaption></figure>

### PUT y PATCH

Los verbos PUT/PATCH son muy similares ya que ambos se usan para modificar un recurso existente. PUT se diferencía de PATCH, en que el primero indica que vamos a sustituir por completo un recurso, mientras que PATCH habla de actualizar algunos elementos del recurso mismo, sin sustituirlo por completo.

En la práctica, ambos verbos se usan para actualizar un recurso, sin importar si lo sustituimos parcial o totalmente.

Ejemplo de uso de PUT, sustituyendo un recurso:

<figure><img src=".gitbook/assets/image (22).png" alt=""><figcaption></figcaption></figure>

Ejemplo de uso de PATCH, actualizando un recurso de forma parcial:

<figure><img src=".gitbook/assets/image (23).png" alt=""><figcaption></figcaption></figure>

### DELETE

DELETE es el verbo que usamos para eliminar registros, puede usarse para eliminar un recurso individual o para eliminar una colección completa.

Ejemplo de eliminación de un recurso:

<figure><img src=".gitbook/assets/image (24).png" alt=""><figcaption></figcaption></figure>

## Fuentes

Agradecimientos a:

* Guías Devcamp
* https://codigofacilito.com/articulos/rails-verbos-http&#x20;
* https://blog.hubspot.es/website/que-es-api-rest
