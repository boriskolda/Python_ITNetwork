#!/usr/bin/env python3

zelenina = ["zelí", "okurka", "rajče", "paprika", "ředkev",
            "mrkev", "brokolice"]

# Zde dokonči úlohu svým kódem...

ovoce = ["malina", "banán", "jablko", "hruška", "meloun", "kiwi", "pomeranč"]

pokracovat = "ano"
kolik_slov = 0

while pokracovat == "ano":
    zadani = input("Zadejte název libovolné zeleniny nebo ovoce: ")
    if zadani in zelenina:
        print("Zadali jste zeleninu.")
    elif zadani in ovoce:
        print("Zadali jste ovoce.")
    else:
        print("Zadanou zeleninu nebo ovoce nemám v seznamu.")
    kolik_slov += 1
    pokracovat = input("Přejete si zadat další slovo? (ano/ne) ")
print("Zadali jste", kolik_slov, "slov")
input()
    



#     """
# # seznamy ovoce a zeleniny
# zelenina = ["zelí", "okurka", "rajče", "paprika", "ředkev",
#             "mrkev", "brokolice"]
# ovoce = ["jablko", "hruška", "pomeranč", "jahoda", "banán", "kiwi", "malina"]


# pocet_slov = 0
# pokracovat = "ano"
# while pokracovat == "ano":
#     slovo = input("Zadej název libovolného ovoce nebo zeleniny: \n")
#     if slovo in ovoce:
#         print("Zadal jsi ovoce")
#     elif slovo in zelenina:
#         print("Zadal jsi zeleninu")
#     else:
#         print("Tvoje slovo nemám v seznamu")
#     pocet_slov += 1
#     pokracovat = input("Přeješ si zadat další slovo? (ano/ne) ")
# print("Zadal jsi", pocet_slov, "slov")
# input()

    
