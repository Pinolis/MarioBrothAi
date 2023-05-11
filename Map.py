import numpy as np
import cv2 as cv

class Map:

    

    def __init__(self,width,heigth,dim):
        
        self.width = width
        self.heigth = heigth
        self.dim = dim

        self.mapping = None #matrice coi nomi degli oggetto nel mondo                                                     
        self.img = None     #mappa da displayare
        img = np.full((heigth*dim, width*dim, 3), (255,255,255), dtype=np.uint8)  #creo mappa completamente bianca

    
    def setMapping(self,map):
        self.mapping = map
    

    def displayImg():   #displayo la mappa del mondo colorandola opportunamente a seconda dei char in mapping 
        
        cv2.destroyAllWindows()

        for w in range(width):
            for h in range(heigth):

                objectType = (mapping[w][h])[-1]

                match objectType:
                    case "N":
                        img[(w*dim):(w*dim)+dim, (h*dim):(h*dim)+dim] = (255,0,0)

                    case "M": 
                        img[(w*dim):(w*dim)+dim, (h*dim):(h*dim)+dim] = (0,0,255)

                    case "O":
                        img[(w*dim):(w*dim)+dim, (h*dim):(h*dim)+dim] = (0,0,0)

                    case "background":
                        img[(w*dim):(w*dim)+dim, (h*dim):(h*dim)+dim] = (255,255,255)

                
                cv2.imshow('Mappa', img)

                
               


    
    



        
