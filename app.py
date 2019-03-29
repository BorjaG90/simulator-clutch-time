# -*- coding: utf-8 -*-

__author__ = 'Borja Gete'
__email__ = 'borjagete90@outlook.es'

import os, random
from player.player_generator import *
from pymongo import MongoClient



#---------------------------------
# Functions
#---------------------------------
def generate_league():
  """Generate Random League with 12 Players for each Team"""
  db.players.delete_many({})
  number_teams = input("Introduce el nº de equipos a generar: ")
  for team_n in range(0, int(number_teams)):
    #Generamos un equipo
    #for player_n in range(0, 12):
    print("Generamos equipo")
      #Generamos un jugador
    player = generatePlayer(1)
    pid = db.players.insert_one(player.to_db_collection())
    print(pid.inserted_id)
    player = generatePlayer(1)
    pid = db.players.insert_one(player.to_db_collection())
    print(pid.inserted_id)
    player = generatePlayer(2)
    pid = db.players.insert_one(player.to_db_collection())
    print(pid.inserted_id)
    player = generatePlayer(2)
    pid = db.players.insert_one(player.to_db_collection())
    print(pid.inserted_id)
    player = generatePlayer(3)
    pid = db.players.insert_one(player.to_db_collection())
    print(pid.inserted_id)
    player = generatePlayer(3)
    pid = db.players.insert_one(player.to_db_collection())
    print(pid.inserted_id)
    player = generatePlayer(4)
    pid = db.players.insert_one(player.to_db_collection())
    print(pid.inserted_id)
    player = generatePlayer(4)
    pid = db.players.insert_one(player.to_db_collection())
    print(pid.inserted_id)
    player = generatePlayer(5)
    pid = db.players.insert_one(player.to_db_collection())
    print(pid.inserted_id)
    player = generatePlayer(5)
    pid = db.players.insert_one(player.to_db_collection())
    print(pid.inserted_id)
    player = generatePlayer(int(random.randrange(1, 3, 1)))
    pid = db.players.insert_one(player.to_db_collection())
    print(pid.inserted_id)
    player = generatePlayer(int(random.randrange(3, 5, 1)))
    pid = db.players.insert_one(player.to_db_collection())
    print(pid.inserted_id)
    print()

#********************************************************************
# Main

mongoClient_str = 'mongodb://admin:admin1234@ds127376.mlab.com:27376/clutch-time'
mongoClient = MongoClient(mongoClient_str)
db = mongoClient['clutch-time']

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