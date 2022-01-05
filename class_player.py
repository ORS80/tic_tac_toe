import random
class Player:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
    def pick_token(self):
        result1 = random.randint(0,2)
        if result1 == 0:
            print(f"{self.player1} picks 'X'\n{self.player2} picks 'O'")
        else:
            print(f"{self.player1} picks 'O'\n{self.player2} picks 'X'")
    def go_first(self):
        result2 = random.randint(0,2)
        if result2 == 0:
            print(f'{self.player1} goes first!')
        else:
            print(f'{self.player2} goes first!')
info = Player('Tim', 'Al')
info.pick_token()
info.go_first()