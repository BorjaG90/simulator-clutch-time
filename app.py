# -*- coding: utf-8 -*-

__author__ = 'Borja Gete'
__email__ = 'borjagete90@outlook.es'

import os
import player.player_generator
from pymongo import MongoClient



#---------------------------------
# Functions
#---------------------------------
def generate_league():
  """Generate Random League with 12 Players for each Team"""
  number_teams = input("Introduce el nº de equipos a generar")
  for team_n in range(0, number_teams):
    #Generamos un equipo
    for player_n in range(0, 12):
      #Generamos un jugador
      generate_player()


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