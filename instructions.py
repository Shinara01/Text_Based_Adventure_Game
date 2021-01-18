from time import sleep

#Game Instructions
opening = "You awake to find yourself in a room, which by appearance suggests it is part of a grand mansion.\n" \
+ "You may explore the mansion using the compass directions of north, south, east and west.\n" \
+ "The following commands are also available: talk, fight and check bag."

#Time delay printing
def by_letter(text, new_line=True):
    for character in text:
        print(character, end="", flush=True)
        sleep(0.05)
    if new_line == True:
        print()