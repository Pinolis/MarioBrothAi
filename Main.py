import Dataset
from Block import *

Dataset=Dataset.PopulateDataset("assets")
Dataset['goombaE'].setMoving()
Dataset['koopaE'].setMoving()
Dataset['big_mario_headM'].setMoving()
Dataset['small_marioM'].setMoving()

Dataset['mushroomP'].setMoving()
Dataset['mushroomP'].setPerc()

Dataset['starP'].setMoving()
Dataset['starP'].setPerc()

#TRESHOLDS
Dataset['big_mario_baseM'].setMatchTreshold(5)
Dataset['big_mario_headM'].setMatchTreshold(5)
Dataset['blockO'].setMatchTreshold(5)
Dataset['brickO'].setMatchTreshold(5)
Dataset['brick(2)O'].setMatchTreshold(5)
Dataset['flag_pole_topO'].setMatchTreshold(5)
Dataset['goombaE'].setMatchTreshold(5)
Dataset['koopa_shellE'].setMatchTreshold(5)
Dataset['koopaE'].setMatchTreshold(5)
Dataset['mushroomP'].setMatchTreshold(5)
Dataset['platformO'].setMatchTreshold(5)
Dataset['pressed_blockO'].setMatchTreshold(5)
Dataset['pressed_block_brownO'].setMatchTreshold(5)
Dataset['pressed_block_brown(2)O'].setMatchTreshold(5)
Dataset['pressed_block_yellowO'].setMatchTreshold(5)
Dataset['small_marioM'].setMatchTreshold(5)
Dataset['starP'].setMatchTreshold(5)
Dataset['tube_body_RO'].setMatchTreshold(5)
Dataset['tube_top_RO'].setMatchTreshold(5)
#manca il fiore


'''
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
    cellList=CellListMaker(frame, newHeight, newWidth)
    

    # Wait for a key event for 1 millisecond
    key = cv2.waitKey(1)

    # If the 'q' key is pressed, break out of the loop
    if key == ord("q"):
        break

# Release the video capture object and destroy the OpenCV windows
cv2.destroyAllWindows()
'''


