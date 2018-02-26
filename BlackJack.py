# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 10:12:34 2018

@author: bill harding       

Blackjack program that allows 
-one player
-one split
-$1000 starting monies
-line art cards

improvements would be: 
-to use a dictionary to store player ones hand insted of a list of lists
-inprove the error handeling on the Bet() function, it needs a Try:Except
"""

import random
from time import sleep

class Hand(object):
    
       
    def __init__(self, player, deck1, deck2):
        self.player = player
        self.cards = [deck1.pop(),deck2.pop()]
        self.hands = [self.cards]
        self.bust = [False,False]
        self.split= False
        self.wager = 0

        
    def Show(self,group=0):

        lst= self.hands[group]

        amt_row_p = ''
        suit_row_p = ''
        
        top_row = '\u250c\u2500\u2500\u2510 ' * len(lst)
        for i in range(0,len(lst)):
            amt_row_p += '\u2502'+lst[i][0]+' \u2502 '
            suit_row_p += '\u2502 '+lst[i][1]+'\u2502 '
        bottom_row = '\u2514\u2500\u2500\u2518 ' * len(lst)
        
        print(top_row)
        print(amt_row_p)
        print(suit_row_p)
        print(bottom_row)
        
   
    def Split(self,deck):
        lst = self.hands.pop(0)
        hand0 = Hand(self.player,lst,deck)
        hand1 = Hand(self.player,lst,deck)
        self.hands.extend([hand0.cards])
        self.hands.extend([hand1.cards])
        self.split=True

       
    def Hit(self,group,deck):
        self.hands[group] = self.hands[group] + [deck.pop()]
        
    def Tot(self,group=0):
        lst= self.hands[group]
        total=0
        ace = 0
        for i in range(0,len(lst)):
            if lst[i][0] in ('T','J','Q','K'):
                total += 10
            elif lst[i][0] == 'A':
                ace += 1
            else:
                total += int(lst[i][0])

                
        if ace > 0 :
            for j in range(0,ace):
                if total + 11 <= 21 :
                    total += 11
                else:
                    total += 1
                    
        return total
        
    def Bust(self,group=0):
        if self.Tot(group) > 21:
            self.bust[group]=True
            print('BUST!!')


class Dealer(Hand):
    
        def __init__(self, player, deck1, deck2):
            Hand.__init__(self, player, deck1, deck2)
    
        def Dshow(self):
            top_row = '\u250c\u2500\u2500\u2510 ' * 2
            amt_row_p = '\u2502'+self.cards[0][0]+' \u2502 \u2502\u2743\u2743\u2502 '
            suit_row_p = '\u2502 '+self.cards[0][1]+'\u2502 \u2502\u2743\u2743\u2502'
            bottom_row = '\u2514\u2500\u2500\u2518 ' * 2
        
            print(top_row)
            print(amt_row_p)
            print(suit_row_p)
            print(bottom_row)

        def Play(self,deck,group=0):
            while self.Tot() in range(0,18):
                sleep(2)
                self.Hit(group,deck)
                print('\n\nDealer hitting - ')
                self.Show()
            self.Bust()
                

class Wallet(object):
    
    def __init__(self,value=1000):
        self.amount = value
        
    def Wager(self,amt):
        self.amount -= amt
        
    def Collect(self,amt):
        self.amount += amt
        
    def __str__(self):
        return '$%10.2f \u26c3' % self.amount
    
    
def New(number=3):
    deck=[]
    for i in range(1,number+1):
        for card in ['2','3','4','5','6','7','8','9','T','J','K','Q','A']:
            for suit in ['\u2660','\u2663','\u2665','\u2666']:
                deck.append((card,suit))
                random.shuffle(deck)

    return  deck


def Renew(deck,number=3):
    if len(deck) < 20:
        hold = New(number)
        deck = deck + hold
        
def Pboard(d,p):
    print('\n\n\n\n\nDEALER:')
    d.Dshow()
    print("PLAYER: {}".format(wallet))
    for x in range(0,len(p.hands)):
        p.Show(x)
        if p.bust[x] == True: 
            print('     -BUST-')
        print("Wager=${} \u26c2".format(p.wager))
        
    
def Dboard(d,p):
    print('\n\n\n\n\nDEALER:')
    d.Show()
    if d.bust == True : print('     -BUST-')
    print("PLAYER: {}".format(wallet))
    for x in range(0,len(p.hands)):
        p.Show(x)
        if p.bust[x] == True: 
            print('     -BUST-')
        print("Wager=${} \u26c2".format(p.wager))   
        
def Bet(wallet):

    valid = False
     
    hold = int(input('Player please enter wager ==>'))
    
    while valid == False:
        if not isinstance(hold, (int, float)):
            hold = int(input('Bet must be a number ==>'))
        elif hold <= 0:  
            hold = int(input('NICE TRY Smartypants! Bet must be a number greater than 0 ==>'))
        elif hold > wallet.amount:
            hold = int(input('Bet must be less than or equal to {} ==>'.format(wallet.amount)))
        else:
            valid = True
            wallet.Wager(hold)
            
    return hold

def Compare(p,w,hand,bet):
        print('\n=============================\n')
        if len(p.hands[hand])==2 and player1.Tot(x) == 21:
            print("player's hand {} Blackjack!  Wins ${}\n".format(x+1, bet*2))
            w.Collect(bet*3)
        elif (dealer.Tot() > 21 and player1.Tot(x) <= 21) or (dealer.Tot() < player1.Tot(x) <= 21):
            print("player's hand {} won ${}\n".format(x+1, bet))
            w.Collect(bet*2)
        elif player1.Tot(x) > 21 or ( player1.Tot(x) < dealer.Tot() <= 21):
            print("player's hand {} lost.\n".format(x+1))
        elif dealer.Tot() == player1.Tot(x):
            print("player's hand {} push\n".format(x+1))
            w.Collect(bet)
    
if __name__ == '__main__':    

###########################
## Set up game parameters
###########################
    
    print("""Welcome to BlackJack
            \nPlayer starts with $1000 in tokens.
            \nDealer will hit 17 and below.
            \nYou may split 10,J,K,Q only once, if you have funds.
            \n---------------------------------------------------------\n\n""")
    
    again = True
    mydeck = New(3)
    wallet = Wallet()
    
    while again == True:
        
        ###########################
        ## Deal the cards
        ###########################
        Renew(mydeck,3)
        player1 = Hand(1,mydeck,mydeck)
        dealer = Dealer('dealer',mydeck,mydeck)
        
        ###########################
        ## Let's Rock
        ###########################
        
        player1.wager = Bet(wallet)
    
        Pboard(dealer,player1)
    
        ###########################
        ## Check to see if there 
        ## is possible split
        ###########################
        move = None
    
        if player1.hands[0][0][0] in ('T','J','Q','K') and player1.hands[0][1][0] in ('T','J','Q','K'):
            if player1.wager * 2 > wallet.amount:
                print('You do not have enough funds to split')
            else:
                while move not in ('Y','y','N','n'):
                    move = input('Would you like to split? Y/N ==>')
                    if move in ('Y','y'):
                        player1.Split(mydeck)
                        player1.split = True
                        wallet.Wager(player1.wager)
                        Pboard(dealer,player1)

        ###########################
        ## Play the Players Hand(s)
        ###########################                    
                        
        for i in range(0,len(player1.hands)):
            move = None
            while move != '2' and player1.bust[i] == False:
                
                move = input('Choose: 1=Hit, 2=Stand ==>')
                while move not in ('1','2'):
                    move = input('Choose: 1=Hit, 2=Stand ==>')
    
                if move == '1' :
                    player1.Hit(group=i,deck=mydeck)
                    player1.Bust(i) 
                    Pboard(dealer,player1)
            
        ###########################
        ## Play the Dealers Hand
        ########################### 
        Dboard(dealer,player1)
        
        dealer.Play(deck=mydeck)
    
        Dboard(dealer,player1)
        
        ###########################
        ## Check for win(s)
        ########################### 
            
        for x in range(0,len(player1.hands)):
            Compare(player1,wallet,x,player1.wager)
     
        ###########################
        ## Display new wallet
        ########################### 
        print('\n\n\nPlayer has ${}'.format(wallet.amount))
        
        ###########################
        ## Ask for continue
        ########################### 
        another = None        
        while another not in ('Y','y','N','n'):
            another = input('Play again? Y/N ==>')
            if another in ('N','n'):
                again = False
                
            
