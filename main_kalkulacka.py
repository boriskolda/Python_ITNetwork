from kalkulacka_tridy import Kalkulacka

kalkulacka = Kalkulacka()
print("Zadej 1. číslo: ", end="")
cislo1 = float(input())
kalkulacka.cislo_1 = cislo1
print("Zadej 2. číslo: ", end="")
cislo2 = float(input())
kalkulacka.cislo_2 = cislo2

print(f"Součet: {kalkulacka.soucet()}")
print(f"Rozdíl: {kalkulacka.rozdil()}")
print(f"Součin: {kalkulacka.soucin()}")
print(f"Podíl: {kalkulacka.podil()}")