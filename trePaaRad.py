brett = ["1","2","3",
         "4","5","6",
         "7","8","9"]
toggle = ["X","O"]         
def ledigFelt(a):
  if brett[a] != str(a + 1):
    return False
  else:
    return True

def test():
  if brett[0]==brett[1]==brett[2]:
    return True
  elif brett[3]==brett[4]==brett[5]:
    return True
  elif brett[6]==brett[7]==brett[8]:
    return True
  elif brett[0]==brett[3]==brett[6]:
    return True
  elif brett[1]==brett[4]==brett[7]:
    return True
  elif brett[2]==brett[5]==brett[8]:
    return True
  elif brett[0]==brett[4]==brett[8]:
    return True
  elif brett[2]==brett[4]==brett[6]:
    return True
  else:
    return False

game = True
while game:
  print("")
  print("|",brett[0],brett[1],brett[2],"|")
  print("|",brett[3],brett[4],brett[5],"|")
  print("|",brett[6],brett[7],brett[8],"|")
  runde = True
  while runde:
    spiller = int(input(toggle[0] + " sin tur (1-9): ")) - 1
    if spiller < 1 and spiller > 9:
      print("Oppgi gyldig plass") 
    elif ledigFelt(spiller):
      brett[spiller] = toggle[0]
      toggle.reverse()
      runde = False
    else:
      print("Det feltet er tatt!")

  bunny = test()
  if bunny:
    print(toggle[1] + " vant!")
    game = False