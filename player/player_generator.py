# -*- coding: utf-8 -*-

__author__ = 'Borja Gete'
__email__ = 'borjagete90@outlook.es'

import json
import random

from player.player import *

def generatePlayer(pos):
  with open('exclude/names.json') as json_file:  
    data = json.load(json_file)
    "Seleccionamos un pais"
    country = random.choice(list(data['countries']))
    firstname = random.choice(list(data['names'][country]['firstname']))
    lastname = random.choice(list(data['names'][country]['lastname']))
    age = int(random.randrange(17, 42, 1))
    secondary = generateSecondPosition(pos)
    height = generateHeight(pos)
    weight = generateWeight(height)
    print("{} {} de {}, {} años, {}-{} , {} cms y {} kgs".format(
      firstname,
      lastname, 
      country, 
      age, 
      pos,
      secondary,
      height,
      weight
      )
    )
    
def generateSecondPosition(pos):
  up = int(random.randrange(0, 3, 1))
  if(pos == 1 and up < 1):
    secondary = 1
  elif(pos == 5 and up > 1):
    secondary = 5
  else:
    secondary = pos + (up-1)
  return secondary
  
def generateHeight(pos):
  height = 160 + int(random.randrange(7, 14, 1))*pos
  return height
    
def generateWeight(height):
  h = float(height/100)
  weight = int((h*h) * float(random.randrange(18, 30, 1)))
  return weight
  
  
