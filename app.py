#to prevent python from generating pyc files
import sys
sys.dont_write_bytecode = True

import customtkinter as ctk
import price_tracker
from PIL import Image

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Crypto Price Search')
        self.geometry(f"{1100}x{580}")

        #grid layout
        self.grid_columnconfigure(1,weight = 1)
        self.grid_rowconfigure(4, weight = 0)
        self.grid_columnconfigure(3, weight = 1)

        #sidebar frame 
        self.sideBarFrame = ctk.CTkFrame(self, width = 250)
        self.sideBarFrame.grid(row = 0, column = 0, rowspan = 2, sticky = 'nsew')
        self.sideBarFrame.grid_rowconfigure(5, weight = 1)
        self.sideBarTitle = ctk.CTkLabel(self.sideBarFrame, text = 'Trending', font = ctk.CTkFont(size = 16, weight = 'bold'), width = 250)
        self.sideBarTitle.grid(row = 0, column = 0, padx = 10, pady = (10, 20))

        #sidebar items (5 trending coins)
        trendingDict = self.getTrending()
        trendingNames = self.getTrendingName(trendingDict)
        trendingPrices = self.getTrendingPrice(trendingDict)
        #trendingImages = self.getTrendingImages(trendingDict)

        self.trendingLabel1 = ctk.CTkLabel(self.sideBarFrame, text = trendingNames[1], compound='left', padx = 10, pady = 10)
        self.priceLabel1 = ctk.CTkLabel(self.sideBarFrame, text = trendingPrices[1], compound = 'right', padx = 10, pady = 10)
        self.trendingLabel2 = ctk.CTkLabel(self.sideBarFrame, text = trendingNames[2], compund = 'left', padx = 10, pady = 10)
        self.priceLabel2 = ctk.CTkLabel(self.sideBarFrame, text = trendingPrices[2], compound = 'right', padx = 10, pady = 10)
        self.trendingLabel3 = ctk.CTkLabel(self.sideBarFrame, text = trendingNames[3], compound = 'left', padx = 10, pady = 10)
        self.priceLabel3 = ctk.CTkLabel(self.sideBarFrame, text = trendingPrices[3], compound = 'right', padx = 10, pady = 10)
        self.trendingLabel4 = ctk.CTkLabel(self.sideBarFrame, text = trendingNames[4], compund = 'left', padx = 10, pady = 10)
        self.priceLabel4 = ctk.CTkLabel(self.sideBarFrame, text = trendingPrices[4], compound = 'right', padx = 10, pady = 10)
        self.trendingLabel5 = ctk.CTkLabel(self.sideBarFrame, text = trendingNames[5], compound = 'left', padx = 10, pady = 10)
        self.priceLabel5 = ctk.CTkLabel(self.sideBarFrame, text = trendingPrices[5], compound = 'right', padx = 10, pady = 10)

        #ids label
        self.idsLabel = ctk.CTkLabel(self, text = 'Search by ID')
        self.idsLabel.grid(row = 1, column = 1, padx = 50, pady = 20, sticky = 'nsew')

        #ids entry 
        self.idsEntry = ctk.CTkEntry(self, placeholder_text = 'Enter the ID of desired curency')
        self.idsEntry.grid(row = 2, column = 1, columnspan = 2, padx = 50, pady = 20, sticky = 'ew')

        #search ids button
        self.idsSearchButton = ctk.CTkButton(self, fg_color = 'black',text = 'Search', command = self.fillDisplayBox)
        self.idsSearchButton.grid(row = 3, column = 1, columnspan = 2, rowspan = 1, padx = 50, pady = 20, sticky = 'ew')

        #get value from entry
        ids = self.idsEntry.get()

        #field for price of currency
        self.displayBox = ctk.CTkTextbox(self, width = 100, height = 50)
        self.displayBox.grid(row = 4, column = 1, columnspan = 2, padx = 50, pady = 20, sticky = 'nsew')


    #pass ids through price_tracker
    def getIds(self):
        text = self.idsEntry.get()
        return text
    
    def getPrice(self, text):
        price = price_tracker.getPrice(text)
        return price

    def fillDisplayBox(self):
        t = self.getIds()
        p = self.getPrice(t)
        self.displayBox.delete('0.0', 'end')
        self.displayBox.insert('0.0', f'${p}')
    """
    def createTrendingItem(self, price, image = None, n):
        trendingDict = self.getTrending
        label = ctk.CTkLabel(self, text = price, image = image, compound = 'left')
        label.grid(row = len(trendingDict), column = 0, padx = 10, pady = 10)
        return label
    """
    def getTrending(self):
        trendingList = price_tracker.getTrending()
        return trendingList
    
    def getTrendingName(self, trendingList):
        nameList = []
        for k, v in trendingList.items():
            nameList.append(k)
        return nameList

    def getTrendingPrice(self, trendingList):
        priceList = []
        for k, v in trendingList.items():
            priceList.append(v['price'])
        return priceList
    """
    def getTrendingImage(self, trendingList):
        imageList = []
        for k, v in trendingList.items():
            imageList.append(list(v.values())[1])
        return imageList
    """


if __name__ == '__main__':
    app = App()
    app.mainloop()
