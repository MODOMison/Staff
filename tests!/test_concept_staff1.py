import tkinter as tk
from main_script import ConceptStaff, UCSD_BLUE

def test_button_text():
    root = tk.Tk()
    app = ConceptStaff(root)
    
    assert app.button_open_websites.cget('text') == 'Target Assignment'







    


        


