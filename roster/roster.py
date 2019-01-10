# -*- coding: utf-8 -*-

__author__ = 'Borja Gete'
__email__ = 'borjagete90@outlook.es'

import random

class Player:
  def __init__(self, id_player, fn, ln, nation, age, hgt, wgt, p1, p2):
    self.id_player = int(id_player)
    self.firstname = fn
    self.lastname = ln
    self.nation = nation
    self.age = int(age)
    self.height = float(hgt)
    self.weight = float(wgt)
    self.position = int(p1)
    self.position2 = int(p2)
    

  def generate(self):
    jump = random.randint(0,100)
    speed = random.randint(0,100)
    strn = random.randint(0,100)
    res = random.randint(0,100)
    ft = random.randint(0,100)
    lu = random.randint(0,100)
    fg = random.randint(0,100)
    s3p = random.randint(0,100)
    offr = random.randint(0,100)
    defr = random.randint(0,100)
    ste = random.randint(0,100)
    blk = random.randint(0,100)
    ltl = random.randint(0,100)
    drb = random.randint(0,100)
    self.train(jump, speed, strn, res, ft, lu, fg, s3p, offr, defr, ste, blk, ltl, drb)

  def train(self, jump, speed, strn, res, ft, lu, fg, s3p, offr, defr, ste, blk, ltl, drb):
    self.jump = int(jump)
    self.speed = int(speed)
    self.strength = int(strn)
    self.resistance = int(res)
    self.freethrow = int(ft)
    self.layup = int(lu)
    self.fieldgoal = int(fg)
    self.threepoint = int(s3p)
    self.offrebound = int(offr)
    self.defrebound = int(defr)
    self.steal = int(ste)
    self.block = int(blk)
    self.lateral = int(ltl)
    self.dribbling = int(drb)




class Roster:
  def __init__(self, team, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12):
    self.team = int(team)
