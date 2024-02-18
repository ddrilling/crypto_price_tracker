#to prevent python from generating pyc files
import sys
sys.dont_write_bytecode = True

import customtkinter as ctk
import price_tracker
from PIL import Image

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

class TrendingFrame(ctk.CTkFrame): 
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.nameList = []
        self.priceList = []
        self.trendingList = []

    def addItem(self, name, price, rowNum):
        nameLabel = ctk.CTkLabel(self, text = name, compound = 'left', padx = 10, pady = 10)
        nameLabel.grid(row = rowNum, column = 0, pady = (0,10), sticky = 'w')
        priceLabel = ctk.CTkLabel(self, text = price, compound = 'right', padx = 10, pady = 10)
        priceLabel.grid(row = rowNum, column = 1, pady = (0,10), sticky = 'e')

    def deleteItem(self, list, rowNum):
        for label, price in zip(self.nameList, self.priceList):
            label.destroy()
            price.destroy()
            self.nameList.remove(label)
            self.priceList.remove(price)
            return
        
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


class SearchFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.idEntryValue = ''
        self.idEntry = ctk.StringVar()
        displayBox = ctk.StringVar()

    def createLabel(self):
        idLabel = ctk.CTkLabel(self, text = 'Search By ID', font = ctk.CTkFont(size = 14, weight = 'bold'), width = 50)
        idLabel.grid(row = 0, padx = 10, pady = 10, sticky = 'ew')
    
    def createEntryBox(self):
        self.idEntry = ctk.CTkEntry(self, placeholder_text = 'Enter the ID of desired cryptocurrency', height = 25, border_width = 5)
        self.idEntry.grid(row = 1, columnspan = 2, padx = 10, pady = 5, sticky = 'ew')
        

    def getEntry(self):
        idEntryValue = self.idEntry.get()
        return idEntryValue

    def searchButton(self, searchCommand):
        searchButton = ctk.CTkButton(self, fg_color = 'black', text = 'Search', command = searchCommand)
        searchButton.grid(row = 2, columnspan = 2, padx = 20, pady = 5, sticky = 'ew')

    def createDisplayBox(self):
        self.displayBox = ctk.CTkTextbox(self, width = 50, height = 25)
        self.displayBox.grid(row = 3, columnspan = 2, padx = 10, pady = 5, sticky = 'nsew')

    def getPrice(self, id):
        price = price_tracker.getPrice(id)
        return price
    
    def fillDisplayBox(self):
        t = self.getEntry()
        p = self.getPrice(t)
        self.displayBox.delete('0.0', 'end')
        self.displayBox.insert('0.0', f'${p}')

    

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Crypto Price Search')
        self.geometry(f"{1100}x{580}")

        #grid layout
        self.grid_columnconfigure(2, weight = 1)
        self.grid_rowconfigure(4, weight = 1)

        #sidebar for trending coins
        self.trendingItemsFrame = TrendingFrame(master = self, width = 250)
        self.trendingItemsFrame.grid(row = 0, column = 0, rowspan = 2, sticky = 'nsew')
        self.trendingItemsFrame.grid_columnconfigure(2, weight = 1)
        self.trendingItemsFrame.grid_rowconfigure(10, weight = 1)
        self.sideBarTitle = ctk.CTkLabel(self.trendingItemsFrame, text = 'Trending', font = ctk.CTkFont(size = 16, weight = 'bold'), width = 250)
        self.sideBarTitle.grid(row = 0, column = 0, padx = 10, pady = (10, 20))

        #trending items variables
        self.trendingItemsFrame.trendingList = self.trendingItemsFrame.getTrending()
        trendingList = self.trendingItemsFrame.trendingList
        self.trendingItemsFrame.nameList = self.trendingItemsFrame.getTrendingName(trendingList)
        nameList = self.trendingItemsFrame.nameList
        self.trendingItemsFrame.priceList = self.trendingItemsFrame.getTrendingPrice(trendingList)
        priceList = self.trendingItemsFrame.priceList

        #create trending items
        for i in range(0, 10):
            self.trendingItemsFrame.addItem(nameList[i], priceList[i], i + 1)

        #create search frame 
        self.searchFrame = SearchFrame(master = self, width = 250)
        self.searchFrame.grid(row = 0, column = 1, columnspan = 2, rowspan = 2, sticky = 'nsew')
        self.searchFrame.grid_columnconfigure(0, weight = 1)
        self.searchFrame.grid_rowconfigure(4, weight = 1)

        #id label
        self.searchFrame.createLabel()
        
        #entry box
        self.searchFrame.createEntryBox()

        #search Button
        self.searchFrame.searchButton(self.searchFrame.fillDisplayBox)

        #display box
        self.searchFrame.createDisplayBox()

    
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
