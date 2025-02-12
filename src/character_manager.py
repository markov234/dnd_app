from models import Character, session

# These methods are put in this file so I can keep the database interactions separate from the GUI code.
# This way, I can reuse these methods in other parts of the application, such as a command-line interface (CLI).
# This will help if I ever want to add an API or other interfaces to interact with the database in the future.
# character_manager.py is now like the 'single source of truth' for interacting with the database. 
# (for example, add_character.py and add_character_gui.py both use the add_character method from character_manager.py).

def add_character(name, race, char_class, background=None, alignment=None, level=1, 
                  strength=10, dexterity=10, constitution=10, intelligence=10, wisdom=10, charisma=10):
    """Adds a new character to the database."""
    try:
        if not name or not race or not char_class:
            raise ValueError("Name, Race, and Class are required.")

        new_character = Character(
            name=name, race=race, char_class=char_class, background=background,
            alignment=alignment, level=level, strength=strength, dexterity=dexterity,
            constitution=constitution, intelligence=intelligence, wisdom=wisdom, charisma=charisma
        )

        session.add(new_character)
        session.commit()
        return f"Character '{name}' added successfully!"
    except ValueError as e:
        return str(e)


def edit_character(char_id, name=None, race=None, char_class=None, background=None, alignment=None, 
                   level=None, strength=None, dexterity=None, constitution=None, 
                   intelligence=None, wisdom=None, charisma=None):
    """Edits an existing character in the database."""
    character = session.query(Character).filter_by(id=char_id).first()

    if not character:
        return f"No character found with ID {char_id}."

    # Update only the fields that are provided
    if name: character.name = name
    if race: character.race = race
    if char_class: character.char_class = char_class
    if background is not None: character.background = background
    if alignment is not None: character.alignment = alignment
    if level is not None: character.level = level
    if strength is not None: character.strength = strength
    if dexterity is not None: character.dexterity = dexterity
    if constitution is not None: character.constitution = constitution
    if intelligence is not None: character.intelligence = intelligence
    if wisdom is not None: character.wisdom = wisdom
    if charisma is not None: character.charisma = charisma

    session.commit()
    return f"Character '{character.name}' (ID: {char_id}) updated successfully!"


def delete_character(char_id):
    """Deletes a character from the database by ID."""
    character = session.query(Character).filter_by(id=char_id).first()

    if not character:
        return f"No character found with ID {char_id}."

    session.delete(character)
    session.commit()
    return f"Character '{character.name}' (ID: {char_id}) has been deleted."

