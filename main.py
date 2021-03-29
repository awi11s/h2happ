from elo_rating import *
from tkinter import *
import random
import pandas as pd
import csv



i = Implementation()

# window = Tk()
# window.title('By Miguel')
# window.geometry('350x200')



# start a new game
def start_file():
    with open('ratings.csv','w', newline='') as out:
        csv_out = csv.writer(out)
        csv_out.writerow(['player', 'score'])

# save the state of the game
def save_game_state(player_list):
    with open('ratings.csv','w', newline='') as out:
        csv_out = csv.writer(out)
        csv_out.writerow(['player', 'score'])
        for row in player_list:
            csv_out.writerow(row)
            
# imports a saved game state 

def import_names():
    with open('ratings.csv', 'r') as f:
        csv_reader = csv.reader(f)
        header = next(csv_reader)
    
        if header != None:
            ratings_list = list(map(tuple, csv_reader))

    for n in ratings_list:
        help = i.addPlayer(n[0], rating = float(n[1]))

    new_list = i.getRatingList()

    return new_list

# add a new player to the game
def append_new(name):
    i.addPlayer(str(name))

    names = i.getRatingList()
    for n in range(len(names)):
        if name == names[n][0]:
            print('new player has been added')
        else:
            pass
    
    print(names)

# resume a saved match
def resume_match(file):
    with open(file, 'r') as f:
        csv_reader = csv.reader(f)
        header = next(csv_reader)
        
        if header != None:
            ratings_list = list(map(tuple, csv_reader))
    
    old_list = i.getRatingList()

    if len(old_list) <= 0:
        for n in ratings_list:
            i.addPlayer(n[0], rating = float(n[1]))
        new_list = i.getRatingList()

        ri1 = random.randrange(len(new_list))
        ri2 = random.randrange(len(new_list))


        player1 = new_list[ri1][0]
        player2 = new_list[ri2][0]

        if player1 == player2:
            rchoice = int(random.random()*len(new_list))
            player2 = new_list[rchoice][0]
        else:
            pass

        print(player1 + ' vs. ' + player2)
        win = input('who wins? ')

        i.recordMatch(player1, player2, winner = str(win))

        updated_list = i.getRatingList()

    else:
        new_list = i.getRatingList()
        ri1 = random.randrange(len(new_list))
        ri2 = random.randrange(len(new_list))
        

        player1 = new_list[ri1][0]
        player2 = new_list[ri2][0]

        if player1 == player2:
            rchoice = int(random.random()*len(new_list))
            player2 = new_list[rchoice][0]
        else:
            pass

        print(player1 + ' vs. ' + player2)

        match_win = input('who wins? ')

        i.recordMatch(player1, player2, winner= match_win)
        updated_list = i.getRatingList()
    
    

def restart_game():
    with open('ratings.csv', 'r') as f:
        csv_reader = csv.reader(f)
        header = next(csv_reader)
        
        if header != None:
            ratings_list = list(map(tuple, csv_reader))
    
    old_list = i.getRatingList()

    for n in ratings_list:
        i.addPlayer(n[0], rating = float(1000))
    new_list = i.getRatingList()
    
    print('a new game is now ready, with ' + str(len(new_list)) + ' players.')
    print('type done before starting a new match.')

    return new_list

def view_board():
    board_list = i.getRatingList()

    board_df = pd.DataFrame(board_list, columns = ['player', 'score'])

    sorted_df = board_df.sort_values(by='score', ascending=False)

    print(sorted_df.head())

if __name__ == '__main__':
    while True:
        start = input('what would you like to do? ')

        if start == 'insert':
            names = i.getRatingList()
            if len(names) == 0:
                import_names()
            else:
                name = input('name: ')
                append_new(name)
        elif start == 'restart':

            restart_game()

        elif start == 'start':

            start_file()
        elif start == 'scoreboard':
            view_board()

        elif start == 'done':

            player_list = i.getRatingList()
            if len(player_list) > 0:
                save_game_state(player_list)
                print('game has been saved')
            else:
                pass

        elif start == 'match':
            resume_match('ratings.csv')
        elif start == 'exit':
            break

    
