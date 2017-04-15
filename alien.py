# Alien Blaster

class Player(object):
    """ A player in shooter game. """
    def blast(self, enemy):
        print("The player blast an enemy.\n")
        enemy.die()

class Alien(object):
    """ An alien """
    def die(self):
        print("I'm dieing")

# main
print("Death of the alien")

hero = Player()
invader = Alien()
hero.blast(invader)

input("press enter to exit")
