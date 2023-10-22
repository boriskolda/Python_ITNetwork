#!/usr/bin/env python3

leva_mez_1 = int(input("Zadejte levou mez 1. intervalu: "))

# Zde dokončete úlohu svým kódem...

prava_mez_1 = int(input("Zadejte pravou mez 1. intervalu: "))
leva_mez_2 =  int(input("Zadejte levou mez 2. intervalu: "))
prava_mez_2 = int(input("Zadejte pravou mez 2. intervalu: "))

print("Dvojice čísel, jejichž součet leží alespoň v jednom z intervalů:")

if leva_mez_1 < prava_mez_1 and leva_mez_2 < prava_mez_2 and leva_mez_1 <= leva_mez_2:
    
    for i in range(leva_mez_1, prava_mez_1):
        for j in range(leva_mez_2, prava_mez_2):
            soucet = i + j
            if soucet <= prava_mez_1 or soucet <= prava_mez_2:
                print(f"[{i};{j}]")
