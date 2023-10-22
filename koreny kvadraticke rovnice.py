#!/usr/bin/env python3

print("Program na výpočet kvadratické rovnice")
print("Tvar rovnice: ax^2+bx+c=0")

#Zde dokonči úlohu svým kódem...

a = int(input("Zadej koeficient a: \n"))
b = int(input("Zadej koeficient b: \n"))
c = int(input("Zadej koeficient c: \n"))

d = (b * b) - (4 * a * c)

if a > 0 or a < 0:
    if d == 0:
        x = -(b)/(2*a)
        print("Rovnice má jeden kořen: \n", x)
    elif d > 0:
        x1 = (-(b)+d**(1/2))/(2*a)
        x2 = (-(b)-d**(1/2))/(2*a)
        print("Rovnice má dva kořeny: \n", x1,"\n", x2)
    else:
        print("Rovnice nemá řešení v oboru reálných čísel")
else:
    print("Není kvadratická rovnice")
