from hand import Hand
from math import sqrt

class Spillbrett:
  def __init__(self):
    self._steiner = []
    self._sakser = []
    self._papirer = []
  
  def make_hand(self, type, posisjon_venstre, posisjon_topp):
    if type == "stein":
      self._steiner.append(Hand(type, posisjon_venstre, posisjon_topp))
    elif type == "saks":
      self._sakser.append(Hand(type, posisjon_venstre, posisjon_topp))
    elif type == "papir":
      self._papirer.append(Hand(type, posisjon_venstre, posisjon_topp))


  def oppdater(self):
    for stein in self._steiner:
      stein.beveg()
      for saks in self._sakser:
        if touching(stein, saks):
          saks.transformer()
          self._sakser.remove(saks)
          self._steiner.append(saks)
    for saks in self._sakser:
      saks.beveg()
      for papir in self._papirer:
        if touching(saks, papir):
          papir.transformer()
          self._papirer.remove(papir)
          self._sakser.append(papir)
    for papir in self._papirer:
      papir.beveg()
      for stein in self._steiner:
        if touching(papir, stein):
          stein.transformer()
          self._steiner.remove(stein)
          self._papirer.append(stein)

      
  def tegn(self, skjerm):
    for stein in self._steiner:
      stein.tegn(skjerm)
    for saks in self._sakser:
        saks.tegn(skjerm)
    for papir in self._papirer:
        papir.tegn(skjerm)

def touching(objekt1, objekt2):
  deltaX = objekt2.hent_posisjon_venstre() - objekt1.hent_posisjon_venstre()
  deltaY = objekt2.hent_posisjon_topp() - objekt1.hent_posisjon_topp()
  touching = sqrt(deltaX**2 + deltaY**2)
  if touching < 15:
    return True
  return False

def har_kollidert(objekt1, objekt2):
  kollisjon = (objekt2.hent_posisjon_venstre() > objekt1.hent_posisjon_venstre() - 50
    and objekt2.hent_posisjon_venstre() < objekt1.hent_posisjon_venstre() + 50
    and objekt2.hent_posisjon_topp() > objekt1.hent_posisjon_topp() - 50
    and objekt2.hent_posisjon_topp() < objekt1.hent_posisjon_topp() + 50)
  if kollisjon:
    return True
  else:
    return False