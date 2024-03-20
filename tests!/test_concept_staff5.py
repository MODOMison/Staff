import os
import tkinter as tk
import ctypes
from tkinter import messagebox
from main_script import ConceptStaff

def test_concept_staff():
    root = tk.Tk()
    app = ConceptStaff(root)

    # Test creation of hidden zone
    hidden_zone_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', "\u200B")
    try:
        if os.path.exists(hidden_zone_path):
            os.rmdir(hidden_zone_path)

        app.create_hidden_zone()

        assert os.path.exists(hidden_zone_path)
    finally:
        if os.path.exists(hidden_zone_path):
            os.rmdir(hidden_zone_path)

if __name__ == "__main__":
    test_concept_staff()

