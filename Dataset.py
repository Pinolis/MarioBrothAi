import cv2
import os
import block as b


def PopulateDataset(dir) :
    #creo il sift
    sift = cv2.SIFT_create()
    sift.setContrastThreshold(0.0001)
    sift.setNOctaveLayers(20)
    sift.setSigma(3.0)
    dataset={}
    index=0
    #ciclo la directori di assets
    for filename in os.listdir(dir) :
            index+=1
            fullpath = os.path.join(dir, filename)
            img=cv2.imread(fullpath)
            
            #preprocessing per il detect dei keypoints
            upsampled = cv2.resize(img, None, fx=3, fy=3, interpolation=cv2.INTER_LINEAR)
            gray = cv2.cvtColor(upsampled, cv2.COLOR_BGR2GRAY)
            gray_eq= cv2.equalizeHist(gray)      
            equalized = cv2.equalizeHist(gray_eq)
            gray_blur = cv2.GaussianBlur(equalized,(5,5),0)
            thresh = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
            
            #detect
            keypoints, des = sift.detectAndCompute(thresh,None)
            
            #se il file non è nel dizionario aggiungo l'oggetto blocco
            if not(filename in dataset) :
                block= b.Block()
                block.setKp(keypoints)
                block.setDes(des)
                block.setImg(img)
                dataset[filename] = block
    return dataset

def main() :
    
    Dataset=PopulateDataset("assets")
    return Dataset
    
if __name__ == "__main__":
    main()