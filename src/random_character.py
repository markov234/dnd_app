import random
from character_manager import add_character

# Predefined options for character generation
RACES = ["Human", "Elf", "Dwarf", "Halfling", "Dragonborn", "Gnome", "Half-Orc", "Tiefling"]
CLASSES = ["Fighter", "Wizard", "Rogue", "Cleric", "Paladin", "Barbarian", "Ranger", "Bard"]
BACKGROUNDS = ["Noble", "Sage", "Soldier", "Urchin", "Acolyte", "Criminal", "Entertainer", "Guild Artisan"]
ALIGNMENTS = ["Lawful Good", "Neutral Good", "Chaotic Good", 
              "Lawful Neutral", "True Neutral", "Chaotic Neutral",
              "Lawful Evil", "Neutral Evil", "Chaotic Evil"]

# Standard Array for Ability Scores
STANDARD_ARRAY = [15, 14, 13, 12, 10, 8]

def generate_random_character():
    """Generates and adds a random D&D character to the database."""
    name = f"Random-{random.randint(1000, 9999)}"  # Placeholder name
    race = random.choice(RACES)
    char_class = random.choice(CLASSES)
    background = random.choice(BACKGROUNDS)
    alignment = random.choice(ALIGNMENTS)
    level = 1  # Default starting level

    # Assign ability scores in random order
    random.shuffle(STANDARD_ARRAY)
    strength, dexterity, constitution, intelligence, wisdom, charisma = STANDARD_ARRAY

    message = add_character(name, race, char_class, background, alignment, level,
                            strength, dexterity, constitution, intelligence, wisdom, charisma)
    return message

if __name__ == "__main__":
    print(generate_random_character())
