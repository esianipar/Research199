#from osgeo import gdal
import numpy as np
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import *
import pickle
import tifffile
import matplotlib.pyplot as plt

#npy.save()
#write comments in tiff file?
#pil (python image library)


#V.2.0
#TIF to RAW is a script that extracts the raw data within a TIF or TIFF file
#   and outputs it as a 2D numpy array. The values output correlate to stored
#   variable within the .TIF file, and this can be verified using ArcGIS.
#   This will only output the raw data, so for example if you have a temperature
#   in K, then it will not output the K to denote temperature of type Kelvin.

### classes ###
class ArrayList: 
    
    
    
    """ Methods """
    def __init__(self):
        """ Variables """
        #ERA5
        self.temperature2mHash = {}
        self.SkinTemperatureHash = {}
        self.snowfallHash = {}
        self.snowDepthHash = {}
        self.windU10mHash = {}
        self.windV10mHash = {}
        self.surfacePressureHash = {}
        self.totalPrecipitationHash = {}
        self.surfaceLatentHeatFluxHash = {}
        self.surfaceNetSolarRadiationHash = {}
        self.surfaceNetThermalRadiationHash = {}
        #Other
        self.fireHash = {}
        self.droughtHash = {}
        self.extremeWeatherHash = {} 
        self.customHash = {}
        
        #calculation arrays
        self.calculationArray = []

    def get_temperature2mHash(self):
        return self.temperature2mHash

    def get_SkinTemperatureHash(self):
        return self.SkinTemperatureHash

    def get_snowfallHash(self):
        return self.snowfallHash

    def get_snowDepthHash(self):
        return self.snowDepthHash

    def get_windU10mHash(self):
        return self.windU10mHash

    def get_windV10mHash(self):
        return self.windV10mHash

    def get_surfacePressureHash(self):
        return self.get_surfacePressureHash()

    def get_totalPrecipitationHash(self):
        return self.totalPrecipitationHash

    def get_surfaceLatentHeatFluxHash(self):
        return self.surfaceLatentHeatFluxHash

    def get_surfaceNetSolarRadiationHash(self):
        return self.surfaceNetSolarRadiationHash

    def get_surfaceNetThermalRadiationHash(self):
        return self.surfaceNetThermalRadiationHash




    
    def add_array(self, array, option):
        #Adds an array to a chosen hash
        
        #applies options from convert .tif_to_raw
        if option != 1:
            #internal calculation -- no name neccesary
            self.calculationArray.append(array)
        else:
            #user inputs a name to identify array
            newName = input("\nType a name to identify this Array (0 to exit): ")
        
            if(newName == '0'):
                return
            
            varType = 0
            while varType < 1 or varType > 17:
                #user selects a variable to store the array in
                print("\nType of Variable: ")
                print("1:  2m Temperature (2t)")
                print("2:  Skin Temperature (skt)")
                print("3:  Snowfall (sf)")
                print("4:  Snow Depth (snod)")
                print("5:  10m Wind U (10u)")
                print("6:  10m Wind V (10v)")
                print("7:  Surface Pressure (sp)")        
                print("8:  Total Precipitation (tp)")
                print("9:  Surface Latent Heat Flux (slhf)")
                print("10: Surface Net Solar Radiation (ssr)")
                print("11: Surface Net Thermal Radiation (str)")
                print("12: Fire")
                print("13: Drought")
                print("14: Extreme Weather")
                print("15: Custom")
                varType = input("Please Select Which Type of Variable this Array Contains: ")
                varType = int(varType)
            
            if varType == 1:
                self.temperature2mHash[newName] = array
            elif varType == 2:
                self.SkinTemperatureHash[newName] = array
            elif varType == 3:
                self.snowfallHash[newName] = array
            elif varType == 4:
                self.snowDepthHash[newName] = array
            elif varType == 5:
                self.windU10mHash[newName] = array
            elif varType == 6:
                self.windV10mHash[newName] = array
            elif varType == 7:
                self.surfacePressureHash[newName] = array
            elif varType == 8:
                self.totalPrecipitationHash[newName] = array    
            elif varType == 9:
                self.surfaceLatentHeatFluxHash[newName] = array
            elif varType == 10:
                self.surfaceNetSolarRadiationHash[newName] = array
            elif varType == 11:
                self.surfaceNetThermalRadiationHash[newName] = array    
            elif varType == 12:
                self.fireHash[newName] = array
            elif varType == 13:
                self.droughtHash[newName] = array 
            elif varType == 14:
                self.extremeWeatherHash[newName] = array
            elif varType == 15:
                self.customHash[newName] = array
        
        print("\nAdded Succesfully.\n")
    
    def display_arrays(self):
        #Displays all arrays held in hashes
        #ERA5
        print("1: 2m Temperature")
        print(self.temperature2mHash)
        print("2: Skin Temperature")
        print(self.SkinTemperatureHash)
        print("3: Snowfall")
        print(self.snowfallHash)
        print("4: Snow depth")
        print(self.snowDepthHash)
        print("5: 10m Wind U")
        print(self.windU10mHash)
        print("6: 10m Wind V")       
        print(self.windV10mHash)
        print("7: Surface Pressure")
        print(self.surfacePressureHash)
        print("8: Total Precipitation")
        print(self.totalPrecipitationHash)
        print("9: Surface Latent Heat Flux")
        print(self.surfaceLatentHeatFluxHash)
        print("10: Surface Net Solar Radiation")
        print(self.surfaceNetSolarRadiationHash)
        print("11: Surface Net Thermal Radiation")
        print(self.surfaceNetThermalRadiationHash)
        print("12: Fire")
        print(self.fireHash)
        print("13: Drought")
        print(self.droughtHash)
        print("14: Extreme Weather")
        print(self.extremeWeatherHash)
        print("15: Custom")
        print(self.customHash)
        print("16: Internal Calculation")
        print(self.calculationArray)
        
### end classes ###



### functions ###
def prompt_user():
    
    func = -1
    while func < 0 or func > 7:
        #prompts user for input   
        print("\n\n\n\nFunctions: ")
        print("1: Display Arrays")
        print("2: Convert .tif to raw Data")
        print("3: Calculate Mean of Selected Arrays")
        print("4: Calculate Max/Min of Selected Arrays")
        print("5: Save Data")
        print("6: Load Data")
        print("7: Export Data on to Pickle File")
        print("0: Exit Application")
        func = input("Please Select a Function you Wish to Execute: ")
        func = int(func)
        
        #error msg
        if func < 0 or func > 7:
            print("\nPlease input a number within the given range.")
            
        #confirm exit
        if func == 0:
            func = input("\nAre you sure? (type 0 again to confirm): ")
            func = int(func)
            if func != 0:
                func = -1
    
    #provides spacing
    print(" ")    
    return func
    
def switch(selection, arrayListArr):
    
    #assigns arrayList to be the last element of array (loading data)
    arrayList = arrayListArr[-1]
    
    #calls appropriate function based on user input 
    if selection == 1:
        arrayList.display_arrays()
    elif selection == 2:
        tif_to_raw(arrayList, 1)        
    elif selection == 3:
        mean_arrays(arrayList, True)
    elif selection == 4:
        max_min_arrays(arrayList, True)
    elif selection == 5: 
        save_data(arrayList)
    elif selection == 6: 
        arrayListArr.append(load_data())
    elif selection == 7:
        export_data(arrayList)
    
    #allows changes to arrayListArr in main
    return arrayListArr
       
def tif_to_raw(arrayList, option):
    
    if option != 2 and option != 3:
        # Prints directions and Gets an input
        print("\nDo you wish to add the file(s) directly, or preform a calculation?")
        print("1: Add directly")
        print("2: Mean calculation")
        print("3: Min&Max calculation")
        print("0: Exit")
        option = input("Please Select an Option: ")
        option = int(option)
    
        if option == 0:
            return
    
    #open gui to choose file
    Tk().withdraw()
    fileName = askopenfilenames(filetypes=[("Tif files", "*.tif"), ("Tif files", "*.tiff"), ("All Files", "*.*")]) #opens a dialog box and returns path to file(s) ###update###
    
    #ex format ds = gdal.Open("dst@dbly2.TIF")
    
    for fi in fileName:
        
        print(fi)
        #ds = gdal.Open(fi)
        
        #opens tif and saves image array
        image = tifffile.imread(fi)
        
        #converts 9999. to 0 (convert null data to 0)
        shape = image.shape
        
        for bIndex in range(0, shape[0]):
            for eIndex in range(0,shape[1]):
                if image[bIndex][eIndex] == 0.0:
                    image[bIndex][eIndex] = 9999.0
        
        print(image)
        #print(np.max(image), np.min(image))
        print(image.dtype)

        #displays image created
        tifffile.imwrite('testtif.tiff', image)
        plt.imshow(image)
        #plt.show()

        #applies options 
        if option == 1:       
            #adds array directly to our arrayList
            arrayList.add_array(image, 1)
        else:  
            #adds array to a temporary 'minMax' arrayList
            arrayList.add_array(image, 2)        
    
    #calls mean/min&max function  
    if option == 2:  
        mean_arrays(arrayList, False)
    elif option == 3:  
        max_min_arrays(arrayList, False)
        

def mean_arrays(arrayList, menu):  
    #calculates the mean of selected arrays
    
    #prints options menu if no option chosen
    if menu:  
        print("\nOptions: ")
        print("1: Choose saved arrays (NOT DONE)")
        print("2: Choose .tif files (convert and calculate)")
        print("0: Exit")
        meanOption = input("Please Select an Option: ")
        meanOption = int(meanOption)
    
        #applies options
        if(meanOption == 0):
            return
        if(meanOption == 1):
            arrayList.display_arrays()
            name = input("Enter the names of the .tif files you wish to calculate the mean of: ")
            pass
        if(meanOption == 2):
            tif_to_raw(arrayList, 2)
            #returns here as to not repeat mean calculation
            return
        
    
    #create new array to store result
    shape = arrayList.calculationArray[0].shape
    meanArray = np.zeros(shape)      
    
    #calculates mean
    runs = 0   
    #selects an array within the list
    for ca in arrayList.calculationArray:         
        meanArray = meanArray + ca
        runs = runs + 1
    
    for bIndex in range(0, shape[0]):
        for eIndex in range(0,shape[1]):
            meanArray[bIndex][eIndex] = meanArray[bIndex][eIndex] / runs
                  
    print(meanArray)
    print("\nMean array: ")
    
    arrayList.add_array(meanArray, 1)

def max_min_arrays(arrayList, menu):      
    #calculates the mean of selected arrays
    
    #prints options menu if no option chosen
    if menu:  
        print("\nOptions: ")
        print("1: Choose saved arrays (NOT DONE)")
        print("2: Choose .tif files (convert and calculate)")
        print("0: Exit")
        minMaxOption = input("Please Select an Option: ")
        minMaxOption = int(minMaxOption)
    
        #applies options
        if(minMaxOption == 0):
            return
        if(minMaxOption == 1):
            arrayList.display_arrays()
            name = input("Enter the names of the .tif files you wish to calculate the mean of: ")
            pass
        if(minMaxOption == 2):
            arrayList.calculationArray.clear()
            tif_to_raw(arrayList, 3)
            #returns here as to not repeat mean calculation
            return
        
    
    #create new arrays to store result
    shape = arrayList.calculationArray[0].shape
    minArray = np.full(shape, float("inf"))
    maxArray = np.zeros(shape) 
    
    ##calculates min&max
    #selects array
      
    for bIndex in range(0, shape[0]):
        for eIndex in range(0,shape[1]):
            for ca in arrayList.calculationArray: 
                minArray[bIndex][eIndex] = min(minArray[bIndex][eIndex], ca[bIndex][eIndex])
                maxArray[bIndex][eIndex] = max(maxArray[bIndex][eIndex], ca[bIndex][eIndex])
                  
    print(minArray)
    print("\nMin array: ")
    arrayList.add_array(minArray, 1)
    
    print(maxArray)
    print("\nMax array: ")
    arrayList.add_array(maxArray, 1)

def save_data(arrayList):
    #saves data to "custom name" + ".dat" file
    #user inputs a name to identify file
    #newName = input("Type a name to identify this Array: ")
        
    #open gui to choose file
    Tk().withdraw()
    fileName = asksaveasfilename(filetypes=[("Data Files", "*.obj"), ("All Files", "*.*")]) #opens a dialog box and returns name of file
    
    #saves data
    file = open(fileName + ".obj", 'wb')
    pickle.dump(arrayList, file)
    file.close()
    
    arrayList.display_arrays()
    print("\nData succesfully saved!")

def load_data():
    #loads data from "custom name" + ".dat" file
    #user inputs a name to identify file
    print("Remeber, only load compatable .obj files!")
    
    #open gui to choose file
    Tk().withdraw()
    fileName = askopenfilename(filetypes=[("Data Files", "*.obj"), ("All Files", "*.*")]) #opens a dialog box and returns path to file

    #loads data
    file = open(fileName, 'rb')
    arrayList = pickle.load(file)
    
    arrayList.display_arrays()
    print("\nData succesfully loaded!")
    return arrayList

def export_data(arrayListObject: ArrayList):
    print("Exports data")
    total_hash_map = {}
    for attributes in dir(arrayListObject):
        #attributes is name e.g = temperature2mHash
        if not callable(getattr(arrayListObject, attributes)) and not attributes.startswith("__"):
            print(attributes)
      
            new = "get_" + str(attributes)
            #print(arrayListObject.SkinTemperatureHash.get('hello'))
            total_hash_map[attributes] = arrayListObject.get_totalPrecipitationHash()
    
    print(total_hash_map)







### end functions ###
  

### main ###
arrayListArr = []
arrayListArr.append(ArrayList())

print("\nBooting up .TIF to Raw...")
selection = 1
while selection != 0:
    
    arrayListArr[-1].calculationArray.clear() 
    selection = prompt_user()    
    
    arrayListArr = switch(selection, arrayListArr)
    
print("\nThank you for using .TIF to Raw!\n")
### end main ###          

