class Player:
    def __init__(self, x, y, health):
        self.x = x
        self.y = y
        self.health = health

    def show_info(self):
        print("Player")
        print("Position:", self.x, self.y)
        print("Health:", self.health)

class Bot:
    def __init__(self, x, y, health):
        self.x = x
        self.y = y
        self.health = health

    def show_info(self):
        print("Bot")
        print("Position:", self.x, self.y)
        print("Health:", self.health)

    def move_right(self):
        self.x += 1

    def move_left(self):
        self.x -= 1

    def move_down(self):
        self.y += 1

    def move_up(self):
        self.y -= 1

player = Player(10, 20, 100)
bot = Bot(0, 0, 100)

player.show_info()
print()

bot.show_info()
print()

bot.move_right()
bot.move_right()
bot.move_down()

print("After moving:")
bot.show_info()