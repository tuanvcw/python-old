# A Critter
# One of my first OOP

class Critter(object):
    """ A virtual pet """
    def __init__(self, energy = 0, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        self.energy = energy

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        self.energy = 0 - unhappiness
        if unhappiness < 5:
            m = "happy"
        elif 5<= unhappiness <= 10:
            m = "mkay"
        elif 11 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m

    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time()

    def eat(self):
        food = int(input("How much you want to feed: "))
        print("Brruppp. I'm full.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print("Wheee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()
        
def main():
    crit_name = input("Name of your critter: ")
    crit = Critter(crit_name)

    choice = None
    while choice != "0":
        print \
        ("""
Rasing Critter Game

0 - Quit
1 - Listen to your critter
2 - Feed it
3 - Play with it
""")
        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Good-bye.")
        elif choice == "1":
            crit.talk()
        elif choice == "2":
            crit.eat()
        elif choice == "3":
            crit.play()
        else:
            print("\nSorry, but", choice, "is not a valid choice")

main()
print(crit.energy)
input("Press enter key to exit")

