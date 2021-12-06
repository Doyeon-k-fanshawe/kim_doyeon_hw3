#imports always go at the top
from PIL import Image
from components import vars


def total(value):
    # do some logic to see which character you selected

    if value == 200:
        
        spiderMan = Image.open("images/spider.jpg")
        spiderMan.show()
        
    elif value == 300:

        ironMan = Image.open("images/iron.jpg")
        ironMan.show()
        
    elif value == 500:

        natasha = Image.open("images/black_widow.jpg")
        natasha.show()
        
    elif value == 600:

        captain = Image.open("images/cap.jpg")
        captain.show()
        



