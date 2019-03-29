# -*- coding: utf-8 -*-

__author__ = 'Borja Gete'
__email__ = 'borjagete90@outlook.es'

class Player:
  """ Representa los datos de un jugador """
  def __init__(self, firstName, lastName, position, secondary, age, weight, height, country):
    self.firstName = firstName
    self.lastName = lastName
    self.position = position
    self.secondary = secondary
    self.age = age
    self.weight = weight
    self.height = height
    self.country = country

  def __str__(self):
    return "{} {} de {}, {}-{} de {} años, {} cms y {} kgs".format(
      self.firstName,
      self.lastName,
      self.country,
      self.position,
      self.secondary,
      self.age,
      self.height,
      self.weight
    )

  def to_db_collection(self):
    """ Devuelve los datos de un jugador en un formato legible para MongoDB """
    return {
      "first_name": self.firstName,
      "last_name": self.lastName,
      "position": self.position,
      "secondary": self.secondary,
      "age": self.age,
      "weight": self.weight,
      "heigth": self.height,
      "country": self.country
    }

class Attributes:
  """ Representa los atributos de un jugador """
  def __init__(self, playerId, atRim, layup, dunk, freeThrow, lowPost, halfDistance, three, defReb, offReb, assist, block, steal, speed, jump, endurance, strength):
    self.playerId = playerId
    self.atRim =  atRim
    self.layup =  layup
    self.dunk =  dunk
    self.freeThrow =  freeThrow
    self.lowPost =  lowPost
    self.halfDistance =  halfDistance
    self.three =  three
    self.defReb =  defReb
    self.offReb =  offReb
    self.assist =  assist
    self.block =  block
    self.steal =  steal
    self.speed =  speed
    self.jump =  jump
    self.endurance =  endurance
    self.strength =  strengt
  def __str__(self):
    return "Atributos de {}".format(self.playerId)

  def to_db_collection(self):
    """ Devuelve los datos de un jugador en un formato legible para MongoDB """
    return {
      "player_id": self.playerId,
      "at_rim": self.atRim,
      "layup": self.layup,
      "dunk": self.dunk,
      "free_throw": self.freeThrow,
      "low_post": self.lowPost,
      "half_distance": self.halfDistance,
      "three": self.three,
      "def_reb": self.defReb,
      "off_reb": self.offReb,
      "assist": self.assist,
      "block": self.block,
      "steal": self.steal,
      "speed": self.speed,
      "jump": self.jump,
      "endurance": self.endurance,
      "strengt": self.strength
    }