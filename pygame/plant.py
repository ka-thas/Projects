import datetime
import math

# Handling the logic for a pygame


class Plant:
    def __init__(self):
        self.name = "Ka's bud"
        self.pot = 0
        self.start = None
        self.last_watered = None
        self.level = 0
        self.is_dead = False

        self.read_from_file()

    def info(self):
        print(
            f"name = {self.name} \nlevel = {self.level} \npot = {self.pot} \nstart = {self.start} \nlast_watered = {self.last_watered}"
        )

    def give_water(self):
        self.last_watered = datetime.datetime.now()
        self.check_water(datetime.datetime.now())

    def check_water(self, now):
        since_watered = (now - self.last_watered).seconds
        print("since_watered:", since_watered)
        if since_watered > 15:
            self.dead()
        elif since_watered > 12:
            print("Time since watered: ", since_watered, "(Dry)")
        elif since_watered > 9:
            print("Time since watered: ", since_watered, "(Thirsty)")
        elif since_watered > 3:
            print("Time since watered: ", since_watered, "(Satisfied)")
        elif since_watered > 3:
            print("Time since watered: ", since_watered, "(Drowning)")

    def check_level(self, now):
        self.level = (now - self.start).seconds // 300
        print(self.level)

    def update(self):
        if self.is_dead:
            return

        now = datetime.datetime.now()
        print("now: ", now)
        self.check_water(now)
        self.check_level(now)

    def save_to_file(self):
        # §-seperated values
        f = open("plant_save.txt", "w")
        text = f"{self.name}§{self.pot}§{str(self.start)}§{str(self.last_watered)}"
        f.write(text)
        f.close()

    def new_plant(self):
        print("New plant!")
        self.name = input("Name: ")
        self.pot = int(input("Pot: "))
        now = datetime.datetime.now()
        self.start = now
        self.last_watered = now
        self.save_to_file()

    def read_from_file(self):
        try:
            with open("plant_save.txt", "r") as file:
                file_data = file.readline().split("§")
                self.name = file_data[0]
                self.pot = file_data[1]
                self.start = datetime.datetime.strptime(
                    file_data[2], "%Y-%m-%d %H:%M:%S.%f"
                )
                self.last_watered = datetime.datetime.strptime(
                    file_data[3], "%Y-%m-%d %H:%M:%S.%f"
                )

        except FileNotFoundError:
            self.new_plant()

    def dead(self):
        print("died")
        self.is_dead = True

    def restart(self):
        print("Restart!")
        self.new_plant()


def main():
    plant = Plant()
    plant.info()
    plant.update()
    plant.give_water()
    plant.update()
    plant.save_to_file()


if __name__ == "__main__":
    main()
