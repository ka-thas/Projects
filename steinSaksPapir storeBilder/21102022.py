import random
random.seed(1)

tall = [1, 5, 29, 1, 1]
resultat = (i*random.randint(0,10) for i in tall)
for r in resultat:
  print(r)