import Dataset as D
from block import *
import reader as R
import cv2
from Map import *

dataset=D.PopulateDataset("assets")
dataset['goombaE'].setMoving()
dataset['koopaE'].setMoving()
dataset['big_mario_headM'].setMoving()
dataset['small_marioM'].setMoving()

dataset['mushroomP'].setMoving()
dataset['mushroomP'].setPerc()

dataset['starP'].setMoving()
dataset['starP'].setPerc()

#TRESHOLdS
dataset['big_mario_baseM'].setMatchTreshold(0.7)
dataset['big_mario_headM'].setMatchTreshold(0.8)
dataset['blockO'].setMatchTreshold(0.5)
dataset['brickO'].setMatchTreshold(0.6)
dataset['brick(2)O'].setMatchTreshold(0.7)
dataset['flag_pole_topO'].setMatchTreshold(0.88)
dataset['goombaE'].setMatchTreshold(0.45)
dataset['koopa_ShellE'].setMatchTreshold(0.66)
dataset['koopaE'].setMatchTreshold(0.88)
dataset['mushroomP'].setMatchTreshold(0.55)
dataset['platformO'].setMatchTreshold(0.66)
dataset['pressed_blockO'].setMatchTreshold(0.4)
dataset['question_block_brownO'].setMatchTreshold(0.44)
dataset['question_block_brown(2)O'].setMatchTreshold(0.76)
dataset['question_block_yellowO'].setMatchTreshold(0.87)
dataset['small_marioM'].setMatchTreshold(0.76)
dataset['starP'].setMatchTreshold(0.67)
dataset['tube_body_RO'].setMatchTreshold(0.89)
dataset['tube_top_RO'].setMatchTreshold(0.24)
#manca il fiore

###########TEST ZONE#############
# define the number of rows and columns in the grid
rowsTot = 15 #15 prima
colTot = 16
heigth = 240
width = 256

rowOffset = 2


frame = cv2.imread("testFrame.png")
cellList=R.cellListMaker(frame, width, heigth)
startMatrix=[['B' for j in range(colTot)] for i in range(rowsTot)] #scambio rowstot con coltot
matrix=R.MatrixMaker(startMatrix, cellList, dataset)

print(matrix)
map= Map(width,heigth-rowOffset*16,16)

map.setMapping(matrix)
map.displayImg()

#saveCellList(cellList, "cells")


###########TEST ZONE#############


'''
#VIdEO CAPTURE

# Create a named window for the game
cv2.namedWindow("Game Window", cv2.WINdOW_NORMAL)

# Set the size and position of the OpenCV window
topX, topY, w, h = win32gui.GetWindowRect(win32gui.FindWindow(None, "Super Mario Bros"))
newWidth, newHeight = 236, 24
cv2.moveWindow("Game Window", topX, topY)
cv2.resizeWindow("Game Window", newWidth, newHeight)

cellWidth = newWidth / colTot
cellHeight = newHeight / rowsTot
# Loop through the game frames
while True:
    # Capture the game window using OpenCV
    frame = cv2.cvtColor(np.array(ImageGrab.grab(bbox=(topX, topY, topX+newWidth, topY+newHeight))), cv2.COLOR_RGB2BGR)

    # display the captured frame in the OpenCV window
    cv2.imshow("Game Window", frame)
    cellList=CellListMaker(frame, newHeight, newWidth)
    

    # Wait for a key event for 1 millisecond
    key = cv2.waitKey(1)

    # If the 'q' key is pressed, break out of the loop
    if key == ord("q"):
        break

# Release the video capture object and destroy the OpenCV windows
cv2.destroyAllWindows()
'''


