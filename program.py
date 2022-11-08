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

p1 = genererPerson()

