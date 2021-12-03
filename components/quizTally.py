from components import vars


def total(value):
    # do some logic to see which character you selected

    if value == 50:
        vars.character = vars.characters[2]

        print("It's " + vars.character)
        # add some emoji icons, or show the character image using the Pillow package
    elif value == 20:
        vars.character = vars.characters[1]

        print("It's " + vars.character)
        # add some emoji icons, or show the character image using the Pillow package
    elif value == 30:
        vars.character = vars.characters[0]

        print("It's " + vars.character)
        # add some emoji icons, or show the character image using the Pillow package
    elif value == 40:
        vars.character = vars.characters[3]

        print("It's " + vars.character)
        # add some emoji icons, or show the character image using the Pillow package