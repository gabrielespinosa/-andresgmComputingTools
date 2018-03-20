#!/usr/bin/env python ## #!/usr/local/bin/ python

#20180319: GAEB(Gabriel Andrés Espinosa Barrios) Returning/re-entry Engineering PhD Graduate Student. University of the Andes(Universidad de los Andes). Cod:200311728 Id:110279864X. Bogota(Bogotá) D.C., Colombia. Local, Home, Town: Sincelejo, Sucre, Colombia.
#20180316: GAEB(Gabriel Andres Espinosa Barrios) ID:110279864X, Sincelejo, Sucre, Colombia. University of los Andes(Universidad de los Andes). Code:200311728
#20180315: Gabe Espinosa codes for Python
#email:gabrielespinosa@gmail.com ; g-espino@uniandes.edu.co
#Ph.D. Student. Returning/re-entry.
#University of los Andes (Universidad de los Andes). Bogota D.C., Colombia.

#20180319: Uploading the Python Fourier Transforms Answers Results
"""
Fourd WorkShop - Taller 04. Computing Tools(Herramientas Computacionales) - Uniandes. 
Student:
Gabriel Andrés Espinosa Barrios    
"""
#20180319: Answers Fourth WorkShop - Taller04

#import fucton alphabetic order
import cv2
from glob import glob
import matplotlib.pyplot as plt
from matplotlib import rc, rcParams
import matplotlib.ticker as tick
import numpy as np
import os
import pickle
import random
from scipy import misc
import scipy.io as sio
from skimage.data import coins, coffee, astronaut, clock, horse
import skimage
from skimage import img_as_ubyte
from skimage import transform
import tarfile
import time



def FourierSeries():
    """
    Initial test of Fourier Series 
    """
    
    return FSeries

FourierSeries()
def FourierTrasnforms():
    """
    Basic Main Fourier Transforms 
    """	
    
    return FTransforms     

FourierTrasnforms()

def TaylorSeries():
    """
    Aditional Join with Taylor's series 
    """
TaylorSeries()
                    
#Filters
filtered_img = skimage.filters.gaussian(Andres, sigma=2, multichannel=True)
AndresO = img_as_ubyte(Andres)
AndresF = img_as_ubyte(filtered_img)
AntonioO = img_as_ubyte(Antonio)
AntonioF = skimage.filters.gaussian(AntonioO, sigma=5, multichannel=True)
AntonioF = img_as_ubyte(AntonioF)
newImage = cv2.subtract(AndresO,AndresF)
newImage = cv2.cvtColor(newImage, cv2.COLOR_RGB2GRAY)

resul[:,:,0] = resul[:,:,0]+newImage
resul[:,:,1] = resul[:,:,1]+newImage
resul[:,:,2] = resul[:,:,2]+newImage
#resul[0] = cv2.add(newImage, AntonioF[0])
#resul[1] = cv2.add(newImage, AntonioF[1])
#resul[2] = cv2.add(newImage, AntonioF[2])
plt.subplot(221)
plt.imshow(filtered_img)
plt.subplot(222)
plt.imshow(AntonioO)
plt.subplot(223)
plt.imshow(newImage)
plt.subplot(224)
plt.imshow(result)
