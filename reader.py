# -*- coding: utf-8 -*-
# pyton grid opencv2 for image
import cv2
from Cell import Cell
import Dataset as D
import os
import numpy as np

#function that matches block and cell
def blockMatch(blockName, cell, sift, matcher, dataset):
    MIN_MATCH= 5 #parametro variabile
    processed=D.preProcessing(cell.getImg())
    kpCell, desCell = sift.detectAndCompute(processed,None)
    kpBlock, desBlock = dataset[blockName].getKp(), dataset[blockName].getDes()
    #convert the des senno non funziona il matcher
    desCell = desCell.astype(np.float32)
    desBlock = desBlock.astype(np.float32)
    matches = matcher.knnMatch(desCell,desBlock,k=2)
    good_matches = 0
    for m,n in matches:
        if m.distance < 0.05 * n.distance:
            good_matches+=1
    if good_matches >= dataset[blockName].getMatchTreshold():
        return True #nella return della funzione se true, il blocco nell immagine diventa quello passato nella funzione

#function that creates list of cells
def cellListMaker(frame, width, height):
    cellList=[]
    # Iterate over the image in 16x16 blocks
    cellY=-1
    cellX=-1
    for y in range(0, height, 16):
        cellY+=1
        for x in range(0, width, 16):
            #reset index at end of line
            if cellX==16-1:
                cellX=-1
            cellX+=1
            # init the cell with the coordinates and the image
            cell = Cell()
            cell.setX(cellX)
            cell.setY(cellY)
            cell.setImg(frame[y:y+16, x:x+16])
    
            # Add the block to the list
            cellList.append(cell)
    return cellList


def MatrixMaker(oldMatrix, cellList, dataset):
    #create sift and matcher
    sift = cv2.SIFT_create()
    sift.setContrastThreshold(0.0001)
    sift.setNOctaveLayers(20)
    sift.setSigma(3.0)
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING)
    matrix=[]
    matrixrow=[]
    #metch every cell
    for cell in cellList:
        x=cell.getX()
        y=cell.getY()
        #skip scorse ecc
        if y<2:
            continue
        
        oldBlockName = oldMatrix[y][x]
        
        #caso generale di ottimizzazione blocco vecchio ma scartato in caso di background
        if oldBlockName != 'B' and blockMatch(oldBlockName, cell, sift, matcher, dataset):
            matrixrow.append(oldBlockName)
        else:
            blocks=list(dataset.keys())
            i=0
            while i<len(blocks)-1 and not(blockMatch(blocks[i], cell,sift, matcher, dataset)):
                i+=1
            else:
                if i==len(blocks):
                    matrixrow.append('B')
                else:
                    matrixrow.append(blocks[i])

        if x == 15:
            matrix.append(matrixrow)
            matrixrow=[]

'''            
#function for debug purpuse
def saveCellList(cellList, dir):
    for cell in cellList:
        img = cell.getImg()
        x=cell.getX()
        y=cell.getY()
        filename=f"cell[{y}][{x}].png"
        cv2.imwrite(os.path.join(dir, filename), img)
'''

######################################################################




# Load the image
#frame = cv2.imread("testFrame.png")
#cellList=cellListMaker(frame, width, height)
#saveCellList(cellList, "cells")






