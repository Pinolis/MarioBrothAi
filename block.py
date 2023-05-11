class Block:
    def __init__(self):
        self.img = None
        self.kp = None
        self.des = None
        self.moving = False
        self.matchTreshold = None
        self.perc = False
        
    #sets
    def setImg(self, img):
        self.img = img
        
    def setKp(self, kp):
        self.kp = kp
    
    def setDes(self, des):
        self.des = des
    
    def setIndex(self, index):
        self.index = index
    
    def setMoving(self, moving):
        self.moving = True
        
    def setMatchTreshold(self, matchTreshold):
        self.matchTreshold = matchTreshold
        
    def setPerc(self):
        self.perc = True
    
    #gets
    def getImg(self):
        return self.img
    
    def isMoving(self):
        return self.moving
    
    def isPerc(self):
        return self.perc
    
    def getMatchTreshold(self):
        return self.matchTreshold
    
    def getKp(self):
        return self.kp
    
    def getDes(self):
        return self.des
    
    def getIndex(self):
        return self.index

    
        
    
