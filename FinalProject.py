class Recipe:

    def slice(self):
        print("Slice ingredients\n")

    def cook(self):
        print("Cook\n")


class Pizza(Recipe):

    def __init__(self,people_num):
        self.people_num = people_num
        self.ingredients = ['flour','sausage','mushroom', 'tomatopaste', 'cheese','water']

    def quantityperperson(self):

        print(str(3 * self.people_num) + ' water glass ' + self.ingredients[0])
        print(str(1.5 * self.people_num) + ' water_glass '+ self.ingredients[5])
        print(str(50 * self.people_num) + ' gr '+ self.ingredients[1])
        print( str(6 * self.people_num) + ' pieces '+ self.ingredients[2])
        print(str(2 * self.people_num) + ' tablespoon '+ self.ingredients[3])
        print(str(20 * self.people_num) + ' tsp '+ self.ingredients[4])

    def dough(self):
        print("Mix the flour with water until it shapes a dough\n")

class Lasaigne(Recipe):

    def __init__(self,people_num):
        self.people_num = people_num
        self.ingredients = ['sliced meat', 'pasta', 'cheese', 'bechamelsauce' ]

    def quantityperperson(self):

        print(str(50 * self.people_num)+' gr ' + self.ingredients[0])
        print(str(0.25 * self.people_num) + ' packets'+ self.ingredients[1])
        print(str(30 * self.people_num) + ' gr '+ self.ingredients[2])
        print(str(20 * self.people_num) + ' ml '+ self.ingredients[3])

    def  place_layers(self):
        print("Place layers as following:\n "
              "1-Place bechamel sauce at the bottom of the tray\n"
              "2-Place lasaigne pasta at the top of the bechamel sauce\n"
              "3-Place sliced meat at the top of the lasaigne pasta"
              "4-Repeat these steps until you run out of ingredients or the tray becomes full\n")

class Noodle(Recipe):

    def __init__(self,people_num):
        self.people_num = people_num
        self.ingredients = ['noodle', 'chicken', 'carrot', 'pepper', 'soysauce']

    def quantityperperson(self):

        print(str(1 * self.people_num)+' packets '+ self.ingredients[0])
        print(str(50 * self.people_num) + ' gr '+ self.ingredients[1])
        print(str(0.25 * self.people_num) + ' pieces '+ self.ingredients[2])
        print(str(1 * self.people_num) + ' pieces '+ self.ingredients[3])
        print(str(2 * self.people_num) + ' tablespoon '+ self.ingredients[4])

    def boil(self):
        print("Boil the noodle for 2 mins\n")


selection = int(input("Please select one of the recipes\n"
      "1-Pizza\n"
      "2-Lasaigne\n"
      "3-Noodle\n"))
num = int(input("Please enter number of person to prepare this recipe\n"))
if selection == 1:
    a = Pizza(num)
    a.quantityperperson()
    a.dough()
    a.slice()
    a.cook()

elif selection == 2:
    b = Lasaigne(num)
    b.quantityperperson()
    b.slice()
    b.place_layers()
    b.cook()

elif selection == 3:
    c = Noodle(num)
    c.quantityperperson()
    c.boil()
    c.slice()
    c.cook()

print("Bon Appetit!")