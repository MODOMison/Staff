import os
import tkinter as tk
from tkinter import messagebox
import ctypes

# Define UCSD colors
UCSD_BLUE = "#00539C"  # Blue
UCSD_GOLD = "#FFB71B"   # Gold


class ConceptStaff:
    """
    This class is a "Staff item" managments system

    """
    def __init__(self, root):
        """ initialization, make buttons, load art, prep web list

        Parameters
        ----------
        root: str
            the root directory of tkinter
            the root of the app.

        Returns
        -------
            new object

        """
        self.root = root
        self.root.title("Concept Staff")#name pannel 
        
        # Set UCSD colors for buttons
        self.button_bg_color = UCSD_BLUE
        self.button_fg_color = "white"

        # Load digital art image
        self.digital_art_img = tk.PhotoImage(file="Triton (54).png")  # Replace "triton NFT 54.png" with your image file
        
        # Create and pack background label
        self.background_label = tk.Label(self.root, image=self.digital_art_img)
        self.background_label.place(relwidth=1, relheight=1)

        # Set the size of the panel
        self.root.geometry("300x300")

        # List of websites for "Target Assignment"
        self.websites = [
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

        # Create and pack widgets
        self.label = tk.Label(self.root, text="Ready", bg=UCSD_GOLD, font=("Arial", 13)) #basically a alert says ready to use
        self.label.place(relx=0.96, rely=0.05, anchor='ne')  # Adjusted placement

        #this button does the web app 
        self.button_open_websites = tk.Button(self.root, text="Target Assignment", command=self.open_websites, \
                                              bg=self.button_bg_color, fg=self.button_fg_color, font=("Comfortaa", 9)) #font
        self.button_open_websites.place(relx=0.61, rely=0.2)  # Adjusted placement

        #this button sets the websites
        self.button_atune_staff = tk.Button(self.root, text="Atune Staff", command=self.atune_staff, \
                                            bg=self.button_bg_color, fg=self.button_fg_color, font=("Comfortaa", 9))#font
        self.button_atune_staff.place(relx=0.762, rely=0.35)  # Adjusted placement
        
        #this button cause access to god pannel
        self.button_create_god_mode = tk.Button(self.root, text="Create God Mode", command=self.create_god_mode_panel, \
                                                bg=self.button_bg_color, fg=self.button_fg_color, font=("Comfortaa", 9))#font
        self.button_create_god_mode.place(relx=0.633, rely=0.5)  # Adjusted placement
        
        #this button created hidden zone
        self.button_create_hidden_zone = tk.Button(self.root, text="Create Hidden Zone", command=self.create_hidden_zone, \
                                                   bg=self.button_bg_color, fg=self.button_fg_color, font=("Comfortaa", 9))#font
        self.button_create_hidden_zone.place(relx=0.585, rely=0.65)  # Adjusted placement

        #this button allows the quit
        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.quit, \
                                     bg=self.button_bg_color, fg=self.button_fg_color, font=("Comfortaa", 9)) #font
        self.quit_button.place(relx=0.88, rely=0.8)  # Adjusted placement

    def open_websites(self):
        """
        what is happening: changes the pannel to new status
                begins the next step by call open_in_browser
                this function is intended to be called by a button and loops through all the website 
                to open each of them

        parameters
        ----------
            self

        returns
        -------
            none
        

        """
        self.label.config(text="Opening websites...") #more labeling
        self.root.update()  # Force update to show changes
        
        for website in self.websites:
            self.open_in_browser(website)
            
        
        self.label.config(text="Ready")  # Update label text

    def open_in_browser(self, url):
        """ 
        what is happening: opens web pannel and put the url, activate url

        parameters
        ----------
            self
            the url 

        returns
        -------
            none

        """
        
        try:
            import webbrowser
            webbrowser.open(url)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def atune_staff(self):
        """ 
        what is happening: make new pannel to add or remove the websites

        parameters
        ----------
            self

        returns
        -------
            none
         
        """
        # Create a new window for managing websites
        self.website_window = tk.Toplevel(self.root)
        self.website_window.title("Atune Staff")
        self.website_window.geometry("300x200")

        # Widgets for managing websites
        self.label_website = tk.Label(self.website_window, text="Enter Website URL:", font=("Arial", 10))
        self.label_website.pack()

        self.entry_new_website = tk.Entry(self.website_window, width=30)
        self.entry_new_website.pack()

        self.button_add_website = tk.Button(self.website_window, text="Add Site", \
                                            command=self.add_website, bg=self.button_bg_color, fg=self.button_fg_color, font=("Comfortaa", 9))
        self.button_add_website.pack()

        self.button_remove_website = tk.Button(self.website_window, text="Remove Site", \
                                               command=self.remove_website, bg=self.button_bg_color, fg=self.button_fg_color, font=("Comfortaa", 9))
        self.button_remove_website.pack()

    def add_website(self):
        """ 
        what is happening: add a new website

        parameters
        ----------
            self

        returns
        -------
            none
        
        """
        new_website = self.entry_new_website.get().strip()
        if new_website:
            self.entry_new_website.delete(0, tk.END)
            self.label.config(text=f"Adding website: {new_website}")
            self.root.update()
            # Add the website to the list for "Target Assignment"
            self.websites.append(new_website)
            messagebox.showinfo("Success", "Website added successfully!")
        else:
            messagebox.showwarning("Warning", "Please enter a valid website URL.")

    def remove_website(self):
        """ 
        what is happening: remove a website

        parameters
        ----------
            self

        returns
        -------
            none
        
        """
        # Remove the selected website from the list for "Target Assignment"
        selected_website = self.entry_new_website.get().strip()
        if selected_website:
            if selected_website in self.websites:
                self.websites.remove(selected_website)
                messagebox.showinfo("Success", "Website removed successfully!")
            else:
                messagebox.showwarning("Warning", "Website not found in the list.")
        else:
            messagebox.showwarning("Warning", "Please enter a valid website URL to remove.")

    def create_god_mode_panel(self):
        """ 
        what is happening: access the dormant control pannel

        parameters
        ----------
            self

        returns
        -------
            none
        
        """
        try:
            desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
            god_mode_path = os.path.join(desktop_path, "GodMode.{ED7BA470-8E54-465E-825C-99712043E01C}")
            
            if not os.path.exists(god_mode_path):
                os.makedirs(god_mode_path)
                messagebox.showinfo("Success", "God Mode panel created successfully on Desktop!")
            else:
                messagebox.showwarning("Warning", "God Mode panel already exists on Desktop!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def create_hidden_zone(self):
        """  
        what is happening: create a hidden directory in the desktop folder

        parameters
        ----------
            self

        returns
        -------
            none
        

        """
        try:
            desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
            hidden_zone_path = os.path.join(desktop_path, "\u200B")  # Zero-Width Space character
            
            if not os.path.exists(hidden_zone_path):
                os.makedirs(hidden_zone_path)
                # Make directory hidden
                ctypes.windll.kernel32.SetFileAttributesW(hidden_zone_path, 2)
                messagebox.showinfo("Success", "Hidden zone created successfully on Desktop!")
                # Minimize the tkinter window
                self.root.iconify()  # Minimize the tkinter window
            else:
                messagebox.showwarning("Warning", "Hidden zone already exists on Desktop!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

def main():
    root = tk.Tk()
    app = ConceptStaff(root)
    root.mainloop()

if __name__ == "__main__":
    main()
