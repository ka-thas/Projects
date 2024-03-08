import pgzrun
from spillbrett import Spillbrett
from random import randint

# Her lager vi et nytt spillbrett og oppretter to sauer med ulike bilder og ulike start-posisjoner
spillbrett = Spillbrett()
for i in range(90):
    spillbrett.make_hand("stein", randint(0, 850), randint(0, 650))
    spillbrett.make_hand("saks", randint(0, 850), randint(0, 650))
    spillbrett.make_hand("papir", randint(0, 850), randint(0, 650))

WIDTH = 900
HEIGHT = 700


def draw():
    screen.fill((100, 90, 120))
    spillbrett.tegn(screen)


def update():
    spillbrett.oppdater()


pgzrun.go()
