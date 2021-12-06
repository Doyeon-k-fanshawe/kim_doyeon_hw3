from components import vars, emo
from colorama import Fore, Back, Style

def total(value):
    # do some logic to see which character you selected

    if value == 500:
        vars.character = vars.characters[2]

        print(Fore.BLACK)
        print(Back.WHITE + "It's " + vars.character + emo.moj3)
        print(Style.RESET_ALL)
        print(emo.moj6)
        
    elif value == 300:
        vars.character = vars.characters[1]

        print(Fore.YELLOW)
        print(Back.RED + "It's " + vars.character + emo.moj4)
        print(Style.RESET_ALL)
        print(emo.moj6)
        
    elif value == 200:
        vars.character = vars.characters[0]

        print(Fore.RED)
        print(Back.BLUE + "It's " + vars.character + emo.moj1)
        print(Style.RESET_ALL)
        print(emo.moj6)
        
    elif value == 600:
        vars.character = vars.characters[3]

        print(Fore.WHITE)
        print(Back.RED + "It's " + vars.character + emo.moj2)
        print(Style.RESET_ALL)
        print(emo.moj6)
        