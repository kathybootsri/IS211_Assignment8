# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 10:59:57 2020

@author: kathy
"""

import datetime
import random
seed_delta = 1
seed = datetime.datetime.now() + datetime.timedelta(days = seed_delta)
random.seed(seed)


import datetime
import random
seed_delta = 1
seed = datetime.datetime.now() + datetime.timedelta(days = seed_delta)
random.seed(seed)



class Pig():
    def __init__(self, players):
        self.players = players      
        print("These are the players in this game: ", self.players)

        
    def StartGame(self, all_moves = [], rolls = []):
        self.all_moves = []
        self.rolls = []          
        self.total_score = 0

        
        start_player = 0
        player_scores = {}        
        player_count = len(self.players)
        
        for x in self.players:
            player_scores[x] = []
        
        #Create player scoreboard
        current_player = self.players[start_player]   
        current_score = sum(player_scores[current_player])
        
        while current_score < 100:    
            current_player = self.players[start_player]    

            roll = random.randint(1, 6)  
        
            if current_player == 'Computer':
                this_turn_rolls = []                

                if current_score < 100:
                    
                    while roll != 1 and sum(this_turn_rolls) < 25 and (sum(this_turn_rolls) < 100 - current_score):  
                        print(f'{current_player} has rolled.') 
                        player_scores[current_player].append(roll)    
                        this_turn_rolls.append(roll) 
                        current_score = sum(player_scores[current_player])
                        print (f"{current_player} rolled a {roll}. Computer's total score is {current_score}.")     
                        
                        if current_score < 100:
                            roll = random.randint(1, 6)
                        
                   
                    if roll == 1 and current_score < 100:  
                        self.rolls.append(0)                      
                        print (f"{current_player} rolled a 1. Next player rolls.")                    
                        if start_player + 1 > player_count - 1:
                            start_player = 0
                        else:
                            start_player += 1 
                        current_player = self.players[start_player]
                        current_score = sum(player_scores[current_player])
                        print(f'{current_player}, would you like to roll or hold?')
                        move = input()                        
                           
                    elif current_score >= 100:
                        print('Computer won!')
                        return None
                    
                    else:                       
                        print (f"{current_player} wants to hold. Next player rolls.")
                        if start_player + 1 > player_count - 1:
                            start_player = 0
                        else:
                            start_player += 1 
                        current_player = self.players[start_player]
                        print(f'{current_player}, would you like to roll or hold?')
                        move = input()                                                       
                 
                    
            else:
                print(f'{current_player}, would you like to roll or hold?')
                move = input()
                        
            if move == 'r' and current_score < 100:
                if roll != 1:               
                    player_scores[current_player].append(roll)    
                    current_score = sum(player_scores[current_player])
                    print (f"{current_player} rolled a {roll}. Your total score is {current_score}.")               
                    
                if roll == 1:                           
                    self.rolls.append(0)                      
                    print (f"{current_player} rolled a 1. Next player rolls.")                    
                    if start_player + 1 > player_count - 1:
                        start_player = 0
                    else:
                        start_player += 1 
                    
            elif move == 'h':                       
                print (f"{current_player} wants to hold. Next player rolls.")
                roll = random.randint(1, 6)
                if start_player + 1 > player_count - 1:
                    start_player = 0
                else:
                    start_player += 1                 
            
            elif move == 'stop':
                return None
        
            else:
                print ('Not a valid move, enter r or h for your move.')
        
        else:
            import operator
            
            total_scores = {}
            
            for key, values in player_scores.items():
                total_scores[key] = sum(values)
                
            winner = max(total_scores.items(), key=operator.itemgetter(1))[0]
            max_score = max(total_scores.values())
            current_score = player_scores[current_player]
            
            print (f"{winner} won with a score of {max_score}!")
            return None


class TimedGameProxy(Pig):
    def __init__(self, players):
        super().__init__(players)     
        
    def StartGame(self, start_time = datetime.datetime.now(), end_time = datetime.datetime.now() + datetime.timedelta(minutes = 1), all_moves = [], rolls = []):
        self.all_moves = []
        self.rolls = []          
        self.total_score = 0     
        self.start_time = datetime.datetime.now()
        self.end_time = self.start_time + datetime.timedelta(seconds = 60)

        print(f"The game has started! You have one minute to finish the game.")
        
        start_player = 0
        player_scores = {}        
        player_count = len(self.players)
        
        for x in self.players:
            player_scores[x] = []
        
        #Create player scoreboard
        current_player = self.players[start_player]   
        current_score = sum(player_scores[current_player])
        
        while current_score < 100 and datetime.datetime.now() < self.end_time:    
            current_player = self.players[start_player]    
        
            roll = random.randint(1, 6)  
        
            print(f'{current_player}, would you like to roll or hold?')
            move = input()
            
            if move == 'r' and current_score < 100:
                if roll != 1:               
                    player_scores[current_player].append(roll)    
                    current_score = sum(player_scores[current_player])
                    print (f"{current_player} rolled a {roll}. Your total score is {current_score}.")               
                    if start_player + 1 > player_count - 1:
                        start_player = 0
                    else:
                        start_player += 1  
                        
                if roll == 1:                           
                    self.rolls.append(0)                      
                    print (f"{current_player} rolled a 1. Next player rolls.")                    
                    if start_player + 1 > player_count - 1:
                        start_player = 0
                    else:
                        start_player += 1 
                    
            elif move == 'h':                       
                print (f"{current_player} wants to hold. Next player rolls.")
                if start_player + 1 > player_count - 1:
                    start_player = 0
                else:
                    start_player += 1                 
            
            else:
                print ('Not a valid move, enter roll or hold for your move.')
        
        else:
            import operator
            
            total_scores = {}
            
            for key, values in player_scores.items():
                total_scores[key] = sum(values)
                
            winner = max(total_scores.items(), key=operator.itemgetter(1))[0]
            max_score = max(total_scores.values())
            current_score = player_scores[current_player]
            
            if datetime.datetime.now() < self.end_time:
                print (f"Times up! {winner} won with a score of {max_score}!")
                return None
            
            else: 
                print (f"{winner} won with a score of {max_score}!")
                return None

"""TEST COMPUTER PLAYER"""
game = Pig(['Jim', 'Computer'])

game.StartGame()
    

"""TEST TIMED GAME PROXY"""           
timed = TimedGameProxy(['Jim', 'James'])

timed.StartGame()

