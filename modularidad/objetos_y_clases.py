"""
La programación orientada a objetos (POO/OOP):

- ENCAPSULAMIENTO: Permite empaquetar el código dentro de una unidad (objeto) donde se puede determinar el ámbito de actuación.
- ABSTRACCIÓN: Permite generalizar los tipos de objetos a través de las clases y simplificar el programa.
- HERENCIA: Permite reutilzar código al poder heredar atributos y comportamientos de una clase a otra.
- POLIMORFISMO: Permite crear múltiples objetos a partir de una misma pieza clave.
"""

"""
OBJETO: Un objeto es una instancia única de una clase. (a tráves de los valores de sus atributos) e interactúa con otros objetos a través de métodos.

CLASE: Es el molde o plantilla con el que se crean los objetos. Define los atributos y métodos que tendrán los objetos de esa clase. Es una abstracción de un conjunto de objetos similares.
"""


# Definiendo una clase, palabra reservada 'class'
from time import time
class StarWarsDroid:
    pass


# Instanciando un objeto de la clase StarWarsDroid
c3po = StarWarsDroid()
r2d2 = StarWarsDroid()
bb8 = StarWarsDroid()

"""
Añadiendo métodos: 
Un método es una función que forma parte de una clase o de un objeto. Incorpora un primer argumento que hace referencia al objeto en sí mismo, por convención se llama 'self'.
"""


class Droid:
    # Métodos (Acciones/Comportamientos)
    # Definición de un método
    def switch_on(self):
        print("Droid encendido")

    def switch_off(self):
        print("Droid apagado")


droid1 = Droid()
droid1.switch_on()
droid1.switch_off()

"""
Añadiendo atributos:
Un atributo es una variable que pertenece a un objeto. Se define dentro de la clase y se accede a él a través del objeto.
"""


class Droid2:
    # Definición de atributos
    def switch_on(self):
        self.power_on = True
        print("Droid encendido, en que puedo ayudarle?")

    def switch_off(self):
        self.power_on = False
        print("Droid apagado, hasta luego!")


droid2 = Droid2()
droid2.switch_on()
droid2.switch_off()

"""
Inicialización: 
Existe un método especial llamado __init__ que se ejecuta automáticamente al crear un objeto de la clase. Se utiliza para inicializar los atributos del objeto. Es conocido como 'constructor'.
"""


class Droid3:
    def __init__(self, name: str) -> str:
        self.name = name


droid3 = Droid3("R2D2")

print(droid3.name)

"""
Atributos 
"""


class Droid4:
    def __init__(self, name: str) -> str:
        self.name = name


droid4 = Droid4("C-3PO")

droid4.name = "waka-waka"

print(droid4.name)

# Python permite añadir atributos dinámicamente a un objeto luego de su creación
droid4.manufacturer = "Cybot Galactica"
droid4.height = 1.77

print(droid4.manufacturer, droid4.height)

"""
Uso de las propiedades: Mediante el uso de decoradores

@property: Para leer el valor de un atributo (getter).
@name: Para escribir el valor de un atributo (setter).
"""


class Droid5:

    def __init__(self, name: str) -> str:
        self.hidden_name = name

    @property
    def name(self) -> str:
        print("Inside the getter")
        return self.hidden_name

    @name.setter
    def name(self, name: str) -> None:
        print("Inside the setter")
        self.hidden_name = name


droid5 = Droid5("CG1-23")

droid5.name

droid5.name = "Nigel"

print(droid5.name)

# Seguimos accediendo directamente al atributo oculto
print(droid5.hidden_name)

# Podemos cambiar su valor
droid5.hidden_name = "Wakka-Waka"
print(droid5.hidden_name)

"""
Ocultando atributos: 
Convertir atributos en privados, se le conoce como encapsulamiento. 
"""


class Droid6:
    def __init__(self, name: str) -> str:
        self.__name = name


droid6 = Droid6("RD")

# Indicar _ a la clase para que permita el acceso a los atributos mediante el nombre de la clase
print(droid6._Droid6__name)

"""
Atributos de clase:
Podemos asignar atributos a una clase y serán asumidos por todos los objetos instanciados de esa clase.
"""


class Androide:
    obeys_owner = True  # Obedece a su dueño


good_droid = Androide()
print(good_droid.obeys_owner)

t1 = Androide()
t1.obeys_owner = False
print(t1.obeys_owner)


"""
Si se modifica un atributo de clase, solo se modifica el valor en el objeto y no en la clase.

Si se modifica un atributo desde la clase, se modifica el valor en todos los objetos de la clase.
"""


class Androide2:
    obeys_owner = True


android1 = Androide2()
print(android1.obeys_owner)

android2 = Androide2()
print(android2.obeys_owner)

Androide2.obeys_owner = False  # Cambia pasado y futuro

print(android1.obeys_owner)
print(android2.obeys_owner)


# NO SE MODIFICAN LOS DROIDES PASADOS
class Androide3:
    obeys_owner = True

    def __init__(self):
        self.obeys_owner = Androide3.obeys_owner


android1 = Androide3()
print(android1.obeys_owner)

android2 = Androide3()
print(android2.obeys_owner)

Androide3.obeys_owner = False

print(android1.obeys_owner)
print(android2.obeys_owner)

android3 = Androide3()
print(android3.obeys_owner)


"""
Métodos: Un método de instancia es un método que modifica o accede al estado del objeto al que se hace referencia. Recibe 'self' como primer argumento.
"""


class Androide4:
    # Método de instancia constructor
    def __init__(self, name: str) -> str:
        self.name = name
        self.convered_distance = 0

    def move_up(self, step: int) -> None:
        self.convered_distance += step
        print(f"Moving {step} steps")


robot = Androide4("C1-1SF")

robot.move_up(10)

"""
Métodos de clase: Un método de clase es un método que modifica o accede al estado de la clase a la que hace referencia. La identificación de estos métodos se completa aplicando el decorador '@classmethod' a la función.
"""


class Android:
    count = 0

    def __init__(self):
        Android.count += 1

    @classmethod
    def total_droids(cls) -> None:
        print(f"{cls.count} droids built so far!")


droid_a = Android()
droid_b = Android()
droid_c = Android()

Android.total_droids()


"""
Métodos estáticos: Un método estático es un método que no debería modificar el estado del objeto ni de la clase. No recibe ningún parámetro especial. La identificación de estos métodos se completa aplicando el decorador '@staticmethod' a la función.
"""


class SecondAndroid:
    def __init__(self):
        pass

    @staticmethod
    def get_droids_categories() -> tuple[str]:
        return ("Unipedal", "Bipedal", "Quadrupedal", "Aquatic", "Volant")


print(SecondAndroid.get_droids_categories())


"""
Métodos decorados:
"""


class ThirdDroid:
    @staticmethod
    def audit(method):
        def wrapper(self, *args, **kwargs):
            print(f"Droid {self.name} running {method.__name__}")
            return method(self, *args, **kwargs)  # Llama al método original

        return wrapper

    def __init__(self, name: str) -> str:
        self.name = name
        self.pos = [0, 0]

    @audit
    def move(self, x: int, y: int) -> None:
        self.pos[0] += x
        self.pos[1] += y

    @audit
    def reset(self) -> None:
        self.pos = [0, 0]


android_a = ThirdDroid("B1")

android_a.move(1, 1)
android_a.reset()


"""
Métodos mágicos: 
Los métodos mágicos empiezan y terminan con doble guión (__) se les conoce como dunder methods.

MÉTODOS MÁGICOS PARA COMPARACIONES Y OPERACIONES MATEMÁTICAS:
== : __eq__
!= : __ne__
< : __lt__
> : __eq__
<= : __gt__
>= : __le__

+ : __add__
- __sub__
* __mul__
/ : __truediv__
// : __floordiv__
% : __mod__
** : __pow__
"""


class Droid:
    def __init__(self, name: str, power: int):
        self.name = name
        self.power = power

    def __add__(self, other: Droid) -> Droid:
        new_name = self.name + "-" + other.name
        new_power = self.power + other.power
        return Droid(new_name, new_power)  # Retorna un nuevo objeto


r1 = Droid("C3-PO", 45)
r2 = Droid("R2D2", 91)

r3 = r1 + r2

print(f"Fusión driod \n{r3.name} with power {r3.power}")

# __str__ : Permite establecer la forma en la que un objeto es presentado
# como una cadena de texto


class Machine:
    def __init__(self, name: str, serial_number: int):
        self.serial_number = serial_number
        self.name = name

    def __str__(self) -> str:
        return f"🤖 Droid: {self.name}, serial-number: {self.serial_number}"


droid = Machine("Hulk", 1234)

print(droid.__str__())  # Llama a Machine.__str__()

# str(droid)

print(f"Droid -> {droid}")

"""
__repr()__:
El método __repr()__ se invoca automáticamente en los dos siguientes escenarios:

1. Cuando no existe el método __str__() en el objeto y tratamos de encontrar su representación en cadena de texto con str() o print().

2. Cuando utilizamos el intérprete interactivo de Python y pedimos el «valor» del objeto.
"""


class Machine2:

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"🤖 Hi there! I'm: {self.name}"

    def __repr__(self):
        return f"🤖 [Droid] '{self.name}' @ {hex(id(self))}"


c14 = Machine2("C-14")

print(c14)

print(c14.__repr__())

"""
Gestores de contexto: Un gestor de contexto permite aplicar una serie de acciones a la entrada y a la salida del bloque de código que engloba.

1. __enter__(): Acciones que se llevan a cabo al entrar al contexto.
2. __exit__(): Acciones que se llevan a cabo al salir del contexto.
"""

# Mide el tiempo de ejecución de un bloque de código


class Timer:
    def __enter__(self):
        self.start = time()

    def __exit__(self, exc_type, exc_value, traceback):
        self.end = time()
        exc_time = self.end - self.start
        print(f"Execution time: {exc_time} seconds")


# Probar el gestor de contexto
with Timer():
    for _ in range(1_000_000):
        x = 2**20

with Timer():
    x = 0
    for _ in range(1_000_000):
        x += 2**20

# print(x)

"""
Herencia: La herencia consiste en construir una nueva clase partiendo de una clase existente. Pero que añade o modifica ciertos atributos y métodos.
"""


# Herencia desde una clase base
class Droid:
    # Clase base
    def switchOn(self):
        print("Droid encendido")

    def switchOff(self):
        print("Droid apagado")


class ProtocolDroid(Droid):
    # Clase derivada que hereda de la clase base
    pass


print(issubclass(ProtocolDroid, Droid))

robot1 = Droid()
robot2 = ProtocolDroid()

robot1.switchOn()

robot2.switchOn()

"""
Sobreescribir un método: Permite modificar el comportamiento de la herencia.
"""


class Droid2:
    def switchOn(self):
        print("Hola, soy un Droid! como puedo ayudarte?")

    def switchOff(self):
        print("Hola, ya no puedo ayudarte! lo siento mucho")


class ProtocolDroid2(Droid2):
    # Sobreescribe el método switchOn
    def switchOn(self):
        print("Hola, soy un Droid PROTOCOL! como puedo ayudarte?")


roboto1 = Droid2()
roboto2 = ProtocolDroid2()

roboto1.switchOn()
roboto2.switchOn()

"""
Añadir un método: Una clase derivada puede, como cualquier otra clase normal añadir métodos que no estaban presentes en su clase base.
"""


class Droid:
    def switch_on(self):
        print("Hi! I'm a droid. Can I help you?")

    def switch_off(self):
        print("Bye! I'm going to sleep")


class ProtocolDroid(Droid):
    def switch_on(self):
        print("Hi! I'm a PROTOCOL droid. Can I help you?")

    # Nuevo método
    def translate(self, msg: str, *, from_lang: str) -> str:
        """Translate from language to Human understanding"""
        return f'{msg} means "ZASCA" in {from_lang}'


r2d2 = Droid()
c3po = ProtocolDroid()

c3po.translate("kiitos", from_lang="Huttese")  # idioma de Watoo

"""
Accediendo a la clase base:
Cuando tenemos métodos (o atributos) definidos con el mismo nombre en la clase base y en la clase derivada (colisión), debe existir un mecanismo para diferenciarlos. Para estas ocasiones Python ofrece la función 'super()' para acceder a métodos (o atributos) de la clase base.
"""


class Droides:
    def __init__(self, name: str):
        self.name = name


class ProtocoloDroides(Droides):
    def __init__(self, name: str, languages: list[str]):
        super().__init__(name)
        self.languages = languages


droides1 = ProtocoloDroides("C-3PO", ["Español", "Inglés", "Watoo"])

print(droides1.name)  # Fijado en el constructor de la clase base
print(droides1.languages)  # Fijado en el constructor de la clase derivada

"""
Herencia múltiple: Python permite heredar de múltiples clases bases.
"""


class Droidess:
    def greet(self):
        return "Here a Droid!"


class ProtocolDroid1(Droidess):
    def greet(self):
        return "Hello, I'm a Protocol Droid!"


class AstromechDroid(Droidess):
    def greet(self):
        return "Hello, I'm an Astromech Droid!"


class SuperDroid(ProtocolDroid1, AstromechDroid):
    pass


class HyperDroid(AstromechDroid, ProtocolDroid1):
    pass


# Comprobando herencia múltiple
print(issubclass(SuperDroid, (ProtocolDroid1, AstromechDroid, Droidess)))
print(issubclass(HyperDroid, (AstromechDroid, ProtocolDroid1, Droidess)))

super_droid = SuperDroid()
hyper_droid = HyperDroid()

print(super_droid.greet())
print(hyper_droid.greet())

"""
Agregación y composición: 

1. Agregación: Implica que el objeto utilizado puede funcionar por sí mismo.
3. Composición: Implica a que el objeto utilzado no púede funcionar sin la presencia de su propietario.
"""


# Ejemplo de agregación
class Tool:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name.upper()


class SecondDroid:
    def __init__(self, name: str, serial_number: int, tool: Tool):
        self.name = name
        self.serial_number = serial_number
        self.tool = tool  # Agregación

    def __str__(self):
        return f"Droid {self.name} armed with a {self.tool}"


lighter = Tool("lighter")

bb8 = SecondDroid("BB-8", 12343453, lighter)
print(bb8)
