import numpy as np
import cv2 as cv
import math


def distance(xa,ya):
    return math.pow((math.pow(xa,2) + math.pow(ya,2)),0.5)
def nearest_point(max_index,pointSet,type,align):
    next_max = next_min = pointSet[0][0]
    next_max_index=next_min_index =0
    iteration = 0 
    if type is 'max':
        for x in pointSet:
            if iteration is not max_index:
                
                if x[align] > next_max:
                    next_max_index = iteration
                    next_max = x[align]
                
            iteration+=1
        return next_max_index
        
        
    
    elif type is 'min':
        for x in pointSet:
            if iteration is not x_min_index:
            
                if x[align] < next_min:
                    next_min_index = iteration
                    next_min = x[align]
        
            iteration +=1
        return next_min_index

    else:
        return -1
    
img = cv.imread('down.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#edges = cv.Canny(gray, 50, 150, apertureSize=3)
corner = cv.goodFeaturesToTrack(gray, 9, 0.009, 10)
corners = np.int0(corner)
pointSet =[]     
for i in corners:
    x, y = i.ravel()
    pointSet.append((x,y))
    cv.circle(img, (x, y), 6, [255, 0, 255], 4)
cv.imshow('Direction', img)
cv.waitKey(0)
cv.destroyAllWindows()

#finding four crucia point
x_max = x_min= pointSet[0][0]
y_min = y_max= pointSet[0][1]
x_max_index=y_max_index =x_min_index =y_min_index =iteration=  0
for i in pointSet:
    
    if i[0] > x_max:
        x_max_index = iteration
        x_max= i[0]
    if i[0]<x_min:
        x_min_index = iteration
        x_min= i[0]

    if i[1] > y_max:
        y_max_index = iteration
        y_max = i[1]
    if i[1]<y_min:
        y_min_index = iteration
        y_min = i[1]
    iteration = iteration+1

#decide vertical or horizontal arrow
a = abs(pointSet[x_min_index][1] - pointSet[x_max_index][1])
b = abs(pointSet[y_min_index][0] - pointSet[y_max_index][0])

if a > b :
    next_x_max_index = nearest_point(x_max_index,pointSet,'max',0)
    next_x_min_index = nearest_point(x_min_index,pointSet,'min',0)
    a = abs(pointSet[x_max_index][0] - pointSet[next_x_max_index][0])
    b = abs(pointSet[x_min_index][0] - pointSet[next_x_min_index][0])
    
    #determinig right or left
    if a > b : 
        print("right")
    else :
        print("left")     
else:
    next_y_max_index = nearest_point(y_max_index,pointSet,'max',1)
    next_y_min_index = nearest_point(y_min_index,pointSet,'min',1)
    a = abs(pointSet[y_max_index][1] - pointSet[next_y_max_index][1])
    b = abs(pointSet[y_min_index][1] - pointSet[next_y_min_index][1])
    
    #determing up or down
    if a > b : 
        print("down")
    else :
        print("up")     
    