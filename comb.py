w1=set(['a1','a2','a3'])  
w2=set(['b1','b2','b3']) 
w3=set(['c1','c2','c3']) 
w4=set(['a1','b1','c1'])
w5=set(['a2','b2','c2'])
w6=set(['a3','b3','c3']) 
w7=set(['a1','b2','c3']) 
w8=set(['a3','b2','c1'])

lists=(w1,w2,w3,w4,w5,w6,w7,w7)






def pos_win(a):
    for list in lists:
       if list == a:
        return   list
import random

def place(player1_chos,player2_chos):
        
        if player1_chos== "a1":
            return 0      #Player.pick_token[player1]
        if player1_chos=="a2":
            return 1
        if player1_chos== "a3":
            return 2     #Player.pick_token(self=player1)
        if player1_chos=="b1":
            return 3
        if player1_chos== "b2":
            return 4  #Player.pick_token(self=player1)
        if player1_chos=="b3":
            return 5
        if player1_chos== "c1":
            return 6    #Player.pick_token(self=player1)
        if player1_chos=="c2":
            return 7
        if player1_chos=="c3":
            return 8
        
        if player2_chos== "a1":
            return 0   #Player.pick_token(self=player1)
        if player2_chos=="a2":
            return 1
        if player2_chos== "a3":
            return 2    #Player.pick_token(self=player1)
        if player2_chos=="b1":
            return 3
        if player2_chos== "b2":
            return 4     #Player.pick_token(self=player1)
        if player2_chos=="b3":
            return 5
        if player2_chos== "c1":
            return 6     #Player.pick_token(self=player1)
        if player2_chos=="c2":
            return 7
        if player2_chos=="c3":
            return 8      





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
player1_pos=[]
player2_pos=[]
empty_board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
a1=(0)
a2=(1)
a3=(2)
b1=(3)
b2=(4)
b3=(5)
c1=(6)
c2=(7)
c3=(8)
class Game(Player):
    
    def __init__(self,player1,player2):
        super().__init__(player1,player2)
        Player.player1=player1
        Player.player2=player2
        
   
        
    def board(self):
        self=empty_board
        a = '|'.join(self[:3:])
        b = '|'.join(self[3:6:])
        c = '|'.join(self[6::])
        print(f'{a}\n{b}\n{c}')
        return
   
    def select_board_position(self):
        player1=Player.player1
        player2=Player.player2
        
        #player1_chos=input(f"select board position {positions}")# need error handling for user input
        player1_chos=random.choice(positions)
        ans=player1_chos
        print(player1_chos)
        
        Game.board_place(self)
        a=place(player1_chos=player1_chos,player2_chos="")
        print(a)
        empty_board[a]="X"
        Game.board(self)
        positions.remove(ans)
        player1_pos.append(ans)
        Game.list_check_winner(player1_pos,player1)
        #print(f'{a} {player1} is winner')
        print(f'{player1} {player1_pos}')
        
        
       # player2_chos=input(f"select board position {positions}")# need error handling for user input
        player2_chos=random.choice(positions)
        ans=player2_chos
        print(player2_chos)
        b=place(player1_chos="",player2_chos=player2_chos)
        print(b)
        empty_board[b]="O"
        Game.board(self)
        positions.remove(ans)
        player2_pos.append(ans)
        
        print(f'{player2} {player2_pos}')
        Game.list_check_winner(player2_pos,player2)

        
        print(f'Positions left on the board {positions}')

    def board_place(self):
        if player1_pos== "a1":
            a1
    def calc_winner(player1_pos=set(player1_pos),player2_pos=set(player2_pos)):
        player1=Player.player1
        player2=Player.player2
        print(player1_pos)
        print(player2_pos)
        a=pos_win(player1_pos)
        b=pos_win(player2_pos)
        win1=a
        win2=b
        if player1_pos == win1:
            return f'{player1} wins'
            print('win')
        elif player2_pos == win2:
            return f'{player2} wins'
            print('win')
        else:
            print('No winner yet')
    def list_check_winner(list1,player):
        if all(i in list1 for i in w1):
            print(f'{player} is winner')
        elif all(i in list1 for i in w2):
            print(f'{player} is winner')
        elif all(i in list1 for i in w3):
            print(f'{player} is winner')
        elif all(i in list1 for i in w4):
            print(f'{player} is winner')
        elif all(i in list1 for i in w5):
            print(f'{player} is winner') 
        elif all(i in list1 for i in w6):
            print(f'{player} is winner')
        elif all(i in list1 for i in w7):
            print(f'{player} is winner')
        elif all(i in list1 for i in w8):
            print(f'{player} is winner')             
        else:
            print(f'{player} is not a winner')

info = Player('Tim', 'Al')
info.pick_token()
info.go_first()
info=Game('Tim', 'Al')
info.select_board_position()
info.board()
info.select_board_position()
info.select_board_position()  
info.select_board_position()  