print("Program zjistí, z čeho se skládá slovo.")
slovo = input("Zadejte slovo: ")
samohlasky = 0
souhlasky = 0
cisel = 0
for znak in slovo:
    if znak in "aáeéěiíoóuúů":
        samohlasky = samohlasky + 1
    elif znak in "bcčdďfghjklmnňpqrřsštťvwxzž":
        souhlasky = souhlasky + 1
    elif ord(znak) in range(48, 58):
        cisel = cisel + 1
    else:
        pass
print(slovo, "má: ")
print("samohlásek", samohlasky)
print("souhlásek", souhlasky)
print("čísel", cisel)
print("ostatních znaků...", len(slovo) - samohlasky - souhlasky - cisel)

input("\nAplikaci ukončíte stisknutím klávesy Enter...")