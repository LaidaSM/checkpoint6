# ¿Qué es el polimorfismo?

## Conocimiento previo: Herencia

Antes de ver en qué consiste el polimorfismo en Python, aclaremos primero el concepto de herencia.&#x20;

Como concepto general, la herencia es la capacidad de crear versiones especializadas de las clases. Es un proceso mediante el cual se puede crear una clase hija que hereda de una clase padre, compartiendo sus métodos y atributos. La clase hija puede sobreescribir los métodos o atributos, o definir unos nuevos.

Para implementar la herencia, la sintaxis consiste en añadir paréntesis después del nombre de la clase hija al definirla, y dentro se pasa el nombre de la clase padre.

En el siguiente ejemplo tenemos una clase padre que es el genérico Animal, con un atributo y una función. Hemos definido también la clase hija Horse, que heredará el artributo y el método de la clase Animal:

```
class Animal:
  def __init__(self, weight):
    self.weight = weight

  def feed(self):
    self.weight += 1
    print(f"That was delicious. New weight is {self.weight} kg")

class Horse(Animal):
  def speak(self):
    print('¡Hiiii!')
```

Vamos a instanciar un objeto y acceder a métodos y atributos de la clase hija y la clase padre:

```
bojack_horseman = Horse(400)

bojack_horseman.speak()
# Output: ¡Hiiii!
print(bojack_horseman.weight)
# Output: 400
bojack_horseman.feed()
# Output: That was delicious. New weight is 401 kg
```

Hemos visto que la instancia de la clase hija tiene acceso a la clase padre.

Pero, ¿ y al contrario? Creemos una instancia de la clase padre Animal e intentemos realizar las mismas operaciones:

```
anonymous_animal = Animal(5)

anonymous_animal.speak()
# Output: AttributeError: 'Animal' object has no attribute 'speak'
print(anonymous_animal.weight)
# Output: 5 
anonymous_animal.feed()
# Output: That was delicious. New weight is 6 kg
```

Como podréis ver, la instancia de la clase padre tiene acceso a métodos y atributos de la clase padre, pero obtenemos un error si intentamos acceder a la clase hija.

## Polimorfismo

El término polimorfismo tiene origen en las palabras poly (muchos) y morfo (formas), y aplicado a la programación hace referencia a que los objetos pueden tomar diferentes formas, lo cual significa que un objeto se puede comportar de manera diferente en distintos contextos.

Para implementar el polimorfismo, simplemente podemos definir diferentes métodos que compartan el mismo nombre pero que realicen operaciones distintas.

Veamoslo con nuestro anterior ejemplo. Hemos creado un método llamado speak en la clase padre Animal, y haremos que lance un error porque no queremos que nadie llame a la clase Animal, ya que es una clase abstracta. Tiene el único propósito de mantener y almacenar el comportamiento compartido. Sólo las clases hijas van a llamar a esta clase.

Hemos añadido la función speak() a cada una de nuestras clases hijas, por lo que sobrescribirán el comportamiento de la función en la clase padre.

```
class Animal:
  def __init__(self, weight):
    self.weight = weight

  def feed(self):
    self.weight += 1
    print(f"That was delicious. New weight is {self.weight} kg")

  def speak(self):
    raise NotImplementedError('Subclass must implement speak method')

class Horse(Animal):
  def speak(self):
    print('¡Hiiii!')

class Cat(Animal):
  def speak(self):
    print('Miau')

class Dog(Animal):
  def speak(self):
    print('Guau Guau')
```

Veamos como se comporta la función speak() para cada instancia, tomando una forma distinta, es decir,  en este caso imprimiendo un texto distinto, para cada clase hija.

```
bojack_horseman = Horse(400)
princess_carolyn = Cat(4)
mr_peanutbutter = Dog(10)

bojack_horseman.speak()
# Output: ¡Hiiii!  
princess_carolyn.speak()
# Output: Miau
mr_peanutbutter.speak()
# Output: Guau Guau

anon = Animal(5)
anon.speak()
# Output: NotImplementedError: Subclass must implement speak method
```

### Otra opción: construir funciones polimórficas

En lugar de crear una clase abstracta y tener varias clases que hereden de ella, tenemos la opción de crear clases independientes y crear además una función donde ocurra el polimorfismo.

Vamos a reorganizar el código de nuestro anterior ejemplo, de forma que tenemos 3 clases, cada una con su función dunder init y speak.

Además, creamos la función speaker, de forma que cuando la llamemos tomando como argumento cada una de nuestras instancias, llamará a su vez a la función speak:

```
class Horse():
  def __init__(self, weight):
    self.weight = weight
    
  def speak(self):
    print('¡Hiiii!')

class Cat():
  def __init__(self, weight):
    self.weight = weight
  
  def speak(self):
    print('Miau')

class Dog():
  def __init__(self, weight):
    self.weight = weight
  
  def speak(self):
    print('Guau Guau')

    
def speaker(animal_obj):
  return animal_obj.speak()

bojack_horseman = Horse(400)
princess_carolyn = Cat(4)
mr_peanutbutter = Dog(10)

speaker(bojack_horseman)
# Output: ¡Hiiii!
speaker(princess_carolyn)
# Output: Miau
speaker(mr_peanutbutter)
# Output: Guau Guau
```

Aunque creo que el ejemplo de los animales es útil para entender el concepto, tal vez no sea muy útil para aplicarlo a la vida real. Puede que el siguiente ejemplo os pueda dar una pista de cómo podrían usarse estas herramientas para dar solución a requerimientos más realistas:

```
class Sociedad():
  def __init__(self, ventas, costes):
    self.ventas = ventas
    self.costes = costes
    
  def beneficio_despues_impuestos(self):
    return (self.ventas - self.costes) * 0.7

class Cooperativa():
  def __init__(self, ventas, costes):
    self.ventas = ventas
    self.costes = costes
  
  def beneficio_despues_impuestos(self):
    return (self.ventas - self.costes) * 0.85

    
def calculador_beneficio(empresa):
  return empresa.beneficio_despues_impuestos()

floristeria = Sociedad(1000, 500)
academias = Cooperativa(1000, 500)

print(calculador_beneficio(floristeria))
# Output: 350.0
print(calculador_beneficio(academias))
# Output: 425.0
```

### ¿Cuando usar clases abstractas vs funciones polimórficas?

Cuando tenemos mucho comportamiento compartido, será una buena idea hacer uso de la herencia. Por ejemplo, si la clase padre tiene 5 funciones que las clases hijas también deberían compartir de otro modo.

Si no tenemos mucho comportamiento compartido, pero simplemente queremos ser capaces de llamar la misma función, utilizar el polimorfismo con un enfoque basado en funciones es una buena manera de hacerlo.

## Fuentes

Agradecimientos a:

* Guías Devcamp
* [https://desarrolloweb.com/articulos/polimorfismo-programacion-orientada-objetos-concepto.html  ](https://desarrolloweb.com/articulos/polimorfismo-programacion-orientada-objetos-concepto.html)
* [https://ellibrodepython.com/programacion-orientada-a-objetos-python  ](https://ellibrodepython.com/programacion-orientada-a-objetos-python)
* [https://www.w3schools.com/python/python\_polymorphism.asp  ](https://www.w3schools.com/python/python\_polymorphism.asp)
* [https://blog.hubspot.es/website/clases-python#:\~:text=Una%20clase%20en%20Python%20es,en%20un%20programa%20de%20computadora](https://blog.hubspot.es/website/clases-python)[  ](https://desarrolloweb.com/articulos/polimorfismo-programacion-orientada-objetos-concepto.html)
