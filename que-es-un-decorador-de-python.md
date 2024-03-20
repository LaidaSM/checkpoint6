# ¿Qué es un decorador de python?

## Decoradores - qué son

Los decoradores son funciones que modifican el comportamiento de otras funciones.

Al utilizar la palabra decorar estamos indicando que queremos modificar el comportamiento de una función ya existente, pero sin tener que modificar su código. Una analogía tomada prestada directamente de https://codigofacilito.com/articulos/decoradores-python indica que podemos ver el tema como un pastel, donde en ocasiones la base del pastel no es suficiente para una fiesta y debemos añadir elementos extras, quizás glaseado, velas, aderezos etc ... de esta forma el pastel tendrá mejor aspecto y sabrá mejor. En la analogía la base del pastel no será más que nuestra función a decorar y los elementos extras los decoradores.

Un decorador no es más que una función la cual toma como input una función y a su vez retorna otra función.

## Cómo crear un decorador

Veamos un ejemplo sencillo. Queremos decorar la función ventas\_totales usando ejemplo\_decorador().

La función ejemplo\_decorador() define una nueva función que envuelve la función que se pasa como entrada. Concretamente, imprime dos strings, antes y después de la llamada a la función.

Para decorar una función basta con colocar en la parte superior el decorador con el prefijo @.

```
def ejemplo_decorador(funcion):
  def nueva_funcion(a, b):
      print("Antes de llamar a la función")
      c = funcion(a, b)
      print("Después de llamar a la función")
      return c
  return nueva_funcion

@ejemplo_decorador
def ventas_totales(a, b):
  print("Se está ejecutando la función ventas_totales()")
  return a + b

print(ventas_totales(100, 200))
```

Y obtendremos como output:

```
Antes de llamar a la función
Se está ejecutando la función ventas_totales()
Después de llamar a la función
300
```

## Algunos decoradores integrados en Python

Hemos visto como podemos definir nuestros propios decoradores, pero hay algunos que ya están integrados en Python.

Algunos de los más comunes son:

@staticmethod: Se utiliza en una clase para indicarte que el método que está decorando es un método estático (pueden ejecutarse sin crear instancias de la clase)

```
class Magikarp:
  @staticmethod
  def salpicadura():
      print('No pasó nada...')

Magikarp.salpicadura()
# Output: No pasó nada...
```

@classmethod: Se usa para indicarte que el método que está decorando es un método de clase. Los métodos de clase tampoco requieren que la clase sea instanciada antes de que puedan ser llamados, pero al contrario que los métodos estáticos, sí tienen acceso a los atributos de clase.

@property: se utiliza para etiquetar un método como definidor de propiedades.

## Decorador @property

### Conocimiento previo: atributos privados y protegidos

Como hemos mencionado en el apartado de getters y setters de atributos, el hecho de tener acceso a todos los datos dentro de una clase se puede considerar una mala práctica, y puede dar lugar a errores.

Los atributos a los que solo se debe acceder dentro de la clase, ni siquiera las clases anidadas, se llaman atributos privados y la convención común es añadir dos guiones bajos antes de su nombre.

Los atributos protegidos, por otro lado, se establecen añadiendo un guion bajo delante del nombre del atributo. Son similares a los atributos privados, porque no deben ser accedidos directamente desde fuera de la clase. Sin embargo, se puede acceder a los atributos protegidos desde las subclases.

Es importante destacar que el uso de atributos privados o protegidos nos ayuda a que nuestros datos no sean accidentalmente sobrescritos, pero no protegen frente a las infracciones intencionadas.

Volvamos a nuestro ejemplo de clase Store y protejamos los atributos.

```
class Store:
  def __init__(self, product, sales):
    self._product = product
    self._sales = sales

  def __str__(self):
    return f'We have sold {self._sales} units of {self._product}.'

  def __repr__(self):
    return f"Store('{self._product}', {self._sales})"


chocolate = Store('chocolate', 100)
```

Si intentasemos acceder a alguno de los valores usando la sintaxis habitual, obtendríamos un error.

```
print(chocolate.sales)
# Output: AttributeError: 'Store' object has no attribute 'sales'. Did you mean: '_sales'?
```

Por supuesto, siempre podríamos intentar acceder al atributo añadiendo simplemente el guion bajo, pero esto sería una mala práctica, ya que el código nos está indicando que no lo hagamos:

```
# Bad practice
print(chocolate._sales)
# Output: 100
```

### Uso del decorador @property

El decorador de propiedad puede ser usado sobre un método, que hará que actúe como si fuera un atributo.

Así, podemos agragar getters y setters "behind the scenes" y poder utilizar la sintaxis utilizada para acceder a los atributos cuando eran públicos.

Para añadir una propiedad, deberemos añadir @property dentro de la clase. El código introducido en el ejemplo nos permite acceder a la variable sales directamente:

```
class Store:
  def __init__(self, product, sales):
    self._product = product
    self._sales = sales

  def __str__(self):
    return f'We have sold {self._sales} units of {self._product}.'

  def __repr__(self):
    return f"Store('{self._product}', {self._sales})"

  @property
  def sales(self):
    return self._sales
```

Así, si intentamos acceder a sales, podemos obtener su valor:

```
chocolate = Store('chocolate', 100)

print(chocolate.sales)
# Output: 100
```

Pero si intentamos cambiar el valor del atributo, seguiremos obteniendo un error:

```
chocolate.sales = 200
# Output: AttributeError: can't set attribute 'sales'
```

Imaginemos que queremos ofrecer la habilidad de acceder a los datos de product y sales, pero solo queremos dar la opción de sobreescribir el valor de sales y no de product.

Como véis, hemos añadido el decorador @property para ambos atributos, pero la función setter (el decorador @sales.setter) solo ha sido añadido para el atributo sales.

```
class Store:
  def __init__(self, product, sales):
    self._product = product
    self._sales = sales

  def __str__(self):
    return f'We have sold {self._sales} units of {self._product}.'

  def __repr__(self):
    return f"Store('{self._product}', {self._sales})"

  @property
  def sales(self):
    return self._sales

  @sales.setter
  def sales(self, sales):
    self._sales = sales

  @property
  def product(self):
    return self._product


chocolate = Store('chocolate', 100)
```

Por lo tanto, vamos a poder consultar ambos atributos, pero solo podremos cambiar el valor de sales.

```
print(chocolate.sales)
#Output: 100
chocolate.sales = 200
print(chocolate.sales)
#Output: 200
print(chocolate.product)
#Output: chocolate
chocolate.product = 'candy'
print(chocolate.product)
#Output: AttributeError: can't set attribute 'product'
```

Como conclusión, cuando vemos un decorador de propiedad, tenemos que pensar que vamos a querer acceder a esos datos en algún momento. Si sólo vemos atributos con \_ delante del nombre pero no decoradores de propiedad, esto significa que los datos son para el uso interno de la clase.

## Fuentes

Agradecimientos a:

* Guías Devcamp
* [https://geekflare.com/es/python-decorators/](https://geekflare.com/es/python-decorators/)
* [https://www.geeksforgeeks.org/decorators-in-python/](https://www.geeksforgeeks.org/decorators-in-python/)
* [https://codigofacilito.com/articulos/decoradores-python  ](https://codigofacilito.com/articulos/decoradores-python)
* [https://ellibrodepython.com/decoradores-python](https://ellibrodepython.com/decoradores-python)[  \
  ](https://www.geeksforgeeks.org/decorators-in-python/)
