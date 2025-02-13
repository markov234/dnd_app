import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from character_manager import edit_character
from models import session, Character

class EditCharacterGUI:
    def __init__(self, parent, char_id, refresh_callback):
        """Initialize the Edit Character window."""
        self.parent = parent
        self.char_id = char_id
        self.refresh_callback = refresh_callback
        self.window = tk.Toplevel(parent)
        self.window.title("Edit Character")
        self.window.geometry("400x500")

        # Fetch character details
        character = session.query(Character).filter_by(id=char_id).first()
        if not character:
            messagebox.showerror("Error", "Character not found.")
            self.window.destroy()
            return

        # Labels & Entry Fields
        fields = ["Name", "Race", "Class", "Background", "Alignment", "Level", 
                  "Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
        
        self.entries = {}
        for idx, field in enumerate(fields):
            ttk.Label(self.window, text=field + ":").grid(row=idx, column=0, padx=10, pady=5, sticky="w")
            entry = ttk.Entry(self.window)
            entry.grid(row=idx, column=1, padx=10, pady=5)
            self.entries[field.lower()] = entry

        # Pre-fill fields with existing character data
        self.entries["name"].insert(0, character.name)
        self.entries["race"].insert(0, character.race)
        self.entries["class"].insert(0, character.char_class)
        self.entries["background"].insert(0, character.background or "")
        self.entries["alignment"].insert(0, character.alignment or "")
        self.entries["level"].insert(0, str(character.level))
        
        for stat in ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]:
            self.entries[stat].insert(0, str(getattr(character, stat)))

        # Image Button
        self.image_path = character.image_path
        self.image_label = ttk.Label(self.window, text=f"Current Image: {self.image_path or 'None'}")
        self.image_label.grid(row=len(fields), column=0, columnspan=2, pady=(10, 0))

        self.upload_button = ttk.Button(self.window, text="Change Image", command=self.upload_image)
        self.upload_button.grid(row=len(fields) + 1, column=0, columnspan=2, pady=(0, 10))

        # Submit Button
        # Here, we call the save_changes method from within the EditCharacterGUI class.
        ttk.Button(self.window, text="Save Changes", command=self.save_changes).grid(row=len(fields) + 2, column=0, columnspan=2, pady=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.image_path = file_path
            self.image_label.config(text=f"Current Image: {self.image_path}")
    
    def save_changes(self):
        """Collect user input and update the character in the database."""
        try:
            name = self.entries["name"].get()
            race = self.entries["race"].get()
            char_class = self.entries["class"].get()
            background = self.entries["background"].get()
            alignment = self.entries["alignment"].get()
            level = int(self.entries["level"].get())

            strength = int(self.entries["strength"].get())
            dexterity = int(self.entries["dexterity"].get())
            constitution = int(self.entries["constitution"].get())
            intelligence = int(self.entries["intelligence"].get())
            wisdom = int(self.entries["wisdom"].get())
            charisma = int(self.entries["charisma"].get())

            message = edit_character(self.char_id, name, race, char_class, background, alignment, level,
                                     strength, dexterity, constitution, intelligence, wisdom, charisma, 
                                     image_path=self.image_path)

            messagebox.showinfo("Success", message)
            self.window.destroy()
            self.refresh_callback()

        except ValueError:
            messagebox.showerror("Error", "Level and ability scores must be numbers.")
