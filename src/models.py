from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import sys

# Creates a base class for all ORM (Object Relational Mapping) classes.
# In other words, it creates a base class for all database tables.
# Each table is a different type of object (e.g., Character, Item, etc.).
Base = declarative_base()

# Define the Character class, which becomes a table in the database.
class Character(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    race = Column(String, nullable=False)
    char_class = Column(String, nullable=False)
    background = Column(String, nullable=True)
    alignment = Column(String, nullable=True)
    level = Column(Integer, default=1)

    # Ability Scores
    strength = Column(Integer, default=10)
    dexterity = Column(Integer, default=10)
    constitution = Column(Integer, default=10)
    intelligence = Column(Integer, default=10)
    wisdom = Column(Integer, default=10)
    charisma = Column(Integer, default=10)

    image_path = Column(String, nullable=True)
    notes = Column(Text, nullable=True)

# If want more objects, create more classes like Character.

# Create SQLite database
# This method helps identify the path to the database file, 
# whether running as a script or a compiled app.
def get_database_path():
    """Get the path to dnd_characters.db, compatible with PyInstaller and development."""
    if getattr(sys, 'frozen', False):  # Running as a compiled app
        base_path = sys._MEIPASS  # Temporary folder where PyInstaller unpacks stuff
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, "..", "dnd_characters.db")

DATABASE_URL = f"sqlite:///{get_database_path()}"

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

print("Database initialized!")
