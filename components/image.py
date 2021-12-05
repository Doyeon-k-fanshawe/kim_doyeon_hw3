#imports always go at the top
from PIL import Image
from components import vars


def total(value):
    # do some logic to see which character you selected

    if value == 30:
        
        spiderMan = Image.open("images/spider.jpg")
        spiderMan.show()
        # add some emoji icons, or show the character image using the Pillow package
    elif value == 20:

        ironMan = Image.open("images/iron.jpg")
        ironMan.show()
        # add some emoji icons, or show the character image using the Pillow package
    elif value == 50:

        natasha = Image.open("images/black_widow.jpg")
        natasha.show()
        # add some emoji icons, or show the character image using the Pillow package
    elif value == 40:

        captain = Image.open("images/cap.jpg")
        captain.show()
        # add some emoji icons, or show the character image using the Pillow package



