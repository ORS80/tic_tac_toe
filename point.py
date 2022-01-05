import random


positions=['a1','a2','a3','b1','b2','b3','c1','c2','c3']
player1_pos=[]
player2_pos=[]
def position_selection():
    player1=random.choice(positions)
    ans=player1
    positions.remove(ans)
    player1_pos.append(ans)
    player2=random.choice(positions)
    ans=player2
    positions.remove(ans)
    player2_pos.append(ans)
 

position_selection()
print(positions)
print(player1_pos)
print(player2_pos)

position_selection()
print(positions)
print(player1_pos)
print(player2_pos)

position_selection()
print(positions)
print(player1_pos)
print(player2_pos)
