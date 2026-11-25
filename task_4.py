summa = float(input("Введіть суму у євро: ").replace(",", "."))
summa_in_cent = round(summa * 100)

count_banknotes = 0
count_coins = 0
list_strings = []

nominals = [50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

for nominal in nominals:
    count = summa_in_cent // nominal
    if count > 0:
        display_nominal = nominal // 100 if nominal >= 100 else nominal / 100
        list_strings.append(f"{count} x {display_nominal}")
        summa_in_cent %= nominal
        if nominal < 500:
            count_coins += count
        else:
            count_banknotes += count

print(f"Кількість банкнот: {count_banknotes}")
print(f"Кількість монет: {count_coins}")
print("Склад суми:")

for item in list_strings:
    print(item)
