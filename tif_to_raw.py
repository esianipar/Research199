from osgeo import gdal
import numpy as np


#V.1.2
#TIF to RAW is a script that extracts the raw data within a TIF or TIFF file
#   and outputs it as a 2D numpy array. The values output correlate to stored
#   variable within the .TIF file, and this can be verified using ArcGIS.
#   This will only output the raw data, so for example if you have a temperature
#   in K, then it will not output the K to denote temperature of type Kelvin.






# Prints Directions and Gets an input
print("Booting up .TIF to Raw...\n")
print("Make sure .TIF/.TIFF file is located in the same directory as this script.")
print("Please Specify the File You Wish to Convert (ex: Image.TIF): ")
fileName = input()




ds = gdal.Open(fileName)


# loop through each band
for bi in range(ds.RasterCount):
    band = ds.GetRasterBand(bi + 1)
    
    # Read this band into a 2D NumPy array
    bArr = band.ReadAsArray()
    print('Band %d has type %s'%(bi + 1, np.dtype))


#prints bArr array
for item in bArr:
    print(item)
