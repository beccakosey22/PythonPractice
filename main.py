#create function that gives definitions for ten words
def define(word):
    word = word.lower()
    if word == "programming":
        return "the process or activity of writing computer programs."
    elif word == "computer":
        return "an electronic device that processes and stores data"
    elif word == "school":
        return "any institution at which instruction is given in a particular discipline."
    elif word == "IDE":
        return "software for building applications that combines common developer tools into a single graphical user interface"
    elif word == "keyboard":
        return "a panel of keys that operate a computer or typewriter."
    elif word == "teacher":
        return "a person who teaches, especially in schools."
    elif word == "lizard":
        return "a reptile that typically has a long body and tail, four legs, movable eyelids, and a rough, scaly, or spiny skin."
    elif word == "video game":
        return "a game played by electronically manipulating images produced by a computer program on a television screen or other display screen."
    elif word == "chameleon":
        return "a small slow-moving Old World lizard with a prehensile tail, long extensible tongue, protruding eyes that rotate independently, and a highly developed ability to change color."
    elif word == "fish":
        return "a limbless cold-blooded vertebrate animal with gills and fins and living wholly in water."
    else:
        return word + " is not defined in this dictionary"