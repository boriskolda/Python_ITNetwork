# Zde dokonči úlohu svým kódem...

vstup = input("Zadejte text k zašifrování: \n")
heslo = input("Zadejte heslo: \n")

vystup = ""

for i, znak in enumerate(vstup):
    x = ord(heslo[i % len(heslo)]) - (ord("a") - 1)
    if ord(znak) + x > ord("z"):
        x -= ord("z") - ord("a") + 1
    vysledek = chr(ord(znak) + x)
    vystup += vysledek
print("Výsledek:", vystup)
input()
    

    

    
