# ¿Qué es una API?

API es el acrónimo de "application programming interface" o interfaz de programación de aplicaciones.

Una API es un servicio similar a un sitio web o un servidor con el que puedes comunicarte, pero en lugar de recibir una página web, recibes datos.

## ¿Cómo funcionan las API?

La arquitectura de las API suele explicarse en términos de cliente y servidor. La aplicación que envía la solicitud se llama cliente, y la que envía la respuesta se llama servidor. Las API pueden funcionar de cuatro maneras diferentes, según el momento y el motivo de su creación.&#x20;

* API de SOAP: utilizan el protocolo simple de acceso a objetos. El cliente y el servidor intercambian mensajes mediante XML. Se trata de una API menos flexible que era más popular en el pasado.&#x20;
* API de RPC: se denominan llamadas a procedimientos remotos. El cliente completa una función (o procedimiento) en el servidor, y el servidor devuelve el resultado al cliente.&#x20;
* API de WebSocket: otro desarrollo moderno de la API web que utiliza objetos JSON para transmitir datos&#x20;
* API de REST: las API más populares y flexibles que se encuentran en la web actualmente. El cliente envía las solicitudes al servidor como datos. El servidor utiliza esta entrada del cliente para iniciar funciones internas y devuelve los datos de salida al cliente.

## Clasificación según ámbito de uso

Hay cuatro tipos de API según el ámbito de uso:&#x20;

API privadas: son internas de una empresa y solo se utilizan para conectar sistemas y datos dentro de la empresa.&#x20;

API públicas: están abiertas al público y pueden cualquier persona puede utilizarlas. Puede haber o no alguna autorización y coste asociado a este tipo de API.&#x20;

API de socios: solo pueden acceder a ellas los desarrolladores externos autorizados para ayudar a las asociaciones entre empresas.&#x20;

API compuestas: combinan dos o más API diferentes para abordar requisitos o comportamientos complejos del sistema.#

## ¿Qué es un punto final de API?

Un punto final de API es la ubicación de la API en la que un sistema interactúa con una API web. También es el punto de comunicación entre dos sistemas.

Es la URL específica que se utiliza para acceder a un recurso proporcionado por una aplicación web desde una API. El punto final se refleja como un buscador uniforme de recursos (URL), similar a la URL de un sitio web, donde los datos se transmiten de un programa a otro.

La URL del punto final es la ubicación exacta del recurso solicitado en un servidor API, permitiendo así que dos programas interactúen. En el punto final, la API accederá a los recursos que necesite de un servidor para realizar una tarea específica, como la obtención de ciertos datos o información.

Las API envían solicitudes para acceder a los datos desde un servidor y reciben una respuesta. La ubicación de la respuesta es el punto final, y es una parte importante de cualquier documentación porque indica a los desarrolladores cómo realizar solicitudes de API.

## APIs públicas para practicar

Con el fin de practicar y familiarizarte con las API, desde https://ed.team/blog/las-mejores-apis-publicas-para-practicar nos proporcionan 6 APIs públicas y gratuitas:

* API de Marvel: http://developer.marvel.com/&#x20;
* PokéAPI: https://pokeapi.co/&#x20;
* COVID Tracking: https://covidtracking.com/data/&#x20;
* Nomics: https://nomics.com/&#x20;
* OpenWeather APIs: https://openweathermap.org/api&#x20;
* JSON placeholder: https://jsonplaceholder.typicode.com/

Vamos a ver un ejemplo de dos de ellas, para comprobar qué nos encontraremos al consultarlas

### PokéAPI

Si como yo eres una buena millenial y no puedes resistirte al universo Pokémon, puedes acceder a la API mediante el enlace anteriormente proporcionado.

En la documentación de la API ([https://pokeapi.co/docs/v2](https://pokeapi.co/docs/v2)) encontramos indicaciones sobre su uso. Se nos indica además que la API es solo para consumo, por lo que solo está disponible el método HTTP GET. Hablaremos de los verbos HTTP en la siguiente sección.

Si accedemos al recurso de prueba que nos indican ([**https://pokeapi.co/api/v2/pokemon/ditto**](https://pokeapi.co/api/v2/pokemon/ditto)**), encontraremos el siguiente código:**

<figure><img src=".gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

Esto es código JSON, y presentado de esta forma es muy dificil de leer.

Podemos usar Postman, que es una herramienta que explicaremos en una de las siguientes secciones, para obtener un resultado más legible:

<figure><img src=".gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

### JSON placeholder

JSON placeholder es **u**na API gratuita que te ofrece datos ficticios como fotos, publicaciones, comentarios, datos de usuarios falsos...

Podemos acceder a través del enlace https://jsonplaceholder.typicode.com/. Al contrario que la anterior API, esta soporta todos los métodos HTTP:

<figure><img src=".gitbook/assets/image (18).png" alt=""><figcaption></figcaption></figure>

Aunque en la propia guía se nos indica que los recursos no se actualizaran realmente en el servidor, sino que se fingirá como si así fuese.

A continuación tenemos el ejemplo de crear un  nuevo post mediante el verbo POST en Postman:

<figure><img src=".gitbook/assets/image (19).png" alt=""><figcaption></figcaption></figure>

## Fuentes

Agradecimientos a:

* Guías Devcamp
* https://aws.amazon.com/es/what-is/api/&#x20;
* https://www.xataka.com/basics/api-que-sirve&#x20;
* https://ed.team/blog/las-mejores-apis-publicas-para-practicar
* https://mailchimp.com/es/resources/what-is-an-api-endpoint/
