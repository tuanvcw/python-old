# television

class Television(object):
    """ A Television """
    def __init__(self, volume = 20, channel = 1):
        self.volume = volume
        self.channel = channel

    def volume_up(self):
        self.volume += 10

    def volume_down(self):
        self.volume -= 10

    def channel_up(self):
        self.channel += 1

    def channel_down(self):
        self.channel -= 1

    def display(self):
        print("""
    =========================
    |  This is tuanvc's TV  |
    |                       |
    | 0 - Exit              |
    | 1/2 - volume up/down  |
    | 3/4 - channel up/down |
    =========================
    """)
        print("Channel: ", self.channel, "Volume: ", self.volume)

def main():
    tv = Television()
    tv.display()

    choice = None
    while choice != 0:
        choice = int(input("Your choice: "))
        if choice == 1:
            tv.volume_up()
        elif choice == 2:
            tv.volume_down()
        elif choice == 3:
            tv.channel_up()
        elif choice == 4:
            tv.channel_down()
        else:
            print("Invalid choice")
        tv.display()
        
main()
input = ("press enter to exit")
