height = float(input("Podaj wzrtost: "))
weight = float(input("Podaj wagę: "))

BMI = weight / (height ** 2)

print("Twoje BMI to {:.2f}".format(BMI))

if BMI < 18.5:
    print("Masz niedowagę.")
elif BMI < 25:
    print("Twoja waga jest optymalna.")
elif BMI < 30:
    print("Masz nadwagę.")
else:
    print("Masz otyłość.")
