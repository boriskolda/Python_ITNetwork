slovo = input("Zadej palindrom:")

if slovo == slovo[::-1]:
    print("Ano, je to palindrom")
else:
    print("Ne, není to palindrom")


