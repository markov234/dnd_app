from models import Character, session

def list_characters():
    print("\nStored D&D Characters")
    print("=" * 40)

    # Query all objects of type Character from the database
    characters = session.query(Character).all()

    if not characters:
        print("No characters found.")
        return

    for char in characters:
        print(f"ID: {char.id} | Name: {char.name} | Class: {char.char_class} | Race: {char.race} | Level: {char.level}")
        print(f"  Alignment: {char.alignment}, Background: {char.background}")
        print(f"  STR: {char.strength}, DEX: {char.dexterity}, CON: {char.constitution}, "
              f"INT: {char.intelligence}, WIS: {char.wisdom}, CHA: {char.charisma}")
        print("-" * 40)

if __name__ == "__main__":
    list_characters()
