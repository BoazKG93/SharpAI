import pyvips
import numpy as np

img = pyvips.Image.new_from_file('/u01/rawdata/images/airbus//u01/rawdata/images/airbus/france/DS_PHR1A_201604111052119/3605834101/IMG_PHR1A_PMS_001/IMG_PHR1A_PMS_201604111052119_ORT_3605834101_R2C1.JP2', access='sequential')
print("opened")
img.crop(100,100)
img.resize(0.1)
img.dzsave("test.jpg")