# -*- coding: utf-8 -*-
# pyton grid opencv2 for image
import cv2
import dataset  as D
import Cell
import numpy as np
import win32gui
from PIL import ImageGrab

def blockMatch(blockName, cell, orb, matcher):
    MIN_MATCH= 5 #parametro variabile
    kpCell, desCell = orb.detectAndCompute(Cell.getImgCell(cell),None)
    kpBlock, desBlock = D.Dataset[blockName].getKp(), D.Dataset[blockName].getDes()
    matches = matcher.knnMatch(desCell,desBlock,k=2)
    good_matches = 0
    for m,n in matches:
        if m.distance < 0.05 * n.distance:
            good_matches+=1
    if good_matches >= D.Dataset[blockName].getMatchTreshold():
        return True #nella return della funzione se true, il blocco nell immagine diventa quello passato nella funzione
    
def gridFrameMaker(frame,height, width):
    cellList=[]
    cell=Cell.Cell()
    # Iterate over the image in 16x16 blocks
    cellY=0
    cellX=0
    for y in range(0, height, 16):
        cellY+=1
        for x in range(0, width, 16):
            cellX+=1
            # Get the block of 16x16 pixels from the image
            cell.setImg(frame[y:y+16, x:x+16])
            cell.setX(cellX)
            cell.setY(cellY)
            # Add the block to the list
            cellList.append(cell)

# Define the number of rows and columns in the grid
rowsTot = 15
colTot = 16

#VIDEO CAPTURE

# Create a named window for the game
cv2.namedWindow("Game Window", cv2.WINDOW_NORMAL)

# Set the size and position of the OpenCV window
topX, topY, w, h = win32gui.GetWindowRect(win32gui.FindWindow(None, "Super Mario Bros"))
newWidth, newHeight = 256, 24
cv2.moveWindow("Game Window", topX, topY)
cv2.resizeWindow("Game Window", newWidth, newHeight)

cellWidth = newWidth / colTot
cellHeight = newHeight / rowsTot
# Loop through the game frames
while True:
    # Capture the game window using OpenCV
    frame = cv2.cvtColor(np.array(ImageGrab.grab(bbox=(topX, topY, topX+newWidth, topY+newHeight))), cv2.COLOR_RGB2BGR)

    # Display the captured frame in the OpenCV window
    cv2.imshow("Game Window", frame)
    cellList=gridFrameMaker(frame, newHeight, newWidth)
    

    # Wait for a key event for 1 millisecond
    key = cv2.waitKey(1)

    # If the 'q' key is pressed, break out of the loop
    if key == ord("q"):
        break

# Release the video capture object and destroy the OpenCV windows
cv2.destroyAllWindows()

        

