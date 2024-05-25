import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("road(1).jpg")
path = r'road(1).jpg'
img2 = cv2.imread(path, cv2.IMREAD_GRAYSCALE) 
#Displaying image using plt.imshow() method
plt.imshow(img)
 
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
 
#Displaying image using plt.imshow() method
plt.imshow(RGB_img)
  
#hold the window
plt.waitforbuttonpress()
plt.close('all')