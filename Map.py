import numpy as np
import cv2 as cv2

class Map:

    

    def __init__(self,width,heigth,dim):
        
        self.width = width
        self.heigth = heigth
        self.dim = dim

        self.mapping = None #matrice coi nomi degli oggetto nel mondo                                                     
        self.img = None     #mappa da displayare
        img = np.full((self.heigth*self.dim, self.width*self.dim, 3), (255,255,255), dtype=np.uint8)  #creo mappa completamente bianca

    
    def setMapping(self,map):
        self.mapping = map
    

    def displayImg(self):   #displayo la mappa del mondo colorandola opportunamente a seconda dei char in mapping 
        
        cv2.destroyAllWindows()

        for w in range(self.width):
            for h in range(self.heigth):

                objectType = (self.mapping[w][h])[-1]

                match objectType:
                    case "E":
                        self.img[(w*self.dim):(w*self.dim)+self.dim, (h*self.dim):(h*self.dim)+self.dim] = (255,0,0)

                    case "M": 
                        self.img[(w*self.dim):(w*self.dim)+self.dim, (h*self.dim):(h*self.dim)+self.dim] = (0,0,255)

                    case "O":
                        self.img[(w*self.dim):(w*self.dim)+self.dim, (h*self.dim):(h*self.dim)+self.dim] = (0,0,0)

                    case "B":
                        self.img[(w*self.dim):(w*self.dim)+self.dim, (h*self.dim):(h*self.dim)+self.dim] = (255,255,255)
                    #da aggiunger caso delle perc(funghi stella fiore)
                
                cv2.imshow('Mappa', self.img)


    
    



        
