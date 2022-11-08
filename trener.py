from person import Person

class Trener(Person):
    """
    Klasse for å lage trener-objekter

    Klassen skal arve fra superklassen "Personer" 
    """

    def __init__(self, navn, etternavn, telefonnummer):
        super().__init__(navn, etternavn, telefonnummer)
        self.rolle = ""

        self.roller()

    def roller(self):
        valg1 = int(input(
            "Skriv inn '1' for å bli Hovedtrener, '2' for å bli assistent, eller '3' for å bli begge"))

        if valg1 == 1:
            if self.rolle == "Hovedtrener":
                print("Treneren er allerede skrevet opp som en hovedtrener")
                return
            self.rolle == "Hovedtrener"

        elif valg1 == 2:
            # Må sjekke om gruppen har en hovedtrener
            if self.rolle == "Assistent":
                print("Treneren er allerede skrevet opp som en assistent")
                return
            self.rolle == "Assistent"

        elif valg1 == 3:
            self.rolle == "Begge"
