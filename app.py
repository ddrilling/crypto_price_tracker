import customtkinter as ctk

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Crypto Price Search')
        self.geometry(f"{600}x{700}")

        self.grid_rowconfigure(3, weight = 0)
        self.grid_columnconfigure(3, weight = 1)

        #ids label
        self.idsLabel = ctk.CTkLabel(self, text = 'IDS')
        self.idsLabel.grid(row = 2, column = 1, padx = 20, pady = 20, sticky = "nsew")

        #ids entry 
        self.idsEntry = ctk.CTkEntry(self, placeholder_text = 'ethereum')
        self.idsEntry.grid(row = 2, column = 2, columnspan = 2, padx = 20, pady = 20, sticky = "nsew")

        #search ids button
        self.idsSearchButton = ctk.CTkButton(self, fg_color = 'black',text = 'Search')
        self.idsSearchButton.grid(row = 3, column = 2, columnspan = 2, rowspan = 1, padx = 10, pady = 20, sticky = "ew")

if __name__ == '__main__':
    app = App()
    app.mainloop()
