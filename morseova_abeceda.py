# řetězec, který chceme dekódovat
s = ".-.. . --- -. .- .-. -.. ---"
print(f"Původní zpráva: {s}")
# řetězec s dekódovanou zprávou
zprava = ""

# vzorové seznamy
abecedniZnaky = "abcdefghijklmnopqrstuvwxyz"
morseovyZnaky = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
"..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-",
"...-", ".--", "-..-", "-.--", "--.."]

znaky = s.split(" ")

for morseuvZnak in znaky:
    abecedniZnak = "?"
    index = morseovyZnaky.index(morseuvZnak)
    if (index >=0):
        abecedniZnak = abecedniZnaky[index]
    zprava += abecedniZnak
print(f"Dekodovaná zpráva je: {zprava}")

