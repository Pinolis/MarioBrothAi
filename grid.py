# -*- coding: utf-8 -*-
# pyton grid opencv2 for image
import cv2

def blockMatch(block, cell, orb, matcher):
    MIN_MATCH= 5 #parametro variabile
    kpCell, desCell = orb.detectAndCompute(cell,None)
    kpBlock, desBlock = Dataset.getpreBlockData(block)
    matches = matcher.knnMatch(desCell,desBlock,k=2)
    good_matches = []
    for m,n in matches:
        if m.distance < 0.05 * n.distance:
            good_matches.append(m)
    if len(good_matches) >= MIN_MATCH:
        return True #nella return della funzione se true, il blocco nell immagine diventa quello passato nella funzione
    
    
    
    



source = cv2.imread("testsDir\test.png")
output_dir = 'testsDir\testOut.png'
block = cv2.imread("testsDir\testBlock.png")
    
# Define the number of rows and columns in the grid
rows = 15
col = 16

# Get the dimensions of the image (should be 256x240)
height, width = source.shape[:2]

# Calculate the size of each cell in the grid
cell_width = width // col
cell_height = height // rows
orb=cv2.ORB_create()

# Loop over each cell in the grid and extract its image data
for y in range(rows):
    for x in range(col):
        matched_image=None
        x1 = x * cell_width
        y1 = y * cell_height
        x2 = x1 + cell_width
        y2 = y1 + cell_height
        cell = source[y1:y2, x1:x2]

        # campute keypoints and decscriptors of the two images
        keypoints_cell, des_cell = orb.detectAndCompute(cell, None)
        

        # matching keypoints through knn
        # matches = matcher.match(des_cell, des_block)
        # matched_image= cv2.drawMatches(block,keypoints_block,block,des_block,matches,None)
        
        # while True:
        #     cv2.imshow('block_matching', matched_image)
        #     matched_image = cv2.resize(matched_image,(1500,800) )
        #     if cv2.waitKey(1) & 0xFF == ord('q'):
        #         break
        
        
        
        # Do something with the cell image data, such as saving it to a file
        #cv2.imwrite('cell{}{}.png'.format(x,y), cell)
        

