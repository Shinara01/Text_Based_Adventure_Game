from time import sleep

#Game Instructions
opening = """You awake to find yourself in a room,
which by appearance suggests it is part of a grand mansion.

You may explore the mansion using the compass directions
of north, south, east and west.

The following commands are also available:
talk, fight and check bag."""

#Time delay printing
def by_letter(text):
    for character in text:
        print(character, end="", flush=True)
        sleep(0.05)