import tkinter as tk
from main_script import ConceptStaff, UCSD_BLUE

def test_label_text():
    root = tk.Tk()
    app = ConceptStaff(root)

    label_text = app.label.cget("text")

    assert label_text == "Ready"
