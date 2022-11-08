# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 10:01:12 2022

@author: synneped
"""
# importerer bibliotek
from person import *
from spiller import *
from trener import *
from lag import *
import random as r

fornavnliste = ["Synne", "Are", "Trygve", "Johannes", "Oskar", "Margit", "Joel"]
etternavnliste = ["Pedersen", "Flo", "Karlsen", "Engseth", "Lyngstad", "Erlandsson"]

def genererPerson():
    fNavn = fornavnliste[r.randint(0,len(fornavnliste)-1)]
    eNavn = etternavnliste[r.randint(0, len(etternavnliste)-1)]
    mob = r.randint(10000000, 99999999)
    
    return Person(fNavn, eNavn, mob)

p1 = Spiller(genererPerson(), "angrep")
trener1 = Trener(genererPerson())
trener1.leggTilRolle()

print(trener1.fornavn)
print(trener1.roller[0])

print(p1.fornavn)
print(p1.etternavn)
print(p1.tlf)
print(p1.posisjon)

lag1 = Lag(10, trener1)
lag1.leggTilSpiller(p1)

