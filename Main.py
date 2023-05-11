import Dataset as D
from Block import *
import Reader as R
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
dataset['big_mario_baseM'].setMatchTreshold(3)
dataset['big_mario_headM'].setMatchTreshold(3)
dataset['blockO'].setMatchTreshold(3)
dataset['brickO'].setMatchTreshold(3)
dataset['brick(2)O'].setMatchTreshold(3)
dataset['flag_pole_topO'].setMatchTreshold(3)
dataset['goombaE'].setMatchTreshold(3)
dataset['koopa_shellE'].setMatchTreshold(3)
dataset['koopaE'].setMatchTreshold(3)
dataset['mushroomP'].setMatchTreshold(3)
dataset['platformO'].setMatchTreshold(3)
dataset['pressed_blockO'].setMatchTreshold(3)
dataset['question_block_brownO'].setMatchTreshold(3)
dataset['question_block_brown(2)O'].setMatchTreshold(3)
dataset['question_block_yellowO'].setMatchTreshold(3)
dataset['small_marioM'].setMatchTreshold(3)
dataset['starP'].setMatchTreshold(3)
dataset['tube_body_RO'].setMatchTreshold(3)
dataset['tube_top_RO'].setMatchTreshold(3)
#manca il fiore

###########TEST ZONE#############
# define the number of rows and columns in the grid
rowsTot = 15
colTot = 16
heigth = 240
width = 256

frame = cv2.imread("testFrame.png")
cellList=R.cellListMaker(frame, width, heigth)
startMatrix=[['B' for j in range(colTot)] for i in range(rowsTot)]
matrix=R.MatrixMaker(startMatrix, cellList, dataset)
map= Map(width,heigth,16)
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


