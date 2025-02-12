from character_manager import edit_character
from list_characters import list_characters  # Reuse the listing function

def edit_character_cli():
    """CLI interface to edit a character."""
    list_characters()
    
    char_id = input("\nEnter the ID of the character to edit (or press Enter to cancel): ")
    if not char_id:
        print("Edit canceled.")
        return

    try:
        char_id = int(char_id)
    except ValueError:
        print("Invalid input. Please enter a numeric ID.")
        return

    # Collect only the fields the user wants to change
    print("\nPress Enter to keep current values.")
    name = input("New name: ") or None
    race = input("New race: ") or None
    char_class = input("New class: ") or None
    background = input("New background: ") or None
    alignment = input("New alignment: ") or None
    level = input("New level: ")
    
    strength = input("New Strength: ")
    dexterity = input("New Dexterity: ")
    constitution = input("New Constitution: ")
    intelligence = input("New Intelligence: ")
    wisdom = input("New Wisdom: ")
    charisma = input("New Charisma: ")

    # Convert numeric fields if provided
    level = int(level) if level else None
    strength = int(strength) if strength else None
    dexterity = int(dexterity) if dexterity else None
    constitution = int(constitution) if constitution else None
    intelligence = int(intelligence) if intelligence else None
    wisdom = int(wisdom) if wisdom else None
    charisma = int(charisma) if charisma else None

    message = edit_character(char_id, name, race, char_class, background, alignment, level,
                             strength, dexterity, constitution, intelligence, wisdom, charisma)
    print(message)

if __name__ == "__main__":
    edit_character_cli()
