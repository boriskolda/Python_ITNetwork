class Zdravic:
    def pozdrav(self, jmeno):
        print("Ahoj uživateli {0}".format(jmeno))

zdravic = Zdravic()
zdravic.pozdrav("Karel")
zdravic.pozdrav("Petr")