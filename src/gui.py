import tkinter as tk
from tkinter import ttk, messagebox
from models import Character, session
from PIL import Image, ImageTk
from add_character_gui import AddCharacterGUI
from edit_character_gui import EditCharacterGUI
from character_manager import delete_character
from random_character import generate_random_character
import os

class CharacterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("D&D Character Manager")

        # Frame for character list
        self.frame = ttk.Frame(root, padding=10)
        self.frame.pack(fill="both", expand=True)

        # Title
        self.title_label = ttk.Label(self.frame, text="D&D Character Manager", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=10)

        # Treeview (Table) to Display Characters
        self.tree = ttk.Treeview(self.frame, columns=("ID", "Name", "Class", "Race", "Level", "Image"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Class", text="Class")
        self.tree.heading("Race", text="Race")
        self.tree.heading("Level", text="Level")
        self.tree.heading("Image", text="Image Path")

        self.tree.pack(pady=10, fill="both", expand=True)

        # Character Image Preview
        self.image_label = ttk.Label(self.frame, text="Character Image Preview")
        self.image_label.pack(pady=10)
        self.character_image = ttk.Label(self.frame)
        self.character_image.pack(pady=5)

        # Notes Section Label
        self.notes_label = ttk.Label(self.frame, text="Character Notes")
        self.notes_label.pack(pady=5, padx=10, side=tk.RIGHT)

        # Notes Textbox
        self.notes_text = tk.Text(self.frame, width=40, height=10, wrap="word")
        self.notes_text.pack(pady=5, padx=10, side=tk.RIGHT)

        # Bind the event to detect changes while typing
        self.notes_text.bind("<KeyRelease>", self.save_notes)

        # Buttons
        self.button_frame = ttk.Frame(self.frame)
        self.button_frame.pack(pady=5)

        ttk.Button(self.button_frame, text="Add Character", command=self.add_character).grid(row=0, column=0, padx=5)
        ttk.Button(self.button_frame, text="Edit Character", command=self.edit_character).grid(row=0, column=1, padx=5)
        ttk.Button(self.button_frame, text="Delete Character", command=self.delete_character).grid(row=0, column=2, padx=5)
        ttk.Button(self.button_frame, text="Refresh", command=self.load_characters).grid(row=0, column=3, padx=5)
        ttk.Button(self.button_frame, text= "Generate Random", command=self.generate_random).grid(row=0, column=4, padx=5)

        # Load initial data
        self.load_characters()

        self.tree.bind("<<TreeviewSelect>>", self.on_character_select)


    def load_characters(self):
        """Fetch and display all characters in the table."""
        # Clear existing items
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Fetch characters from database
        characters = session.query(Character).all()
        for char in characters:
            self.tree.insert("", "end", values=(char.id, char.name, char.char_class, char.race, char.level, char.image_path))

    def add_character(self):
        """Open the Add Character GUI window."""
        AddCharacterGUI(self.root, self.load_characters)

    def edit_character(self):
        """Open the Edit Character GUI window for the selected character."""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("No Selection", "Please select a character to edit.")
            return

        char_id = int(self.tree.item(selected, "values")[0])  # Get character ID
        EditCharacterGUI(self.root, char_id, self.load_characters)

    def delete_character(self):
        """Delete the selected character from the main GUI, with confirmation."""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("No Selection", "Please select a character to delete.")
            return

        char_id = int(self.tree.item(selected, "values")[0])  # Get selected character ID
        char_name = self.tree.item(selected, "values")[1]  # Get character name

        confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete '{char_name}'?")
        if confirm:
            message = delete_character(char_id)  # Call delete function
            messagebox.showinfo("Deletion", message)
            self.load_characters()  # Refresh character list

    def generate_random(self):
        """Generate a random character and refresh the list."""
        message = generate_random_character()
        messagebox.showinfo("Random Character", message)
        self.load_characters()  # Refresh the character list

    def on_character_select(self, event):
        """Load and display the selected character's image, or show 'No Image Available'."""
        selected = self.tree.selection()
        if not selected:
            return

        char_id = int(self.tree.item(selected, "values")[0])
        image_path = self.tree.item(selected, "values")[5]

        # Load and display character image
        if image_path and os.path.exists(image_path):
            image = Image.open(image_path)
            image = image.resize((150, 150))
            photo = ImageTk.PhotoImage(image)
            self.character_image.configure(image=photo, text="")
            self.character_image.image = photo
        else:
            self.character_image.configure(image=None, text="No Image Available")

        # Fetch notes from the database
        character = session.query(Character).filter_by(id=char_id).first()
        if character:
            self.notes_text.delete("1.0", tk.END)  # Clear old notes
            self.notes_text.insert("1.0", character.notes or "")  # Insert existing notes
            self.notes_text.config(state=tk.NORMAL)  # Allow editing
            self.current_character_id = char_id  # Store the current character ID for saving

    def save_notes(self, event):
        """Automatically save notes when the user types."""
        if hasattr(self, 'current_character_id') and self.current_character_id:
            new_notes = self.notes_text.get("1.0", tk.END).strip()
            character = session.query(Character).filter_by(id=self.current_character_id).first()
            if character:
                character.notes = new_notes
                session.commit()


if __name__ == "__main__":
    root = tk.Tk()
    app = CharacterApp(root)
    root.mainloop()
