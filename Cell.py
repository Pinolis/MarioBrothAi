class Cell:
    def __init__ (self):
        self.x = None
        self.y = None
        self.img = None
    
    #sets
    def setImg(self, img):
        self.img = img

    def setX(self, x):
        self.x=x

    def setY(self, y):
        self.y=y
        
        
    #gets
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getImg(self):
        return self.img

