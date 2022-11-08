# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 10:13:24 2022

@author: synneped
"""

class Lag:
    """
    Klasse som lager lag
    
    Atributter:
        kapasietet (int): hvor mange spillere kan det være på laget
        trener (object): treneren som laget dannes med
    """
    def __init__(self, kapasitet:int, trener:object):
        self.kapasitet = kapasitet
        self.trener = [trener]
        self.lagListe = []
    #legger til spiller
    def  leggTilSpiller(self, spiller:object):
        if (len(self.lagListe)<self.kapasitet):
            self.lagListe.append(spiller)
        else:
            print("Laget er fullt")
    #fjerner spillere
    def fjernSpiller(self, spiller:object):
        if spiller in self.lagListe:
            self.lagListe.remove(spiller)
        else:
            print("Spilleren er ikke på laget")
    #legger til trener
    def leggTilTrener(self, trener:object):
        if len(self.trener) < 2:
            self.trener.append(trener)
        else:
            print("Det er allerede 2 trenere på laget")
    #fjerner trener
    def fjernTrener(self, trener:object):
        if self.trener > 1:
            if trener in self.trener:
                self.trener.remove(trener)
            else:
                print("Treneren finnes ikke på laget")
        else:
            print("Laget må ha minst en trener")