import cv2 as cv
import numpy as np
import sys

sys.setrecursionlimit(10000)


# we will find number of blobs with pixel value 255 in the following image
# blobdetection1.jpeg

# 1. finding binary image 

img = cv.imread('/home/sirabas/Documents/coding/MicrosoftTeams-image (3).png',0)
n,l=img.shape # will be used while iterating 
count = 0


# 1a. blur the image
ksize = (5, 5) # kernel size
img = cv.blur(img, ksize)

# 1b. thresholding the image
# pixels values less or equal to 127 will be set to 0
# pixels values greater than 127 will be set to 255

# 1.b thresholding the image
for i in range (n):
    for j in range (l):
        if (img[i,j]<=127):
            img[i,j]=0
        else:
            img[i,j]=255


# now we will have binary image of the input image
# so we can now find blobs in it
# for blob detection we will be using dfs

# DFS
# we will use recursion
# DFS(x,y):
#     for all neighbours of x,y:
#         if (neighbour is white):
#             DFS(neighbour)

# DFS defined for blob detection
def dfs(i,j):
    img[i,j]=127 # implying that we have visited this pixel
    cv.imshow('image',img)
    cv.waitKey(10)
    if (i-1>=0):
        if(img[i-1,j]==255):
            dfs(i-1,j)
    if (j-1>=0):
        if(img[i,j-1]==255):
            dfs(i,j-1)        
    if (j+1<l):
        if (img[i,j+1]==255):
            dfs(i,j+1)
    if (i+1<n):
        if (img[i+1,j]==255):
            dfs(i+1,j)
    if ((i-1>=0) and (j-1>=0)):
        if (img[i-1,j-1]==255):
            dfs(i-1,j-1)
    if ((i-1>=0) and (j+1<l)):
        if (img[i-1,j+1]==255):
            dfs(i-1,j+1)
    if ((i+1<n) and (j-1>=0)):
        if (img[i+1,j-1]==255):
            dfs(i+1,j-1)
    if ((i+1<n) and (j+1<l)):
        if (img[i+1,j+1]==255):
            dfs(i+1,j+1)

for i in range (n):
    for j in range (l):
        if (img[i,j]==255):
            count=count+1 # to count number of blobs
            dfs(i,j) # this will check all the neighbours of this pixel

print(count)
# correct answer will be count=5 
