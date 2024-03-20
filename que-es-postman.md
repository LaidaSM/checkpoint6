# ¿Qué es Postman?

Postman es una plataforma API para construir y utilizar APIs. Se trata de una aplicación que dispone de herramientas nativas para diversos sistemas operativos como Windows, Mac y Linux.

Cuenta con una versión libre de pago y con tres planes (básico, profesional y empresarial) que pueden consultarse en su web oficial https://www.postman.com/.

## ¿Para qué sirve Postman?

* Testear colecciones o catálogos de APIs tanto para Frontend como para Backend.
* Organizar en carpetas, funcionalidades y módulos los servicios web.
* Permite gestionar el ciclo de vida (conceptualización y definición, desarrollo, monitoreo y mantenimiento) de nuestra **API**.
* Generar documentación de nuestras APIs.
* Trabajar con entornos (calidad, desarrollo, producción) y de este modo es posible compartir a través de un entorno **cloud** la información con el resto del equipo involucrado en el desarrollo.

## Métodos más utilizados

Los métodos o verbos más utilizados para tomar acción ante nuestras peticiones son los que hemos visto en el apartado anterior:

* **GET**: Obtener información
* **POST**: Agregar información
* **PUT**: Reemplazar la información
* **PATCH**: Actualizar alguna información
* **DELETE**: Borrar información

### Posibles errores

Si la respuesta dada se encuentra en el rango de "200" significa que la petición ha salido sin problemas. El rango 400 hace referencia a errores con el cliente, y los 500 tienen que ver con fallos en el servidor.

* 200 - OK
* 201 - Created
* 204 - No Content
* 400 - Bad Request
* 401 - Unauthorized
* 403 - Forbidden
* 404 - Not Found
* 500 - Internal Server Error

En la siguiente tabla que he tomado prestada de https://blog.hubspot.es/website/que-es-api-rest se ofrecen ejemplos de errores y el porqué de los mismos:

| VERBO HTTP | URL DEL RECURSO    | ACCIÓN                                   | HTTP STATUS                                                                                                                                                                     |
| ---------- | ------------------ | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GET        | /libros            | Obtener una lista de libros              | <p>200 - OK</p><p>204 - Not Content: cuando no hay libros a listar</p>                                                                                                          |
| GET        | /libros/{id-libro} | Obtener detalle de un libro              | <p>200 - OK</p><p>404 - Not Found: cuando no existe el libro buscado</p>                                                                                                        |
| POST       | /libros            | Crear un recurso nuevo libro             | 201 - Created                                                                                                                                                                   |
| PUT        | /libros/{id-libro} | Modificar un recurso libro completamente | <p>200 - OK</p><p>400 - Bad request: cuando algún parámetro enviado no cumple con las reglas</p>                                                                                |
| PATCH      | /libros/{id-libro} | Modificar un recurso libro parcialmente  | <p>200 - OK</p><p>201 - Created: si el recurso a modificar no existe se crea en automático</p><p>400 - Bad request: cuando algún parámetro enviado no cumple con las reglas</p> |
| DELETE     | /libros/{id-libro} | Eliminar un recurso libro                | 201 - Not Content: es el status standard a regresar en un                                                                                                                       |

## Instalación

La descarga e instalación de la aplicación dependerá de tu sistema operativo, por lo que la mejor opción será que accedas al enlace https://www.postman.com/downloads/ y sigas las indicaciones que correspondan en tu caso.

## Primeros pasos

Una vez instalada la aplicación, podemos empezar creando una nueva colección. Dentro de ésta, podemos acceder a Add a request para empezar a utilizar el método.

<figure><img src=".gitbook/assets/image (26).png" alt=""><figcaption></figcaption></figure>

La lista de los verbos API a utilizar se encuentra en el siguiente apartado.

<figure><img src=".gitbook/assets/image (27).png" alt=""><figcaption></figcaption></figure>

Debemos seleccionar el método que queramos, copiar la URL correspondiente a la API, y  pinchar en Send si no tenemos más información que añadir. Los resultados nos aparecerán en el apartado body de la parte inferior:

<figure><img src=".gitbook/assets/image (28).png" alt=""><figcaption></figcaption></figure>

Si debemos introducir código, por ejemplo porque queremos añadir un nuevo recurso mediante el verbo POST, deberemos acceder al apartado Body de la parte superior, seleccionar raw y JSON.

A continuacion introduciremos la info correspondiente y entonces pulsaremos Send.

<figure><img src=".gitbook/assets/image (29).png" alt=""><figcaption></figcaption></figure>

## Ventajas de Postman

Una de las ventajas del uso de Postman es que cuenta con una comunidad grande de usuarios. Además, es posible colaborar con otros miembros de un equipo.

Su interfaz es sencilla e intuitiva, y cuenta con una extensión para el navegador Google Chrome.

Es posible integrarlo con otras herramientas, y es posible agregar scripts de JavaScript para añadir validaciones, automatizar o configurar pruebas.

## Alternativa: SoapUI

SoapUI es una herramienta que ha sido desarrollada en Java y es mayormente utilizada para llevar a cabo pruebas de sistemas cuya arquitectura sea REST o SOAP. Esta soporta múltiples protocolos como JMS, JDBC, HTTP, REST, SOAP.

Al igual que Postman, cuenta con una versión libre y otra de pago. Posee una gran comunidad de usuarios y su curva de aprendizaje es de nivel medio.

A diferencia de Postman, con SoapUI trabajamos en base a proyectos, los cuales pueden ser independientes o compuestos.

## Fuentes

Agradecimientos a:

* Guías Devcamp
* https://www.postman.com/product/what-is-postman
* https://openwebinars.net/blog/que-es-postman/&#x20;
* https://formadoresit.es/que-es-postman-cuales-son-sus-principales-ventajas/
