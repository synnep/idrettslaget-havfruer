# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 09:11:59 2022

@author: synneped
"""

class Spiller(Person):
    """
    Klasse for representasjon av spillerobjekter
        Arver fra person-objekter
    
    parametere fra personobjekt:
        fornavn (str): personens fornavn
        etternavn (str): personens etternavn
        mobilnummer (int): personens mobilnummer
        
    lokale parametere:
        posisjon (str): spillerens posisjon på banen
    """
    
    def __init__(self, fornavn:str, etternavn:str, mobilnummer:str, posisjon:str):
        super().__init__(fornavn, etternavn, mobilnummer)
        self.posisjon = posisjon
    
    def endrePosisjon(self, nyP):
        """
        Parametere: 
            nyP: spillerens nye posisjon
        oppdatterer spillerens posisjon til den nye posisjonen
        """
        self.posisjon = nyP