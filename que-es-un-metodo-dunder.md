# ¿Qué es un método dunder?

## Métodos dunder o mágicos: qué son

En Python, los métodos dunder son métodos especiales que tienen un doble guión bajo al principio y al final de su nombre. Dunder es la abreviatura de double underscore.

Los métodos Dunder son métodos que permiten a las instancias de una clase interactuar con las funciones y operadores incorporados en el lenguaje. Típicamente, los métodos dunder no son invocados directamente por el programador, haciendo que parezca que son llamados por arte de magia. Por eso, a veces también se hace referencia a los métodos dunder como "métodos mágicos".

Sin embargo, los métodos dunder no se invocan por arte de magia. Simplemente son llamados implícitamente por el lenguaje, en momentos específicos que están bien definidos, y que dependen del método dunder en cuestión.

## Algunos de los métodos dunder más comunes

### \_\_init\_\_

Como hemos visto en el apartado correspondiente, es el método dunder que se utiliza para inicializar una instancia de una clase. Cuando se crea una instancia de una clase, el método **init** es llamado automáticamente por el intérprete de Python.

### **\_\_str\_\_**

Es un método dunder que se utiliza para devolver un string de una instancia de una clase. Este método se llama cuando se usa la función str() para imprimir strings de aspecto agradable para los usuarios finales, una representación legible de tu objeto.

En el siguiente ejemplo, tenemos una clase para una tienda, que tiene los atributos product y sales.

```
class Store:
  def __init__(self, product, sales):
    self.product = product
    self.sales = sales

  def __str__(self):
    return f'We have sold {self.sales} units of {self.product}.'
    

chocolate = Store('chocolate', 100)

print(str(chocolate))
# Output: We have sold 100 units of chocolate.
```

Hemos añadido el método **str** para que nos de un string de lectura agradable sobre los atributos de cada instancia.

Fijaos que no llamamos a la función mediante **str**, sino que usamos str() pasando como argumento nuestra instancia.

### \_\_repr\_\_

Así como _str_\_, el método **repr** st utiliza también para convertir una representación de un objeto a un string. La diferencia es que **repr** debe representar sin ambigüedades el objeto, preferiblemente proporcionando una expresión que pueda utilizarse para reconstruir el objeto.

Los desarrolladores pueden utilizar repr porque necesitan depurar código y tienen que asegurarse de que saben lo que están viendo.

Siguiendo con el ejemplo anterior, podemos incluir la función **repr** dentro de la clase, para que apreciemos la diferencia con **str**:

```
class Store:
  def __init__(self, product, sales):
    self.product = product
    self.sales = sales

  def __str__(self):
    return f'We have sold {self.sales} units of {self.product}.'

  def __repr__(self):
    return f"Store('{self.product}', {self.sales})"
    

chocolate = Store('chocolate', 100)

print(str(chocolate))
# Output: We have sold 100 units of chocolate.
print(repr(chocolate))
# Output: Store('chocolate', 100)
```

De forma similar al método str, la función \_\_repr\_\_ se llama mediante la sintaxis repr() tomando como argumento el objeto instanciado.

### &#x20;\_\_add\_\_

El método \_\_**add\_\_** permite la definición de un comportamiento personalizado para el operador + en nuestra clase. Suma los atributos correspondientes de los objetos que contiene el resultado.

Una vez definido, podemos sumar dos objetos de una clase entre sí.

Vamos a añadirlo a nuestro anterior ejemplo:

```
class Store:
  def __init__(self, product, sales):
    self.product = product
    self.sales = sales

  def __str__(self):
    return f'We have sold {self.sales} units of {self.product}.'

  def __repr__(self):
    return f"Store('{self.product}', {self.sales})"

  def __add__(self, other):
    return Store(self.product + other.product, self.sales + other.sales)
    

chocolate = Store('chocolate', 100)
cookies  = Store('cookies', 50)

object_sum = chocolate + cookies

print(object_sum.sales)
# Output: 150
print(object_sum.product)
# Output: chocolatecookies
```

El uso de la palabra other como segundo argumento de la función \_\_add\_\_ es solo una convención, el código funcionará si usamos también otra palabra.

También debemos tener en cuenta la utilidad que queramos darle a la función. Como podréis ver, sumar las ventas de los objetos puede tener sentido, pero sumar los nombres de los productos, no tanto.

## Listado métodos dunder

La siguiente tabla, tomada prestada directamente de [https://www.tutorialsteacher.com/python/magic-methods-in-python](https://www.tutorialsteacher.com/python/magic-methods-in-python), nos muestra un listado de métodos dunder importantes en Python 3.

| Initialization and Construction | Description                                 |
| ------------------------------- | ------------------------------------------- |
| \_\_new\_\_(cls, other)         | To get called in an object's instantiation. |
| \_\_init\_\_(self, other)       | To get called by the \_\_new\_\_ method.    |
| \_\_del\_\_(self)               | Destructor method.                          |

| Unary operators and functions | Description                                        |
| ----------------------------- | -------------------------------------------------- |
| \_\_pos\_\_(self)             | To get called for unary positive e.g. +someobject. |
| \_\_neg\_\_(self)             | To get called for unary negative e.g. -someobject. |
| \_\_abs\_\_(self)             | To get called by built-in abs() function.          |
| \_\_invert\_\_(self)          | To get called for inversion using the \~ operator. |
| \_\_round\_\_(self,n)         | To get called by built-in round() function.        |
| \_\_floor\_\_(self)           | To get called by built-in math.floor() function.   |
| \_\_ceil\_\_(self)            | To get called by built-in math.ceil() function.    |
| \_\_trunc\_\_(self)           | To get called by built-in math.trunc() function.   |

| Augmented Assignment           | Description                                                       |
| ------------------------------ | ----------------------------------------------------------------- |
| \_\_iadd\_\_(self, other)      | To get called on addition with assignment e.g. a +=b.             |
| \_\_isub\_\_(self, other)      | To get called on subtraction with assignment e.g. a -=b.          |
| \_\_imul\_\_(self, other)      | To get called on multiplication with assignment e.g. a \*=b.      |
| \_\_ifloordiv\_\_(self, other) | To get called on integer division with assignment e.g. a //=b.    |
| \_\_idiv\_\_(self, other)      | To get called on division with assignment e.g. a /=b.             |
| \_\_itruediv\_\_(self, other)  | To get called on true division with assignment                    |
| \_\_imod\_\_(self, other)      | To get called on modulo with assignment e.g. a%=b.                |
| \_\_ipow\_\_(self, other)      | To get called on exponentswith assignment e.g. a \*\*=b.          |
| \_\_ilshift\_\_(self, other)   | To get called on left bitwise shift with assignment e.g. a<<=b.   |
| \_\_irshift\_\_(self, other)   | To get called on right bitwise shift with assignment e.g. a >>=b. |
| \_\_iand\_\_(self, other)      | To get called on bitwise AND with assignment e.g. a&=b.           |
| \_\_ior\_\_(self, other)       | To get called on bitwise OR with assignment e.g. a\|=b.           |
| \_\_ixor\_\_(self, other)      | To get called on bitwise XOR with assignment e.g. a ^=b.          |

| Type Conversion Magic Methods | Description                                                                               |
| ----------------------------- | ----------------------------------------------------------------------------------------- |
| \_\_int\_\_(self)             | To get called by built-int int() method to convert a type to an int.                      |
| \_\_float\_\_(self)           | To get called by built-int float() method to convert a type to float.                     |
| \_\_complex\_\_(self)         | To get called by built-int complex() method to convert a type to complex.                 |
| \_\_oct\_\_(self)             | To get called by built-int oct() method to convert a type to octal.                       |
| \_\_hex\_\_(self)             | To get called by built-int hex() method to convert a type to hexadecimal.                 |
| \_\_index\_\_(self)           | To get called on type conversion to an int when the object is used in a slice expression. |
| \_\_trunc\_\_(self)           | To get called from math.trunc() method.                                                   |

| String Magic Methods            | Description                                                                                     |
| ------------------------------- | ----------------------------------------------------------------------------------------------- |
| \_\_str\_\_(self)               | To get called by built-int str() method to return a string representation of a type.            |
| \_\_repr\_\_(self)              | To get called by built-int repr() method to return a machine readable representation of a type. |
| \_\_unicode\_\_(self)           | To get called by built-int unicode() method to return an unicode string of a type.              |
| \_\_format\_\_(self, formatstr) | To get called by built-int string.format() method to return a new style of string.              |
| \_\_hash\_\_(self)              | To get called by built-int hash() method to return an integer.                                  |
| \_\_nonzero\_\_(self)           | To get called by built-int bool() method to return True or False.                               |
| \_\_dir\_\_(self)               | To get called by built-int dir() method to return a list of attributes of a class.              |
| \_\_sizeof\_\_(self)            | To get called by built-int sys.getsizeof() method to return the size of an object.              |

| Attribute Magic Methods            | Description                                                            |
| ---------------------------------- | ---------------------------------------------------------------------- |
| \_\_getattr\_\_(self, name)        | Is called when the accessing attribute of a class that does not exist. |
| \_\_setattr\_\_(self, name, value) | Is called when assigning a value to the attribute of a class.          |
| \_\_delattr\_\_(self, name)        | Is called when deleting an attribute of a class.                       |

| Operator Magic Methods              | Description                                                  |
| ----------------------------------- | ------------------------------------------------------------ |
| \_\_add\_\_(self, other)            | To get called on add operation using + operator              |
| \_\_sub\_\_(self, other)            | To get called on subtraction operation using - operator.     |
| \_\_mul\_\_(self, other)            | To get called on multiplication operation using \* operator. |
| \_\_floordiv\_\_(self, other)       | To get called on floor division operation using // operator. |
| \_\_truediv\_\_(self, other)        | To get called on division operation using / operator.        |
| \_\_mod\_\_(self, other)            | To get called on modulo operation using % operator.          |
| \_\_pow\_\_(self, other\[, modulo]) | To get called on calculating the power using \*\* operator.  |
| \_\_lt\_\_(self, other)             | To get called on comparison using < operator.                |
| \_\_le\_\_(self, other)             | To get called on comparison using <= operator.               |
| \_\_eq\_\_(self, other)             | To get called on comparison using == operator.               |
| \_\_ne\_\_(self, other)             | To get called on comparison using != operator.               |
| \_\_ge\_\_(self, other)             | To get called on comparison using >= operator.               |

## Fuentes

Agradecimientos a:

* Guías Devcamp
* [https://barcelonageeks.com/dunder-o-metodos-magicos-en-python](https://barcelonageeks.com/dunder-o-metodos-magicos-en-python)
* [https://mathspp.com/blog/pydonts/dunder-methods](https://mathspp.com/blog/pydonts/dunder-methods)
* [https://blog.hubspot.es/website/clases-python#:\~:text=Una%20clase%20en%20Python%20es,en%20un%20programa%20de%20computadora  ](https://blog.hubspot.es/website/clases-python)
* [https://pythondiario.com/2018/06/metodos-magicos-programacion-en-python.html  ](https://pythondiario.com/2018/06/metodos-magicos-programacion-en-python.html)
* [https://www.tutorialsteacher.com/python/magic-methods-in-python](https://www.tutorialsteacher.com/python/magic-methods-in-python)[  \
  ](https://mathspp.com/blog/pydonts/dunder-methods)
