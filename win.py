#p(1+round#)--> p11 will be player1 with round 1, p2 will be player2 with round 2
#board.is_game_over() >>> just for win only not check full
'''only have 8 options to win: 
A1,A2,A3
B1,B2,B3
C1,C2,C3
A1,B1,C1
A2,B2,C2,
A3,B3,C3,
A1,B2,C3
A3,B2,C1
A1 = (0,0), A2 = (1,0), A3 = (2,0)
B1 = (0,1), B2 = (1,1), B3 = (2,1)
C1 = (0,2), C2 = (1,2), C3 = (2,2)
'''
p11 = input('Place your token: ')
print()#print board with p11 under move method
p21 = input('Place your token: ')
print()#print board with p21 under move method
p12 = input('Place your token: ')
print()#print board with p12  under move method
p22 = input('Place your token: ')
print()#print board with p22 under move method
p13 = input('Place your token: ')
print()#print board with p13 under move method
if board.is_game_over() == True:
    board.calc_winner()-->#find out 'x'or'o' --> player1 or player2
    print(f'player1/player2 won')
else:
    p23 = input('Place your token: ')
    print()#print board with p23 under move method
    if board.is_game_over() == True:
        board.calc_winner()-->#find out 'x'or'o' --> player1 or player2
        print(f'player1/player2 won')
    else:
        p14 = input('Place your token: ')
        print()#print board with p14 under move method
        if board.is_game_over() == True:
            board.calc_winner()-->#find out 'x'or'o' --> player1 or player2
            print(f'player1/player2 won')
        else:
            p24 = input('Place your token: ')
            print()#print board with p24 under move method
            if board.is_game_over() == True:
                board.calc_winner()-->#find out 'x'or'o' --> player1 or player2
                print(f'player1/player2 won')
            else:
                p15 = input('Place your token: ')
                print()#print board with p15 under move method
                if board.is_game_over() == True:
                    board.calc_winner()-->#find out 'x'or'o' --> player1 or player2
                    print(f'player1/player2 won')
                else:
                    print(f'No winner and board is full, game withdraw')