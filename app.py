# -*- coding: utf-8 -*-

__author__ = 'Borja Gete'
__email__ = 'borjagete90@outlook.es'

import os

from pymongo import MongoClient

#---------------------------------
# Functions
#---------------------------------

def generate_league():
  """Generate Random League with 16 Teams and 12 Players for each Team"""

#********************************************************************
# Main

mongoClient_str = 'mongodb://localhost:27017/'
mongoClient = MongoClient(mongoClient_str)
db = mongoClient.clutch_time

#---------------------------------
# Menu
#---------------------------------
while True:
  os.system('cls')
  print("\n**Clutch Time Manager Simulator**")
  print("\n[1] Generate random league")
  option = input("Introduce una opción: > ")

  if option == "1":
    generate_league()
  elif option == "0":
    print("Cerrando programa!")
    os.system('cls')
    break
  else:
    print("Opción incorrecta")
  input("\nPulse para continuar...")