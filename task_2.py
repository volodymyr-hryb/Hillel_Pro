username = input("Введіть ім'я користувача: ")
email = input("Введіть електронну адресу: ")
age = input("Введіть вік: ")
password = input("Введіть пароль: ")

errors = []

if len(username) < 5 or username[0].isdigit() or " " in username:
    errors.append("Ім'я користувача повинно містити щонайменше 5 символів, "
                  "не може починатись з числа і не має пробілів.")

if email.count("@") != 1:
    errors.append("Електронна адреса обов'язково повинна містити 1 символ @.")

if not age.isdigit() or int(age) < 16:
    errors.append("Вік може бути тільки з цифр і не менший за 16.")

if len(password) < 8 or len(set(password)) == 1 or " " in password:
    errors.append("Пароль має щонайменше 8 символів, "
                  "не може містити пробіли і не може складатись з одного й того ж символа.")

if not errors:
    print("Дані валідні. Реєстрація успішна!")
else:
    print("Дані невалідні. Виявлені помилки:")
    for error in errors:
        print("-", error)
