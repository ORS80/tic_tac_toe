
class Board:
    def __repr__(self,rows=3,colums=3):
        self.rows=rows
        self.colums=colums
        return f'Board({self.x},{self.y})'
print(Board(0,1))

# def board_positions_full(self):#code needed for user input 
    #     board_pos_full=('choose again position is taken')
    #     select_pos=input(f"select board position {positions}")
    # def three_in_a_row(self):#after third round look for winner
    #     win=('8 different combinations to win')#a1,a2,a3, x8

    # def draw(self):
    #     positions=[]#no winner and board is full
    #     tie_draw=("board is full or can't win")#end