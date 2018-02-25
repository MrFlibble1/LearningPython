# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 10:33:31 2018

@author: bill harding

This program is a simple tic-tac-toe program requiring 2 players
"""

## i decided to use simple line drawing charicters to create the board
def draw_board(brd):
    print('''  a b c\n1 {}\u2502{}\u2502{}\n  \u2500\u253c\u2500\u253c\u2500\n2 {}\u2502{}\u2502{}\n  \u2500\u253c\u2500\u253c\u2500\n3 {}\u2502{}\u2502{}
    '''.format(brd[0][0],brd[0][1],brd[0][2],
            brd[1][0],brd[1][1],brd[1][2],
            brd[2][0],brd[2][1],brd[2][2]))
            
## players place pieces using the 'batle ship' method of lettered columns and numbered rows
def get_move(player):
    column = ''
    row = ''
    while column.lower() not in ('a','b','c'):
        column = input(f"Player{player} enter a valid column letter: ")
    while row not in ('1','2','3'):
        row = input(f"Player{player} enter a valid row number: ")
    
    
    row = int(row) -1
    column = column.lower()
    
    #translate column letter to number
    trans={'a':0, 'b':1, 'c':2}
    
    return(trans[column],row)


## player1 is 'X' and player2 is 'O'
def place_move(player,c,r,board_string):
    r=int(r)
    c=int(c)
    
    if player == 1:
        token = 'X'
    else:
        token = 'O'
        
    board_string[r][c] = token
    
    return(board_string)
    
def check_win(board,player):
    for c in (0,1,2):
        if board[0][c] == board[1][c] == board[2][c] != ' ':
            print(f'Player{player} WINS!')
            done=True
            break
        else:
            for r in (0,1,2):
                if board[r][0] == board[r][1] == board[r][2] != ' ':
                    print(f'Player{player} WINS!')
                    done=True
                    break
                else:
                    done=False
    if done == False:
        if board[0][0] == board[1][1] == board[2][2] != ' ':
            print(f'Player{player} WINS!')
            done=True
        elif board[2][0] == board[1][1] == board[0][2] != ' ':
            print(f'Player{player} WINS!')
            done=True
        else:
            done=False

    return(done)

def determine_player(move):
    if move%2 == 0:
        player = 2
    else:
        player = 1
        
    return(player)
    
def clean_board():
    board=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    
    return(board)

def check_legal_move(c,r,board):
    r=int(r)
    c=int(c)
    if board[r][c] == ' ':
        legal=True
    else:
        legal=False
    return(legal)
    
if __name__ == '__main__':
    
    board = clean_board()
    move=1
    over = False
    
    draw_board(board)
    
    
    while over == False:
        legal = False
        plr = determine_player(move)
        while legal == False:
            c, r = get_move(plr)
            legal=check_legal_move(c,r,board)
        board = place_move(plr,c,r,board)
        draw_board(board)
        over = check_win(board,plr)
        move += 1
        if move == 10 and over == False:
            print("It's a tie!")
            over = True
        
    print('Good Game!')
        

    
