#!/usr/bin/env python3

smajlik = input("Zadej smajlíka: \n")

# Zde dokonči úlohu svým kódem...

if smajlik == (":-)") or smajlik == (":)"): 
    print("Tvůj smajlík je veselý")
elif smajlik == (":-(") or smajlik == (":("):
    print("Tvůj smajlík je smutný")
elif smajlik == (":-*") or smajlik == (":*"): 
    print("Tvůj smajlík je zamilovaný")
elif smajlik == (":-P") or smajlik == (":P"): 
    print("Tvůj smajlík je s vyplazeným jazykem")
else: 
    print("Tvůj smajlík je neznámý")