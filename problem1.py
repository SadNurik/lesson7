values = ("Razakov 32", 10, 1005, ["tables", "chairs"], 23.00)
slova = []

for i in values:
    try:
        set(i)
        slova.append(True)
    except TypeError:
        slova.append(False)
        print(slova)
print(all(slova))