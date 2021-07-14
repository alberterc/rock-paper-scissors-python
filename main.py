import random
from tkinter import *

#player input buttons
def on_rock_button():
    global is_on_rock
    global is_on_paper
    global is_on_scissors
    global player_choice

    if is_on_rock == True and (is_on_paper == True and is_on_scissors == True):
        rock_button.config(bg = 'lightgray')
        player_choice_text.config(text = 'Your Choice: Rock')
        player_choice_text.place(x = 175, y = 220)
        player_choice = 'rock'
        is_on_rock = False
    elif is_on_rock == False and (is_on_paper == True and is_on_scissors == True):
        rock_button.config(bg = 'white')
        player_choice_text.config(text = 'Your Choice: ')
        player_choice_text.place(x = 196, y = 220)
        player_choice = ''
        is_on_rock = True
def on_paper_button():
    global is_on_rock
    global is_on_paper
    global is_on_scissors
    global player_choice

    if is_on_paper == True and (is_on_rock == True and is_on_scissors == True):
        paper_button.config(bg = 'lightgray')
        player_choice_text.config(text = 'Your Choice: Paper')
        player_choice_text.place(x = 172, y = 220)
        player_choice = 'paper'
        is_on_paper = False
    elif is_on_paper == False and (is_on_rock == True and is_on_scissors == True):
        paper_button.config(bg = 'white')
        player_choice_text.config(text = 'Your Choice: ')
        player_choice_text.place(x = 196, y = 220)
        player_choice = ''
        is_on_paper = True
def on_scissors_button():
    global is_on_rock
    global is_on_paper
    global is_on_scissors
    global player_choice

    if is_on_scissors == True and (is_on_rock == True and is_on_paper == True):
        scissors_button.config(bg = 'lightgray')
        player_choice_text.config(text = 'Your Choice: Scissors')
        player_choice_text.place(x = 163, y = 220)
        player_choice = 'scissors'
        is_on_scissors = False
    elif is_on_scissors == False and (is_on_rock == True and is_on_paper == True):
        scissors_button.config(bg = 'white')
        player_choice_text.config(text = 'Your Choice: ')
        player_choice_text.place(x = 196, y = 220)
        player_choice = ''
        is_on_scissors = True

#submit button processes computer choices and game logic
def submit_process():
    choices = ['rock', 'paper', 'scissors']

    if is_on_rock == False or is_on_paper == False or is_on_scissors == False:
        #pick a random choice from the choices
        computer_choice = random.choice(choices)

        #computer choice output
        if computer_choice == 'rock':
            computer_choice_text.config(text = 'Computer Choice: Rock')
            computer_choice_text.place(x = 160, y = 270)
        elif computer_choice == 'paper':
            computer_choice_text.config(text = 'Computer Choice: Paper')
            computer_choice_text.place(x = 155, y = 270)
        elif computer_choice == 'scissors':
            computer_choice_text.config(text = 'Computer Choice: Scissors')
            computer_choice_text.place(x = 145, y = 270)
        
        #disable the buttons after being submitted
        rock_button.config(state = 'disabled')
        paper_button.config(state = 'disabled')
        scissors_button.config(state = 'disabled')
        submit_button.config(state = 'disabled')

        #game logic
        if player_choice == computer_choice:
            result_text.config(text = 'Tie!')
            result_text.place(x = 230, y = 320)
        elif player_choice == 'rock' and computer_choice == 'paper':
            result_text.config(text = 'Computer Wins!')
            result_text.place(x = 183, y = 320)
        elif player_choice == 'rock' and computer_choice == 'scissors':
            result_text.config(text = 'You Win!')
            result_text.place(x = 208, y = 320)
        elif player_choice == 'paper' and computer_choice == 'scissors':
            result_text.config(text = 'Computer Wins!')
            result_text.place(x = 183, y = 320)
        elif player_choice == 'paper' and computer_choice == 'rock':
            result_text.config(text = 'You Win!')
            result_text.place(x = 208, y = 320)
        elif player_choice == 'scissors' and computer_choice == 'rock':
            result_text.config(text = 'Computer Wins!')
            result_text.place(x = 183, y = 320)
        elif player_choice == 'scissors' and computer_choice == 'paper':
            result_text.config(text = 'You Win!')
            result_text.place(x = 208, y = 320)

#resets every buttons and variables
def reset_game():
    #resets the variables
    global is_on_rock
    global is_on_paper
    global is_on_scissors
    global player_choice
    is_on_rock = True
    is_on_paper = True
    is_on_scissors = True
    player_choice = ''

    #resets the choice player chose
    player_choice_text.config(text = 'Your Choice: ')
    player_choice_text.place(x = 196, y = 220)

    #resets the choice computer chose
    computer_choice_text.config(text = 'Computer Choice: ')
    submit_button.place(x = 210, y = 130)

    #resets result text
    result_text.config(text = '')
    result_text.place(x = 155, y = 320)

    #resets the buttons
    rock_button.config(state = 'normal', bg = 'white')
    paper_button.config(state = 'normal', bg = 'white')
    scissors_button.config(state = 'normal', bg = 'white')
    submit_button.config(state = 'normal', bg = 'white')

#init variables
global is_on_rock
global is_on_paper
global is_on_scissors
global player_choice
is_on_rock = True
is_on_paper = True
is_on_scissors = True
player_choice = ''

#init the main window
master = Tk()
master.title('Rock Paper Scissors')
master.resizable(False, False)
master.geometry('500x500')

#title on the most top of the main window
top_title = Label(master,
                font = ('Times New Roman', 20),
                text = 'ROCK - PAPER - SCISSORS'
                )
top_title.pack()

#player input buttons
rock_button = Button(master,
                font = ('Times New Roman', 15),
                text = 'Rock',
                bg = 'white',
                padx = 16,
                command = on_rock_button
                )
paper_button = Button(master,
                font = ('Times New Roman', 15),
                text = 'Paper',
                bg = 'white',
                padx = 15,
                command = on_paper_button
                )
scissors_button = Button(master,
                font = ('Times New Roman', 15),
                text = 'Scissors',
                bg = 'white',
                padx = 5,
                command = on_scissors_button
                )
rock_button.place(x = 75, y = 70)
paper_button.place(x = 205, y = 70)
scissors_button.place(x = 335, y = 70)

#show what the player chooses
player_choice_text = Label(master,
                font = ('Times New Roman', 15),
                text = 'Your Choice: '
                )
player_choice_text.place(x = 196, y = 220)

#show what the computer chooses
computer_choice_text = Label(master,
                font = ('Times New Roman', 15),
                text = 'Computer Choice: '
                )
computer_choice_text.place(x = 179, y = 270)

#submit button
submit_button = Button(master,
                font = ('Times New Roman', 15),
                text = 'Submit',
                bg = 'white',
                padx = 5,
                command = submit_process
                )
submit_button.place(x = 210, y = 130)

#game result
result_text = Label(master,
                font = ('Times New Roman', 15),
                text = '',
                padx = 5
                )
result_text.place(x = 155, y = 320)

#reset the game
reset_button = Button(master,
                font = ('Times New Roman', 15),
                text = 'Reset',
                bg = 'white',
                padx = 16,
                command = reset_game
                )
reset_button.place(x = 207, y = 400)

master.mainloop()