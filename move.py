import class_game

class Board:
    def __init__(self,rows=3,colums=3,size=32):
        self.rows=rows
        self.colums=colums
        self.size=size
    # def __repr__(self):
    
a1=(0)
a2=(1)
a3=(2)
b1=(3)
b2=(4)
b3=(5)
c1=(6)
c2=(7)
c3=(8)

    board=([a1,a2,a3]
    +      [b1,b2,b3]
     +     [c1,c2,c3])


board=([a1,a2,a3]+
        [b1,b2,b3]+
        [c1,c2,c3])   

print(board)
