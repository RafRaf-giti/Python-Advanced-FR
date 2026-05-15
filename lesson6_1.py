# Exceptions
# z.B.:
# - Falscher Variablenname
# - Division durch 0
# - Man greift auf etwas zu, dass es nicht gibt
# - Falscher Datentyp
# Sorgt dafür, dass das Programm angehalten wird / "abstürzt"
from zipfile import error

# Fehler abfangen mit try & except
try:
    pass

except:
    pass


try:
    print("Start code...")
    print(error)
    print("No errors!")
except:
    print("We have an error!")

print("Code after try/except")



try:
    number = int("Hallo")
except ValueError:
    print("Kann nicht String in Integer umwandeln!")


try:
    value = int("Hallo!")
    result = 10 / 0
except ValueError:
    print("Fehler beim Umwandeln!")
except ZeroDivisionError:
    print("Darf nicht durch 0 dividieren")




try:
    value = int(input("Gebe eine Zahl ein!"))
except (ValueError, TypeError):
    print("Es gab einen Eingabefehler!")













try:
    number = int(input("Gebe eine Zahl ein! "))
except ValueError:
    print("Fehler bei der Nutzereingabe!")
else:
    print(f"Das Zweifache von {number} ist {number * 2}")



try:
    print("Start")
    x = 1 / 0
except ZeroDivisionError:
    print("Fehler wurde abgefangen!")
finally:
    print("Dieser Block läuft immer!")


print("\n\n\nKomplettes Beispiel mit allen Blöcken")
try:
    text = input("Gebe eine Zahl ein: ")
    number = int(text)
except ValueError:
    print("Das war keine Zahl!")
else:
    print("Umwandlungen erfolgreich!")
finally:
    print("Einführung in Try/Except")

