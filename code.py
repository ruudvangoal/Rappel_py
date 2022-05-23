
class Man:

    def init(self, name):
        self.name = name
        self.money = House.money
        self.meal = House.fridge
        self.satiety = 30
        self.happiness = 100

    def eating(self):
        meal = self.satiety + random.randint(0, 31)
        House.fridge -= meal
        print("{} поел".format(self.name))

    def working(self):
        House.money += 150
        self.satiety -= 10
        print("{} заработал денег, всего в тумбочке {} денег".
              format(self.name, House.money))

    def gaming(self):
        print("А теперь {} может  поиграть!".format(self.name))
        self.satiety -= 10
        self.happiness += 20

    def petting_the_cat(self):
        self.happiness += 5
        self.satiety -= 10
        print("Кот поглажен. Счастья {}. ".format(self.happiness))


