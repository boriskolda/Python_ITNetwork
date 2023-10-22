
class Nakladni_Auto:
    """
    Nakladní auto - definice
    """
    hmotnost_nakladu = 0
    nosnost = 3000

    def naloz(self, hmotnost):
        if self.hmotnost_nakladu + hmotnost <= self.nosnost:
            self.hmotnost_nakladu += hmotnost

    def vyloz(self, hmotnost):
        if hmotnost < self.hmotnost_nakladu:
            self.hmotnost_nakladu -= hmotnost

    def vypis_nalozeni(self):
        print(f"V nakladnim autě je naloženo {self.hmotnost_nakladu} kg")
        
