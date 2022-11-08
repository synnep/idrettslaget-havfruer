# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 10:14:27 2022

@author: synneped
"""
from person import *

class Trener(Person):
    """
    Klasse for å lage trener-objekter

    Klassen skal arve fra superklassen "Personer" 
    """

    def __init__(self, navn, etternavn, telefonnummer):
        super().__init__(navn, etternavn, telefonnummer)
        self.roller = []

    def leggTilRolle(self):
        valg1 = int(input(
            "Skriv inn '1' for å bli Hovedtrener, '2' for å bli assistent, eller '3' for å bli begge"))

        if valg1 == 1:
            for i in range(len(self.roller)):
                if self.roller[i] == "Hovedtrener":
                    print("Treneren er allerede skrevet opp som en hovedtrener")
                    return
            self.roller.append("Hovedtrener")

        elif valg1 == 2:
            # Må sjekke om gruppen har en hovedtrener
            for i in range(len(self.roller)):
                if self.roller[i] == "Assistent":
                    print("Treneren er allerede skrevet opp som en assistent")
                    return
            self.roller.append("Assistent")

        elif valg1 == 3:
            if len(self.roller) == 0:
                self.roller.append("Hovedtrener")
                self.roller.append("Hovedtrener")
            elif len(self.roller) > 0:
                while len(self.roller) > 0:
                    self.roller[i].pop()

                self.roller.append("Hovedtrener")
                self.roller.append("Hovedtrener")

    def endreRoller(self):
        print("hei")

        valg2 = int(input(
            "For å fjerne hovedtrener-rollen, tast '1', for å fjerne assistent-rollen, tast '2'"))

        if valg2 == 1:
            for i in range(len(self.roller)):
                if self.roller[i] == "Hovedtrener":
                    self.roller[i].pop()
                    return
            print("Treneren hadde aldri denne rollen")

        if valg2 == 2:
            for i in range(len(self.roller)):
                if self.roller[i] == "Assistent":
                    self.roller[i].pop()
                    return
            print("Treneren hadde aldri denne rollen")