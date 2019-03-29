# -*- coding: utf-8 -*-

__author__ = 'Borja Gete'
__email__ = 'borjagete90@outlook.es'

import json
import random

from player.player import *

def generate_player():
  with open('exclude/names.json') as json_file:  
    data = json.load(json_file)
    "Seleccionamos un pais"
    country = random.choice(list(data['countries']))
    print(country)