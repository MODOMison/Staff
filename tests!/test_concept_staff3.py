import tkinter as tk
from main_script import ConceptStaff, UCSD_BLUE

def test_some_stuff():
    root = tk.Tk()
    app = ConceptStaff(root)


    expected_websites = [
        'https://www.blackbox.ai/',
        'https://chat.openai.com/',
        'https://gemini.google.com/',
        'https://poe.com/',
        'https://civitai.com/',
        'https://huggingface.co/',
        'https://github.com/oobabooga/text-generation-webui',
        'https://app.diagrams.net/',
        'https://github.com/AUTOMATIC1111',
        'https://voyant-tools.org/'
        ]
    assert app.websites == expected_websites
