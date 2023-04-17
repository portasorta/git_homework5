class game:
    type_class = 'hack & slash'
    def __init__(self, name, year, platform):
        self.name = name
        self.year = year
        self.platform = platform

    def run(self):
        return 'I can play on xbox360!'

    def getname(self):
        return f'game: {self.name}'

game_sl1 = game('Ninja Gaiden 2', 2009, 'xbox360')
game_sl2 = game('Ninja Gaiden 3', 2012, 'many')


class game2(game):

    def __init__(self, name, year, platform, platform2):
        super().__init__(name, year, platform)
        self.platform2 = platform2

    def run(self):
        return 'I can play on ps3 and xbox360'


game_sl3 = game2('Ninja Gaiden 3', 2012, 'PS3', 'xbox360')
print(game_sl3.getname())
print(game_sl3.type_class)
print(game_sl3.run())


print(game_sl3.__dict__)

