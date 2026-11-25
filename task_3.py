h = int(input("Введіть висоту: "))
w = int(input("Введіть ширину: "))

print("--------------------")
for i in range(1, w + 1):
    print("*" * i)

print("--------------------")
for i in range(w):
    print("*" * (w - i))

print("--------------------")
for i in range(1, h + 1):
    print("*" * w)

print("--------------------")
for i in range(1, h + 1):
    if i == 1 or i == h:
        print("*" * w)
    else:
        print("*" + " " * (w - 2) + "*")
