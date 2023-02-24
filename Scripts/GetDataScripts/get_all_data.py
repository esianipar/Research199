import cdsapi
import requests
import numpy as np
from datetime import datetime
import os, zipfile
#V.1.0
#get_all_data is a script that preforms HTML get requests to a series 
#   of webpages, each with a section of the data necessary for 
#   combination.
#  NOTE:
#   This script does not take into account the proper amount of days
#   per month. This, in effect, allows easy modification of use during
#   leap years. Incorrect tabs will remain open, and must be closed
#   manually.
# Written by Nico Platt

#Tools for better access by Noel Sianipar

def unzip_files(dir_name:str):
    #dir_name = 'C:\\SomeDirectory'
    extension = [".zip", ".gz"]
    os.chdir(dir_name) # change directory from working dir to dir with files

    for item in os.listdir(dir_name): # loop through items in dir
        for ext in extension:
            if item.endswith(ext): # check for ".zip" extension
                file_name = os.path.abspath(item) # get full path of files
                zip_ref = zipfile.ZipFile(file_name) # create zipfile object
                zip_ref.extractall(dir_name) # extract file to dir
                zip_ref.close() # close file
                os.remove(file_name) # delete zipped file




###------------------------Functions------------------------###
def preform_request(url, reqType):
    
    print('Downloading: ' + reqType + ' Data...')
    
    try:
        r = requests.get(url)
        filename = url.split('/')[-1] # this will take only -1 splitted part of the url
        
        if r:
            # Do processing here
            with open(filename,'wb') as output_file:
                output_file.write(r.content)
             
            print('Success!\n')
        else:
            print('No data to download for current date.\n')
    
    except:
        print('Failed to Access Server.\n')     


def request_extreme_events(yearReq, monthReq, dayReq):
    
    print('Attempting to find EXTREME EVENT data, this may take some time...')
    startYear = int(yearReq)
    currentYear = datetime.now().year + 1
    
    #changes years from 
    for year in range(startYear, currentYear):
        try:
            url = "https://www1.ncdc.noaa.gov/pub/data/swdi/stormevents/csvfiles/StormEvents_details-ftp_v1.0_d" + yearReq + "_c" + str(year) + monthReq + dayReq + ".csv.gz"
            r = requests.get(url)
            filename = url.split('/')[-1] # this will take only -1 splitted part of the url
            
            #if we find the correct file, exit function!
            if r:
                # Do processing here
                with open(filename,'wb') as output_file:
                    output_file.write(r.content)
                 
                print('Success!\n') 
                return True
        
        except:
            print('Failed to Access Server.\n')

    #if data is not found
    print('No data to download for: ' + monthReq + '/' + dayReq + '.\n')
    return False
         
###------------------------Functions------------------------### 



###------------------------Body------------------------###
year = input("Specify the year you wish to request Fire data from (ex: 2021): ")

##ERA5
#array of variables to request    
requestVars = np.array(['10m_u_component_of_wind', '10m_v_component_of_wind','snow_depth', 'snowfall',
                'surface_latent_heat_flux', 'surface_net_solar_radiation', 'surface_net_thermal_radiation',
                'surface_pressure','total_precipitation'])

#changes requested variable
c = cdsapi.Client()
for currVar in requestVars:    
    
    print("\n")
    print("Requesting ERA5 Monthly: " + currVar + "\n")
    
    #prefoms request    
    c.retrieve(
        'reanalysis-era5-land-monthly-means',
        {
            'area': [
                34.9, -119.69, 34,
                -117.28,
            ],
            'format': 'grib',
            'year': year,
            'product_type': 'monthly_averaged_reanalysis',
            'time': '00:00',
  
            'variable': currVar,
            'month': [
                '01', '02', '03',
                '04', '05', '06',
                '07', '08', '09',
                '10', '11', '12',
            ],
        },
        currVar + '.grib')
        
        
#array of variables to request    
requestVars = np.array(['2m_temperature',
                'skin_temperature'])

#changes requested variable
c = cdsapi.Client()
for currVar in requestVars:    
    
    print("\n")
    print("Requesting ERA5 Monthly/per hour: " + currVar + "\n")
    
    #prefoms request    
    c.retrieve(
    'reanalysis-era5-land-monthly-means',
    {
        'product_type': 'monthly_averaged_reanalysis_by_hour_of_day',
        'variable': currVar,
        'year': year,
        'month': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
        ],
        'time': [
            '00:00', '01:00', '02:00',
            '03:00', '04:00', '05:00',
            '06:00', '07:00', '08:00',
            '09:00', '10:00', '11:00',
            '12:00', '13:00', '14:00',
            '15:00', '16:00', '17:00',
            '18:00', '19:00', '20:00',
            '21:00', '22:00', '23:00',
        ],
        'area': [
            34.9, -119.69, 34,
            -117.28,
        ],
        'format': 'grib',
    },
    currVar + '.grib')
    
    
#Fire, Drought, Extreme
##brute force method - properly ordered by download time
# used to skip extreme events if already found (since only 1 per year)
found_Extreme = False
for month in range(1, 13):
    
    # changes month into proper string format
    if month < 10:
        monthReq = "0" + str(month)
    else:
        monthReq = str(month)

    ## increments day
    for day in range(1, 32):
        
        # changes day into proper string format
        if day < 10:
            dayReq = "0" + str(day)
        else:
            dayReq = str(day)    

        # preform download request to FIRE website
        url = "https://edcintl.cr.usgs.gov/downloads/sciweb1/shared/firedanger/download-tool/source_rasters/wfpi-forecast-1/emodis-wfpi-forecast-1_data_" + year + monthReq + dayReq + "_" + year + monthReq + dayReq + ".zip"
        preform_request(url, "FIRE")
        
        # preform download request to DROUGHT website
        url = "https://droughtmonitor.unl.edu/data/shapefiles_m/USDM_"+ year + monthReq + dayReq + "_M.zip"
        preform_request(url, "DROUGHT")
        
        # if the file has not been found, preform download request to EXTREME EVENTS data
        if(not(found_Extreme)):
            found_Extreme = request_extreme_events(year, monthReq, dayReq)
        
print("Retrive data request for " + year + " has completed!")



###------------------------Body------------------------###