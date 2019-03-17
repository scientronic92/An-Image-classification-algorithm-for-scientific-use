#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 22:16:52 2016

@author: omer
"""

from PIL import Image,ImageFilter
import numpy as np
import matplotlib.pyplot as plt

'''convert RGB image to labcolorspace image'''

from skimage import io,color
B=io.imread('17.jpg')
lab = color.rgb2lab(B)


'''plotting conversion'''

ax2 = plt.subplot2grid((8,6),(4,0),rowspan=4,colspan=3)
#ax2.imshow(lab)

'''segmentation using clustering'''

import cv2 

#img = cv2.imread('10.jpg')
Z = lab.reshape((-1,3))

# convert to np.float32
Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 2
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((lab.shape))

ax2.imshow(res2)
cv2.imshow('res2',res2)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

'''labeling clusters'''


A = np.array(res[label==0])
B = np.array(res[label==1])

#print(A)

#print(A,B,C,D)


''' calculating the probability of each feature (color) '''

a = len(A)
b = len(B)

Pa = a/(len(Z))
Pb = b/(len(Z))



'''now using decision tree to classify an image wether it's a cloud or not'''

if ((A[1]) == 91): 
    
    
    if ((B[1]) == 6):
        
        print('A = cyan')
        print('B = black')
        print('situation1')

elif ((A[1]) == 6):
    
    if ((B[1]) == 91):
        
        print('B = cyan')
        print('A = black')
        print('situation1')
        
###########################################################
       
elif ((A[1]) == 6): 
    
    
    if ((B[1]) == 72)|((B[1]) == 71):
        
        print('B = orange')
        print('A = black')
        print('situation2')

elif ((A[1]) == 72)|((A[1]) == 71):
    
    if ((B[1]) == 6):
        
        print('B = black')
        print('A = orange')
        print('situation2')        
                
############################################################

if ((A[1]) == 61)|((A[1]) == 62): 
    
    
    if ((B[1]) == 29):
        
        print('A = blue')
        print('B = orange')
        print('situation3')

elif ((B[1]) == 61)|((A[1]) == 62):
    
    if ((A[1]) == 29):
        
        print('A = orange')
        print('B = blue')
        print('situation3')

###########################################################

if ((A[1]) == 38): 
    
    
    if ((B[1]) == 40):
        
        print('A = red')
        print('B = blue')
        print('situation1')

elif ((B[1]) == 38):
    
    if ((A[1]) == 40):
        
        print('B = red')
        print('A = blue')
        print('situation4')
        
############################################################

if ((A[1]) == 36): 
    
    
    if ((B[1]) == 42):
        
        print('A = red')
        print('B = green')
        print('situation1')

elif ((B[1]) == 36):
    
    if ((A[1]) == 42):
        
        print('B = red')
        print('A = green')
        print('situation5')
             
 
#print(Pdark,Pcyan,Pwhite,Pblue)
  
