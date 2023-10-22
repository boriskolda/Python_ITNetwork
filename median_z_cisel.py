
cisla = []
vstup = "vstup" 


print("Zadávej čísla a nakonec zadej pouze ENTER pro ukončení zadávání")
while vstup:
    vstup = input("Zadej číslo: ")
    if vstup != "":
        cisla.append(int(vstup))


cisla_serazene = sorted(cisla)

median = cisla_serazene[len(cisla_serazene)//2]
for cislo in cisla:
    print(cislo, "se od mediánu odlišuje o", cislo - median)
input()

