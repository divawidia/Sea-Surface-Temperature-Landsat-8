from osgeo import gdal
# from pyproj import Proj
# from sklearn.cluster import KMeans
import os
import numpy as np

# from osgeo import gdal,ogr, osr
# from osgeo.gdalconst import GA_ReadOnly
from osgeo import gdal, ogr, osr
from osgeo.gdalconst import GA_ReadOnly

import matplotlib.pyplot as plt

from PIL import Image
from numpy import asarray
# import rasterio

class suhu:
    TAG = "suhu_laut.class"
    imagePath_b10_2020 = ""
    image_b10_2020 = None

    imagePath_b10_2021 = ""
    image_b10_2021 = None

    #Check Image File
    def openImage_b10_2020(self, path):
        print(self.TAG, "File Image Path : ", path)
        openImage = gdal.Open(path, gdal.GA_ReadOnly)
        if not openImage:
            print(self.TAG, "Type : Not Image File")
            return False
        else:
            print(self.TAG, "Type : Image File")
            self.imagePath_b10_2020 = path
            self.image_b10_2020 = openImage
            return True

    #Check Image File
    def openImage_b10_2021(self, path):
        print(self.TAG, "File Image Path : ", path)
        openImage = gdal.Open(path, gdal.GA_ReadOnly)
        if not openImage:
            print(self.TAG, "Type : Not Image File")
            return False
        else:
            print(self.TAG, "Type : Image File")
            self.imagePath_b10_2021 = path
            self.image_b10_2021 = openImage
            return True
    
    def clip_b10_2020(self, path):
        print(self.TAG, "File Shape Path : ", path)
        band10Clip_2020 = gdal.Warp("band10CLIP_2020.tif", self.image_b10_2020, cutlineDSName = path, cropToCutline = True, dstNodata = np.nan)
        self.arrayClippedBand2020 = band10Clip_2020.GetRasterBand(1).ReadAsArray()

        plt.imshow(self.arrayClippedBand2020[3000:6800, 0:3700])
        plt.savefig("band10CLIP_2020.png",bbox_inches="tight")
        plt.show()

        image = Image.open("band10CLIP_2020.png")

        return image

    def clip_b10_2021(self, path):
        print(self.TAG, "File Shape Path : ", path)
        band10Clip_2021 = gdal.Warp("band10CLIP_2021.tif", self.image_b10_2021, cutlineDSName = path, cropToCutline = True, dstNodata = np.nan)
        self.arrayClippedBand2021 = band10Clip_2021.GetRasterBand(1).ReadAsArray()

        plt.imshow(self.arrayClippedBand2021[3000:6800, 0:3700])
        plt.savefig("band10CLIP_2021.png",bbox_inches="tight")
        plt.show()

        image = Image.open("band10CLIP_2021.png")

        return image

    def mulai_TOA_2020(self):

        self.TOA_Rad_b10_2020 = self.arrayClippedBand2020 * 0.0003342 + 0.1

        plt.imshow(self.TOA_Rad_b10_2020[3800:4800, 0:1000], cmap='jet', vmin=8.50, vmax=9.40)
        plt.colorbar()
        plt.savefig("TOA2020.png",bbox_inches="tight")
        plt.show()

        image = Image.open("TOA2020.png")

        return image
    
    def mulai_BT_2020(self):
        self.band10_sat_temp_2020 = 1321.0789 / np.log(774.8853 / self.TOA_Rad_b10_2020 + 1) - 273.15

        plt.imshow(self.band10_sat_temp_2020[3800:4800, 0:1000], cmap='jet', vmin=18.4, vmax=25.6)
        plt.colorbar()
        plt.savefig("BT2020.png",bbox_inches="tight")
        plt.show()

        image = Image.open("BT2020.png")

        return image

    def mulai_TOA_2021(self):

        self.TOA_Rad_b10_2021 = self.arrayClippedBand2021 * 0.0003342 + 0.1

        plt.imshow(self.TOA_Rad_b10_2021[3800:4800, 0:1000], cmap='jet', vmin=8.80, vmax=9.44)
        plt.colorbar()
        plt.savefig("TOA2021.png",bbox_inches="tight")
        plt.show()

        image = Image.open("TOA2021.png")

        return image
    
    def mulai_BT_2021(self):
        self.band10_sat_temp_2021 = 1321.0789 / np.log(774.8853 / self.TOA_Rad_b10_2021 + 1) - 273.15

        plt.imshow(self.band10_sat_temp_2021[3800:4800, 0:1000], cmap='jet', vmin=21.2, vmax=25.6)
        plt.colorbar()
        plt.savefig("BT2021.png",bbox_inches="tight")
        plt.show()

        image = Image.open("BT2021.png")

        return image
    

    def mulai_SST_2020(self):
        self.band10_sst_2020 = -0.0197*self.band10_sat_temp_2020**2 + 0.2881*self.band10_sat_temp_2020 + 29.004

        plt.imshow(self.band10_sst_2020[3800:4800, 0:1000], cmap='jet', vmin=23.6, vmax=27.6)
        plt.colorbar()
        plt.title('Suhu Permukaan Laut Selat Bali\nTahun 2020\n dalam Celcius')
        plt.xlabel('Column #')
        plt.ylabel('Row #')
        plt.savefig("SST2020.png",bbox_inches="tight")
        plt.show()

        image = Image.open("SST2020.png")

        return image

    def mulai_SST_2021(self):
        self.band10_sst_2021 = -0.0197*self.band10_sat_temp_2021**2 + 0.2881*self.band10_sat_temp_2021 + 29.004

        plt.imshow(self.band10_sst_2021[3800:4800, 0:1000], cmap='jet', vmin=23.354, vmax= 26.38)
        plt.colorbar()
        plt.title('Suhu Permukaan Laut Selat Bali\nTahun 2021\n dalam Celcius')
        plt.xlabel('Column #')
        plt.ylabel('Row #')
        plt.savefig("SST2021.png",bbox_inches="tight")
        plt.show()

        image = Image.open("SST2021.png")

        return image
        