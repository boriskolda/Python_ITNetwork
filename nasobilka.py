print("Tabulka malé násobilky:")
for j in range(1, 11):
    for i in range(1, 11):
        cislo = str(i*j).rjust(5)
        print(cislo, end = " ")
    print()
    


