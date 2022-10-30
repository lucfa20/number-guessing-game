import random, keyboard
from colorama import Fore
from Fancy_stuff import typingPrint, typingInput, clearScreen

def detect():
    keyboard.read_key()


showAns = False
h_num = 10

while True:
    num = random.randint(0, h_num)
    input("\npress enter to play")
    clearScreen()
    if showAns == True:
        print(num)
    player_guess = typingInput(f"{Fore.BLUE}Enter you guess 0-{h_num}:{Fore.RESET} ")
    if player_guess == 'activate cheet':
        showAns = True
        clearScreen()
        print(num)
        player_guess = typingInput(f"{Fore.BLUE}Enter you guess 0-{h_num}:{Fore.RESET} ")

    if player_guess == 'deactivate cheet':
        showAns = False
        clearScreen()
        player_guess = typingInput(f"{Fore.BLUE}Enter you guess 0-{h_num}:{Fore.RESET} ")

    player_guess = int(player_guess)

    if player_guess == num:
        typingPrint(f"{Fore.GREEN}\nCorrect it was {num}{Fore.RESET}", 0.05)
        detect()
    
    elif player_guess != num and player_guess <= num:
        typingPrint(f"{Fore.RED}\nWrong it was {num}{Fore.RESET}",0.05)
        detect()

    else:
        typingPrint(f"You need a number in the range of 0-{h_num}")
        detect()

