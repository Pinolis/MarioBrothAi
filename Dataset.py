import cv2
import os

Dataset={}

def getBlockData(blockName):
    return Dataset[blockName][0], Dataset[blockName][1]

def getMinMatch(blockName):
    return Dataset[blockName][2]

def PopulateDataset(dir, dataset, orb) :
    for filename in os.listdir(dir) :
            img = cv2.imread(os.path.join(dir, filename), cv2.IMREAD_COLOR)
            keypoints, des = orb.detectAndCompute(img,None)
            if not(dataset.has_key(filename)) :
                matchTreshold=None
                dataset[filename] = (keypoints, des, matchTreshold)
                
    return dataset

def main() :
    orb = cv2.ORB_create()
    Dataset=PopulateDataset("\BlocchiDataset", Dataset, orb)

if __name__ == "__main__":
    main()