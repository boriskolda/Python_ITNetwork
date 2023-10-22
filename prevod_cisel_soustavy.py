#!/usr/bin/env python3

def preved_cislo_na_znak(cislo):

# Zde úlohu dokonči svým kódem...

    if (cislo >= 0 and cislo <= 0):
        return chr(cislo + ord("0"))
    else:
        return chr(cislo - 10 + ord("A"))

def z_desitkove(vysledek, soustava, zadane_cislo):
    while zadane_cislo > 0:
        vysledek += preved_cislo_na_znak(zadane_cislo % soustava)
        zadane_cislo = int(zadane_cislo / soustava)
    
    vysledek = vysledek[::-1]
    
    return vysledek



    # cislo = int(input("Číslo v desítkové soustavě:"))
    # soustava = int(input("Číselná soustava (2-16):"))
    # zbytek = 0
    # delenec = 0
    # prevedene = ""
    # while True:
        
    #     delenec = cislo // soustava
    #     zbytek = cislo % soustava
    #     cislo = delenec
    #     prevedene += str(zbytek)
    #     if delenec == 0:
    #         break

    # print(f"Číslo ve zvolené soustavě: {prevedene}")

print(preved_cislo_na_znak(16))

print(z_desitkove("", 16, 15))