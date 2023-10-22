class Zdravic:
    """
    Třída reprezentuje zdravič, který slouží ke zdravení uživatelů
    """
    def pozdrav(self, jmeno):
        """
        Vrátí pozdrav uživatele s nastaveným textem a jeho jménem
        """
        return "{0} {1}!".format(self.text, jmeno)

zdravic = Zdravic()
zdravic.text = "Ahoj uživateli"
print(zdravic.pozdrav("Karel"))
print(zdravic.pozdrav("Petr"))
zdravic.text = "Vítám tě tu programátore"
print(zdravic.pozdrav("Richard"))