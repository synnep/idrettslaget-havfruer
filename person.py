# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 09:42:15 2022

@author: synneped
"""

class Person:
    """
    Klasse som lager en person
    
    Atributter:
    fornavn (str):
    etternavn (str):
    tlf (int):
    
    """
    
    def __init__(self, fornavn, etternavn, tlf):
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.tlf = tlf
        
    def visInfo(self):
        #Viser info om personen
        print(f"Fornavn:\t{self.fornavn}")
        print(f"Etternavn:\t {self.etternavn}")
        print(f"Tlf:\t {self.tlf}")
