import tkinter as tk
from main_script import ConceptStaff, UCSD_BLUE

def test_button_color():
    root = tk.Tk()
    app = ConceptStaff(root)

    assert app.button_open_websites.cget('bg') == UCSD_BLUE
