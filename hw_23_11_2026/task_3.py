h = int(input("Введіть висоту: "))
w = int(input("Введіть ширину: "))

print("--------------------")
if w < 2:
    print("При ширині менше 2 трикутник не вийде.")
else:
    for i in range(1, w + 1):
        print("*" * i)

print("--------------------")
if w < 2:
    print("При ширині менше 2 трикутник не вийде.")
else:
    for i in range(w):
        print("*" * (w - i))

print("--------------------")
if w < 2 or h < 2:
    print("При ширині або висоті менше 2 фігура не вийде.")
else:
    for i in range(1, h + 1):
        print("*" * w)

print("--------------------")
if w < 3 or h < 3:
    print("При ширині або висоті менше 3 фігура з порожнечею всередині не вийде.")
else:
    for i in range(1, h + 1):
        if i == 1 or i == h:
            print("*" * w)
        else:
            print("*" + " " * (w - 2) + "*")
