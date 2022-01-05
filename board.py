
empty_board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
def board(self):
    self=empty_board
    a = '|'.join(self[:3:])
    b = '|'.join(self[3:6:])
    c = '|'.join(self[6::])
    print(f'{a}\n{b}\n{c}')
    return
# board([' ',' ',' ',' ',' ',' ',' ',' ',' '])# empty board 
a=board()
a.board()

def board_place(self):
        player1_chos=Game.select_board_position
        if player1_chos== "a1":
            return pos1=a1      #Player.pick_token[player1]
        if player1_chos=="a2":
            return empty_board[a2]="X"
        if player1_chos== "a3":
            return empty_board[a3]=="X"     #Player.pick_token(self=player1)
        if player1_chos=="b1":
            return empty_board[b1]=="X"
        if player1_chos== "b2":
            return empty_board[b2]=="X"     #Player.pick_token(self=player1)
        if player1_chos=="b3":
            return empty_board[b3]=="X"
        if player1_chos== "c1":
            return empty_board[c1]=="X"     #Player.pick_token(self=player1)
        if player1_chos=="c2":
            return empty_board[c2]=="X"
        if player1_chos=="c3":
            return empty_board[c3]=="X" 
        player2_chos=Game.select_board_position
        if player2_chos== "a1":
            return empty_board[a1]=="O"     #Player.pick_token(self=player1)
        if player2_chos=="a2":
            return empty_board[a2]=="O"
        if player2_chos== "a3":
            return empty_board[a3]=="O"     #Player.pick_token(self=player1)
        if player2_chos=="b1":
            return empty_board[b1]=="O"
        if player2_chos== "b2":
            return empty_board[b2]=="O"     #Player.pick_token(self=player1)
        if player2_chos=="b3":
            return empty_board[b3]=="O"
        if player2_chos== "c1":
            return empty_board[c1]=="O"     #Player.pick_token(self=player1)
        if player2_chos=="c2":
            return empty_board[c2]=="O"
        if player2_chos=="c3":
            return empty_board[c3]=="O"       