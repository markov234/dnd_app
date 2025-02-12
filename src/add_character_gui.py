import tkinter as tk
from tkinter import ttk, messagebox
from character_manager import add_character

class AddCharacterGUI:
    def __init__(self, parent, refresh_callback):
        """Initialize the Add Character window."""
        self.parent = parent
        self.refresh_callback = refresh_callback
        self.window = tk.Toplevel(parent)
        self.window.title("Add New Character")
        self.window.geometry("400x500")

        # Labels & Entry Fields
        fields = ["Name", "Race", "Class", "Background", "Alignment", "Level", 
                  "Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
        
        self.entries = {}
        for idx, field in enumerate(fields):
            ttk.Label(self.window, text=field + ":").grid(row=idx, column=0, padx=10, pady=5, sticky="w")
            entry = ttk.Entry(self.window)
            entry.grid(row=idx, column=1, padx=10, pady=5)
            self.entries[field.lower()] = entry

        # Default values
        self.entries["level"].insert(0, "1")
        for stat in ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]:
            self.entries[stat].insert(0, "10")

        # Submit Button
        ttk.Button(self.window, text="Add Character", command=self.add_character).grid(row=len(fields), column=0, columnspan=2, pady=10)

    def add_character(self):
        """Collect user input and add the character via character_manager.py."""
        try:
            name = self.entries["name"].get()
            race = self.entries["race"].get()
            char_class = self.entries["class"].get()
            background = self.entries["background"].get()
            alignment = self.entries["alignment"].get()
            level = int(self.entries["level"].get() or 1)

            strength = int(self.entries["strength"].get() or 10)
            dexterity = int(self.entries["dexterity"].get() or 10)
            constitution = int(self.entries["constitution"].get() or 10)
            intelligence = int(self.entries["intelligence"].get() or 10)
            wisdom = int(self.entries["wisdom"].get() or 10)
            charisma = int(self.entries["charisma"].get() or 10)

            # Use the character_manager function
            message = add_character(name, race, char_class, background, alignment, level,
                                    strength, dexterity, constitution, intelligence, wisdom, charisma)

            messagebox.showinfo("Success", message)
            self.window.destroy()
            self.refresh_callback()

        except ValueError:
            messagebox.showerror("Error", "Level and ability scores must be numbers.")




