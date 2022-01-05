from class_player import Player
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

positions=['a1','a2','a3','b1','b2','b3','c1','c2','c3']
class Game(Player):
    # POS:(['a1','a2','a3','b1','b2','b3','c1','c2','c3'])
    def __init__(self,):
        # self.position=position
        # positions=['a1','a2','a3','b1','b2','b3','c1','c2','c3']
    def select_board_position(self,player,positions):
        select_pos=input(f"select board position {positions}")#random first then user input
        #or
        random.choice(positions)

        player1_positions=['positions']#naming from Tianyang  
        player2_positions=['positions']#naming from Tianyang  
        player1_positions.append(select_pos)
        player2_positions.append(select_pos)
    def board_position_full(self,player):
        board_pos_full=('choose again position is take by {player}')
        select_pos=input(f"select board position {positions}")
    def three_in_a_row(self,player):
        win=('8 different combinations to win')#a1,a2,a3, x8

    def draw(self,player):
        tie_draw=("board is full or can't win")#end

info = Player('Tim', 'Al')
info.pick_token()
info.go_first()

        