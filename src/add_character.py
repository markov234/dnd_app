from character_manager import add_character

def add_character_cli():
    """CLI interface to add a character."""
    name = input("Enter character name: ")
    race = input("Enter race: ")
    char_class = input("Enter class: ")
    background = input("Enter background (optional): ")
    alignment = input("Enter alignment (optional): ")
    level = int(input("Enter level (default 1): ") or 1)

    strength = int(input("Strength (default 10): ") or 10)
    dexterity = int(input("Dexterity (default 10): ") or 10)
    constitution = int(input("Constitution (default 10): ") or 10)
    intelligence = int(input("Intelligence (default 10): ") or 10)
    wisdom = int(input("Wisdom (default 10): ") or 10)
    charisma = int(input("Charisma (default 10): ") or 10)

    message = add_character(name, race, char_class, background, alignment, level,
                            strength, dexterity, constitution, intelligence, wisdom, charisma)
    print(message)

if __name__ == "__main__":
    add_character_cli()

