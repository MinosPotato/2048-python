breite = 10

def verschiebe(bewegung):
	global feld
	werte = feld[:-1]  # ignore the -1 boundary
    
	if bewegung == "right":
		neue = [x for x in werte if x != 0]
		zeros = [0] * (len(werte) - len(neue))
		feld = zeros + neue + [-1]

	if bewegung == "left":
		neue = [x for x in werte if x != 0]
		zeros = [0] * (len(werte) - len(neue))
		feld = neue + zeros + [-1]

def fusioniere(bewegung):
    global feld
    fused = False

    if bewegung == "right":
        # go from right to left (ignore last element -1)
        for i in range(len(feld) - 2, 0, -1):
            if feld[i] == 0 or feld[i] == -1:
                continue
            if feld[i] == feld[i + 1]:
                feld[i + 1] *= 2
                feld[i] = 0
                fused = True

    if bewegung == "left":
        # go from left to right
        for i in range(1, len(feld) - 1):
            if feld[i] == 0 or feld[i] == -1:
                continue
            if feld[i] == feld[i - 1]:
                feld[i - 1] *= 2
                feld[i] = 0
                fused = True

    print(feld)


# Test 1:
print('\n Test 1\n')
feld = [2, 0, 2, 0, 2, 0, 2, 0, 2, 0, -1]

print(feld)

verschiebe('right')
assert feld == [0, 0, 0, 0, 0, 2, 2, 2, 2, 2, -1]
print(feld)
fusioniere('right')
print(feld)
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
print(feld)
assert feld == [8, 0, 16, 0, 16, 0, 0, 0, 0, 0, -1]
print(feld)
verschiebe('left')
assert feld == [8, 16, 16, 0, 0, 0, 0, 0, 0, 0, -1]
print(feld)
