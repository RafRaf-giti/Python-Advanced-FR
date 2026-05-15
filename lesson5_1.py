# Thema: Introspection
# In ein Programm "hineinschauen"

# Infos anzeigen - help(obj)
import random

from lesson2 import makarius
from lesson4_3 import hello_world

help(random)

# Namen eines Moduls mit __name__
print(__name__)

# Den Tüp eines Objekts mit type()
print(type(5)) # <class 'int'>
print(type(2.34)) # <class 'flaot'>
print(type("Hello World"))  # <class 'str'>
print(type(True)) # <class 'bool'y
print(type([1, 2, 3])) # <class 'list'>
print(type((1, 2, 3))) # <class 'tuple'>
print(type({"Bob": "+43 676 4893240"})) # <class 'dict'>
# Beispiel mit Klasse
class Student:
    pass

nick = Student()
print(type(nick)) # <class '__main__.Student'>

# Attribute und Methoden mit dir()
# Kann man sehen, was ein Objekt alles besitzt.
class Human:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("I eat")

david = Human("David")
print(dir(david))

# dir() ohne Argumente
print(dir())  # Liste vom aktuellen Namespace (Klassen, Funktionen, Variablen)

# Prüfen, ob ein Objekt ein bestimmtes Attribut oder Methode besitzt hasattr()
print(hasattr(david, "name")) # True
print(hasattr(david, "age")) # False
# hasattr() fragt "Gibt es das überhaupt?"

# Werte holen mit getattr()
# Wenn man ein Attribut lesen möchte, kann man das verwenden
# Schema: getattr(obj, "attributname", ersatzwert)
print(getattr(david, "name", "Nicht gefunden!")) # David
print(getattr(david, "age", "Nicht gefunden!"))

# Prüfen, ob etwas aufrufbar ist mit callable()
# Prüfen, ob etwas wie eine Funktion aufgerufen werden kann
def hello():
    print("Hello")

x = 10

print(callable(hello)) # True
print(callable(x)) # False

class Parent:
    pass

class Child(Parent):
    pass


print(issubclass(Child, Parent))
print(issubclass(Parent, Child))

makarius = Parent()
print(isinstance(makarius, Parent))
print(isinstance(makarius, Child))

makarius = Child()
print(isinstance(makarius, Parent))
print(isinstance(makarius, Child))
