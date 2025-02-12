from character_manager import delete_character
from list_characters import list_characters

def delete_character_cli():
    """CLI interface to delete a character."""
    list_characters()

    char_id = input("\nEnter the ID of the character to delete (or press Enter to cancel): ")
    if not char_id:
        print("Deletion canceled.")
        return

    try:
        char_id = int(char_id)
    except ValueError:
        print("Invalid input. Please enter a numeric ID.")
        return

    message = delete_character(char_id)
    print(message)

if __name__ == "__main__":
    delete_character_cli()

