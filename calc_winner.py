

w1=set(['a1','a2','a3'])  
w2=set(['b1','b2','b3']) 
w3=set(['c1','c2','c3']) 
w4=set(['a1','b1','c1'])
w5=set(['a2','b2','c2'])
w6=set(['a3','b3','c3']) 
w7=set(['a1','b2','c3']) 
w8=set(['a3','b2','c1'])

lists=(w1,w2,w3,w4,w5,w6,w7,w7)

def list_check_winner(list1):
    if all(i in list1 for i in w1):
        print('w1')
    elif all(i in list1 for i in w2):
        print('w2')
    elif all(i in list1 for i in w3):
        print('w3')
    elif all(i in list1 for i in w4):
        print('w4')
    elif all(i in list1 for i in w5):
        print('w5') 
    elif all(i in list1 for i in w6):
        print('w6')
    elif all(i in list1 for i in w7):
        print('w7')
    elif all(i in list1 for i in w8):
        print('w8')             
    else:
        print('not a winner')


def pos_win(player1_pos):
    for list in lists:
       if list == player1_pos:
        return   list
 
def pos_win_list(list1,list2=lists):
    for list in lists:
       if all(i in list1 for i in list2):
        return   list


def calc_winner(p1,p2,player1_pos,player2_pos):
    a=pos_win(player1_pos)
    b=pos_win(player2_pos)
    win1=a
    win2=b
    if player1_pos == win1:
        return f'{p1} wins'
    elif player2_pos == win2:
        return f'{p2} wins'

player1='Jane'
player2='John'

player1_pos=set(['b3','2c','c3'])
player2_pos=set(['a1','b1', 'b3','b2'])

# list_check(player2_pos,w1)

# pos_win_list(player2_pos)
list_check(player2_pos)

intersec=player2_pos.intersection(w1&w2&w3&w4&w5&w6&w7)
print(intersec)
#print(lists[0].intersection(*player2_pos))
# ab=set.intersection(*[set(player2_pos) for x in lists])  
# print(ab)


win=calc_winner(player1,player2,player1_pos,player2_pos)
print(win)

w1=set(['a1','a2','a3'])  
w2=set(['b1','b2','b3']) 
w3=set(['c1','c2','c3']) 
w4=set(['a1','b1','c1'])
w5=set(['a2','b2','c2'])
w6=set(['a3','b3','c3']) 
w7=set(['a1','b2','c3']) 
w8=set(['a3','b2','c1'])

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

def pos_win(a):
    for list in lists:
       if list == a:
        return   list