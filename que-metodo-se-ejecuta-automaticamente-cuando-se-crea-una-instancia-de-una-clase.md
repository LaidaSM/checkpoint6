# ¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?

## Método \_\_init\_\_ o constructor: qué es

El método \_\_**init\_\_** (dunder init) es el que es llamado automáticamente por el intérprete de Python y se utiliza para realizar cualquier inicialización que sea necesaria para la instancia.

El método \_\_**init\_\_** se usa para asignar valores iniciales a los atributos de una instancia de la clase.

Anteriormente hemos visto los atributos de clase, que son comunes a todas las instancias de una clase. Sin embargo, existen también los atributos de instancia, que pertenecen a cada instancia particular de la clase.

Al llamar al método \_\_**init\_\_**, podemos establecer los valores de estos atributos y configurar la instancia de la clase para su uso posterior.

Veamoslo en nuestro anterior ejemplo. Imaginemos que cada instancia de nuestra clase tiene también dos atributos que consisten en el nombre y la edad del personaje. Deberemos definir la función \_\_**init\_\_** dentro de nuestra clase, tomando primero el argumento self y después los mencionados atributos. La sintaxis para definir los atributos dentro de la función es la siguiente:

```
class SimpsonCharacters:

  def __init__(self, name, age):
    self.name = name
    self.age = age

  
  city = "Springfield"
  type = "Cartoon"

  def creator(self):
    print("Creator: Matt Groening")
```

Así, podemos ver una diferencia clara entre name y age, que serán variables según el objeto que instanciemos, y city y type, que siempre serán los mismos para todos los objetos.



## Crear un objeto cuando existen atributos de instancia

Imaginemos que intentamos crear una instancia con la definición de clase anterior:

```
barney = SimpsonCharacters()
```

```
Traceback (most recent call last):
  File "/home/runner/Just-playin/main.py", line 15, in <module>
    barney = SimpsonCharacters()
TypeError: SimpsonCharacters.__init__() missing 2 required positional arguments: 'name' and 'age'
```

¡Ups! Parece que tenemos un problema. Por suerte, Python nos está chivando que faltan los dos argumentos requeridos por la función \_\_init\_\_.&#x20;

Así, cuando hemos definido atributos de instancia, debemos proporcionarlos cada vez que queramos instanciar un objeto:

```
barney = SimpsonCharacters("Barney Gumble", 40)
lisa = SimpsonCharacters("Lisa Simpson", 8)
ralph = SimpsonCharacters("Ralph Wiggum", 8)
```

## Getters y setters

¿Qué son los métodos Getter y Setter?

* Getter: Método que permite acceder a un atributo de una clase determinada.
* Setter: Un método que te permite establecer o cambiar el valor de un atributo en una clase.

Más adelante veremos también como los getters y setters pueden ayudarnos a acceder a atributos privados. En esta sección veremos un proceso sencillo, pero tiene el inconveniente de ofrecer demasiado acceso. Por lo tanto, deberemos tener en cuenta que esto puede llevar a bugs.

### Getters

Para tener acceso a los valores de atributos que hemos definido, deberemos usar la siguiente sintaxis:

```
print(barney.age)
# Output: 40
print(lisa.name)
# Output: Lisa Simpson
```

También podemos acceder a los atributos de clase con la misma sintaxis:

```
print(ralph.type)
# Output: Cartoon
print(lisa.type)
# Output: Cartoon
```

#### Acceder a funciones

Para acceder a las funciones dentro de la clase, usamos la misma sintaxis pero con paréntesis () al final. Aunque no es el caso, debemos recordar pasar también los argumentos si la función los requiere:

```
barney.creator()
# Output: Creator: Matt Groening
```

Es raro que los lenguajes de programación permitan este nivel de acceso, normalmente habría que entrar dentro de la clase y crear una función que devolviese los datos.

### Setters

Podemos establecer los valores de los atributos después de haber creado el objeto instanciado.

En el ejemplo hemos instanciado el objeto con el valor para age 8, pero posteriormente lo hemos actualizado a 9.

```

  def __init__(self, name, age):
    self.name = name
    self.age = age

  
  city = "Springfield"
  type = "Cartoon"

  def creator(self):
    print("Creator: Matt Groening")


lisa = SimpsonCharacters("Lisa Simpson", 8)

lisa.age = 9
print(lisa.age)
# Output: 9

```

### Problemas derivados del uso de atributos públicos

Por defecto, los atributos son públicos en Python, lo que significa que puede accederse a ellos desde cualquier lugar del programa. Esto parece algo positivo, pero tiene también la contraparte de que cualquiera puede acceder a ellos y modificarlos, incluso en los casos en los que no debería hacerse.

Por ejemplo, alguien podría modificar el valor del atributo de clase city para una de las instancias, cuando debería ser igual para todos las instancias de la clase:

```
lisa.city = "New York"
print(lisa.city)
# Output: New York
```

O podríamos tener un problema peor. Alguien podría modificar el valor de un atributo cambiando el tipo de datos. Las funciones que fuésemos a ejecutar según el tipo de dato original nos darían un error.

Por ejemplo, imaginemos que alguien cambia el valor de la variable age a un string y no nos damos cuenta. Si en otro punto del programa quisiéramos hacer crecer un año a nuestro personaje, obtendríamos este error:

```
# Una parte del programa
lisa.age = "kid"

# Otra parte del programa
lisa.age += 1
```

```
TypeError: can only concatenate str (not "int") to str
```

Como veremos más adelante, también existen atributos privados, a los cuales solo se puede acceder desde dentro de la clase en la que se definen. En Python, los atributos privados se definen mediante el prefijo «\_\_» seguido del nombre del atributo.

## Fuentes

Agradecimientos a:

* Guías Devcamp
* [https://www.w3schools.com/python/python\_classes.asp](https://www.w3schools.com/python/python\_classes.asp)
* [https://ellibrodepython.com/crear-clase-python](https://ellibrodepython.com/crear-clase-python)
* [https://www.udacity.com/blog/2021/11/\_\_init\_\_-in-python-an-overview.html](https://www.udacity.com/blog/2021/11/\_\_init\_\_-in-python-an-overview.html)
* [https://realpython.com/python-getter-setter/](https://realpython.com/python-getter-setter/)
