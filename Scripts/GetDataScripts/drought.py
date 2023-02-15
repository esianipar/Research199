import webbrowser
import time
#V.2.0
#get_drought is a script that opens a series of new webpages, each with 
#   a request for the drought map for a specific day/month, combination
#   in order to quickly download an entire year's worth of drought data
#  NOTE:
#   This script does not take into account the proper 7 day periods
#   for downloading said files, so many improper webpages will be opene

#Input to specify year to attain data for
year = input("Specify the year you wish to request Drought data from (ex: 2021): ")

##brute force method - properly ordered by download time
for month in range(1, 13):
    
    # changes month into proper string format
    if month < 10:
        monthReq = "0" + str(month)
    else:
        monthReq = str(month)

    ## increments day
    for day in range(1, 32):
        time.sleep(1)
        # changes day into proper string format
        if day < 10:
            dayReq = "0" + str(day)
        else:
            dayReq = str(day)    

        # preform request
        webbrowser.open("https://droughtmonitor.unl.edu/data/shapefiles_m/USDM_"+ year + monthReq + dayReq + "_M.zip")