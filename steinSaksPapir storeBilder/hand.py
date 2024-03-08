from random import randint

class Hand():
  def __init__(self, type, posisjon_venstre, posisjon_topp):
    self._type = type
    self._posisjon_venstre = posisjon_venstre
    self._posisjon_topp = posisjon_topp
    self._speed_X = 2
    self._speed_Y = 2

  def beveg(self):
    if randint(0,40) == 1:
      self.sett_fart(randint(-2,2), randint(-2,2))
    self._posisjon_venstre += self._speed_X
    self._posisjon_topp += self._speed_Y
    if self.hent_posisjon_venstre() > 1100-50 or self.hent_posisjon_venstre() < 0:
      self.snu_venstre()
    if self.hent_posisjon_topp() > 700-50 or self.hent_posisjon_topp() < 0:
      self.snu_topp()
  
  def sett_posisjon(self, venstre, topp):
    self._posisjon_venstre = venstre
    self._posisjon_topp = topp
      
  def sett_fart(self, venstre, topp):
    self._speed_X = venstre
    self._speed_Y = topp
  
  def snu(self):
    self._speed_X = self._speed_X * -1
    self._speed_Y = self._speed_Y * -1

  def snu_venstre(self):
    self._speed_X = self._speed_X * -1

  def snu_topp(self):
    self._speed_Y = self._speed_Y * -1

  def transformer(self):
    if self._type == "stein":
      self._type = "papir"
    elif self._type == "saks":
      self._type = "stein"
    elif self._type == "papir":
      self._type = "saks"
  
  def tegn(self, skjerm):
    skjerm.blit(self._type, (self._posisjon_venstre, self._posisjon_topp)) 

  def hent_posisjon_venstre(self):
    return self._posisjon_venstre

  def hent_posisjon_topp(self):
    return self._posisjon_topp

  def hent_speed_X(self):
    return self._speed_X

  def hent_speed_Y(self):
    return self._speed_Y

  def hent_type(self):
    return self._type