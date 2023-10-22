print("Mocninátor")
print("==========")
a = int(input("Zadejte základ mocniny: "))
n = int(input("Zadejte exponent: "))
result = a
for i in range(n - 1):
    result = result * a

print("Výsledek: %d" % (result))
print("Děkuji za použití mocninátoru")