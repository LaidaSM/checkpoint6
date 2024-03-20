# ¿Para qué usamos Clases en Python?

## Clases en Python: qué son

Python es un lenguaje de programación orientado a objetos. Casi todo en Python es un objeto, con sus propiedades y métodos. Una clase es una especie de plantilla o molde para crear objetos, una estructura de progamación que define un conjunto de métodos y atributos.

### ¿Para qué sirven?

Como hemos mencionado anteriormente, una clase define una plantilla para crear objetos, los cuales serán instancias de esa clase. Los objetos creados tienen las mismas propiedades y comportamientos definidos por la clase, pero pueden tener valores diferentes para los atributos que se definen en la clase.

## Crear una clase

Para definir una clase debemos usar la palabra clave **class** seguida del nombre de la clase y dos puntos (:). En la siguiente línea, que debe estar indentada, deberemos introducir las definiciones de métodos y atributos.

En este ejemplo sencillo, hemos definido la clase y hemos añadido atributos generales que pertenecen a la clase y por lo tanto serán comunes a todos los objetos que creemos con ella:

```
class SimpsonCharacters:
  city = "Springfield"
  type = "Cartoon"
```

### Convención general para los nombres de las clases

Según la guía de estilo de Python ([link](https://peps.python.org/pep-0008/#function-and-variable-names)) los nombres de las clases se escriben con la letra inicial mayúscula y se usa Pascal Case.

```
class NombreClase():
```

## Añadir métodos o funciones a la clase

Además de atributos, las clases tienen un conjunto de funciones o métodos que realizan diferentes funcionalidades.

Los métodos se definen de la misma manera que fuera de las clases, pero tienen como primer parámetro o argumento el objeto al que se le aplicará el método, que suele llamarse **self** por convención.

### Error argumentos al definir métodos

Veamos el anterior ejemplo, en el que hemos introducido una función a nuestra clase pero no hemos añadido ningún argumento.

```
class SimpsonCharacters:
  city = "Springfield"
  type = "Cartoon"

  def creator():
    print("Creator: Matt Groening")


barney = SimpsonCharacters()

barney.creator()
```

Si ejecutamos el código, obtendremos el siguiente error:

```
Traceback (most recent call last):
  File "/home/runner/Just-playin/main.py", line 11, in <module>
    print(barney.creator())
TypeError: SimpsonCharacters.creator() takes 0 positional arguments but 1 was given
```

Como veis, Python nos está avisando de que hay un problema con el número de argumentos proporcionado. La forma correcta de definir la función dentro de la clase será la siguiente:

```
class SimpsonCharacters:
  city = "Springfield"
  type = "Cartoon"

  def creator(self):
    print("Creator: Matt Groening")


barney = SimpsonCharacters()

barney.creator()
# Output: Creator: Matt Groening
```

## Crear objeto

Un objeto define una versión particular de una clase, con unos atributos particulares para ese objeto. El proceso de creación de un objeto a partir de una clase se llama instanciación. Es decir, el objeto es la instancia de la clase. La sintáxis para la creación es similar a llamar a una función. Proporcionamos el nombre del objeto, y lo igualamos al nombre de la clase terminado en paréntesis ().

En nuestro ejemplo, habíamos creado anteriormente una instancia llamada barney, y podemos crear más a partir de la clase. En este caso, aún no tenemos atributos que sean específicos para cada instancia, por lo que no pasaremos ningún argumento al instanciar los objetos.

```
class SimpsonCharacters:
  city = "Springfield"
  type = "Cartoon"

  def creator(self):
    print("Creator: Matt Groening")


barney = SimpsonCharacters()
lisa = SimpsonCharacters()
ralph = SimpsonCharacters()
```

### Imprimir los objetos instanciados

Partiendo del ejemplo anterior, hemos creado tres instancias para nuestra clase: barney, lisa y ralph.

Si intentamos imprimir una de estas instancias, obtendremos el siguiente output:

```
print(lisa)
# Output: <__main__.SimpsonCharacters object at 0x728e0e40faf0>
```

Como veis, Python nos está indicando que lisa es un objeto de SimpsonCharacters (el nombre de nuestra clase).

## Ventajas y desventajas del uso de clases

Una de las ventajas del uso de clases en python es que podemos reutilizar nuestro código en distintas partes del programa, reduciendo duplicidad y ahorrando tiempo.

Además, permiten descomponer un programa en componentes más pequeños, facilitando la solución de problemas.

En cuanto a las desventajas, hemos de mencionar que las clases pueden añadir complejidad adicional a un programa, haciendo que sea más dificil de entender. Esto es más notorio cuando su uso es innecesario y una función simple podría haber hecho el mismo trabajo.

## Fuentes

Agradecimientos a:

* Guías Devcamp
* [https://docs.python.org/es/3/tutorial/classes.html](https://docs.python.org/es/3/tutorial/classes.htmlhttps://www.w3schools.com/python/python\_classes.asphttps://ellibrodepython.com/crear-clase-pythonhttps://blog.hubspot.es/website/clases-python)
* [https://www.w3schools.com/python/python\_classes.asp  ](https://docs.python.org/es/3/tutorial/classes.htmlhttps://www.w3schools.com/python/python\_classes.asphttps://ellibrodepython.com/crear-clase-pythonhttps://blog.hubspot.es/website/clases-python)
* [https://ellibrodepython.com/crear-clase-python  ](https://docs.python.org/es/3/tutorial/classes.htmlhttps://www.w3schools.com/python/python\_classes.asphttps://ellibrodepython.com/crear-clase-pythonhttps://blog.hubspot.es/website/clases-python)
* [https://blog.hubspot.es/website/clases-python#:\~:text=Una%20clase%20en%20Python%20es,en%20un%20programa%20de%20computadora](https://docs.python.org/es/3/tutorial/classes.htmlhttps://www.w3schools.com/python/python\_classes.asphttps://ellibrodepython.com/crear-clase-pythonhttps://blog.hubspot.es/website/clases-python)[  \
  \
  ](https://docs.python.org/es/3/tutorial/classes.htmlhttps://www.w3schools.com/python/python\_classes.asphttps://ellibrodepython.com/crear-clase-pythonhttps://blog.hubspot.es/website/clases-python)
