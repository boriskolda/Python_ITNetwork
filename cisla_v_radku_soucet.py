cisla_retezec = "10,50,abcd,30,9"
cisla_pole = cisla_retezec.split(",")

soucet = 0

for cislo in cisla_pole:
    if not cislo.isdigit():
        continue

    else:
        cele_cislo = int(cislo)
        soucet += cele_cislo

print(f"Součet je: {soucet}")