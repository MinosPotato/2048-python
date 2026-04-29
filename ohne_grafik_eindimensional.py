# Anzahl Quadrate in x-Richtung
breite = 10

def verschiebe(bewegung):
	global feld
	for i in len(feld):
		if bewegung == "right":
			if feld[i] == 0:
				feld.pop[i]
				feld.insert(0, 0)
		if bewegung == "left":
			if feld[i] == 0:
				feld.pop[i]
				feld.insert(-2,0)


def fusioniere(bewegung):
	global feld
	# Fusioniert jeweils zwei direkt nebeneinanderliegende Steine derselben Beschriftung.
	# Die Fusion geschieht in der Bewegungsrichtung.

	# Code zu ergänzen.	

	# Beim späteren Verwenden dieser Funktion in der pygame-Version sollte der Rückgabewert 
	# True sein, wenn Fusionen stattgefunden haben, sonst False.

	# Code für Rückgabewert ergänzen.	


# Test 1:
print('\n Test 1\n')
feld = [2, 0, 2, 0, 2, 0, 2, 0, 2, 0, -1]
# Bemerkung: Diese Variable speichert eine Zeile aus 10 Feldern im Spiel 2028.
# Die eigentlichen Einträge stehen an den Positionen 0 bis 9.
# Die beiden "Dummy-Einträge" -1 an den Positionen -1 und 10 markieren den linken bzw. rechten Rand.
# Mit ihrer Hilfe lässt sich bisweilen der Zugriff auf nicht existente Positionen der Liste elegant vermeiden.

print(feld)

verschiebe('right')
assert feld == [0, 0, 0, 0, 0, 2, 2, 2, 2, 2, -1]
print(feld)
fusioniere('right')
assert feld == [0, 0, 0, 0, 0, 2, 0, 4, 0, 4, -1]
print(feld)
verschiebe('right')
assert feld == [0, 0, 0, 0, 0, 0, 0, 2, 4, 4, -1]
print(feld)

# Test 2:
print('\n Test 2\n')

feld = [2, 2, 0, 4, 4, 4, 2, 2, 2, 2, -1]
print(feld)

verschiebe('right')
assert feld == [0, 2, 2, 4, 4, 4, 2, 2, 2, 2, -1]
print(feld)
fusioniere('right')
assert feld == [0, 0, 4, 4, 0, 8, 0, 4, 0, 4, -1]
print(feld)
verschiebe('right')
assert feld == [0, 0, 0, 0, 0, 4, 4, 8, 4, 4, -1]
print(feld)

# Test 3:
print('\n Test 3\n')

feld = [4, 0, 0, 4, 8, 8, 0, 8, 0, 8, -1]
print(feld)

verschiebe('right')
assert feld == [0, 0, 0, 0, 4, 4, 8, 8, 8, 8, -1]
print(feld)
fusioniere('right')
assert feld == [0, 0, 0, 0, 0, 8, 0, 16, 0, 16, -1]
print(feld)
verschiebe('right')
assert feld == [0, 0, 0, 0, 0, 0, 0, 8, 16, 16, -1]
print(feld)

# Test 4: (nun mal nach links)
print('\n Test 4\n')

feld = [4, 0, 0, 4, 8, 8, 0, 8, 0, 8, -1]
print(feld)

verschiebe('left')
assert feld == [4, 4, 8, 8, 8, 8, 0, 0, 0, 0, -1]
print(feld)
fusioniere('left')
assert feld == [8, 0, 16, 0, 16, 0, 0, 0, 0, 0, -1]
print(feld)
verschiebe('left')
assert feld == [8, 16, 16, 0, 0, 0, 0, 0, 0, 0, -1]
print(feld)
