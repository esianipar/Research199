import webbrowser
import time
#V.1.0
#drought is a script that opens a series of new webpages, each with 
#   a request for the drought map for a specific day/month, combination
#   in order to quickly download an entire year's worth of drought data
#  NOTE:
#   This script does not take into account the proper 7 day periods
#   for downloading said files, so many improper webpages will be opene


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
        webbrowser.open("https://edcintl.cr.usgs.gov/downloads/sciweb1/shared/firedanger/download-tool/source_rasters/wfpi-forecast-1/emodis-wfpi-forecast-1_data_2014" + monthReq + dayReq + "_2014" + monthReq + dayReq + ".zip")



#for month in range(1, 12):
#    for day in range(1, 31):
#        webbrowser.open("https://edcintl.cr.usgs.gov/downloads/sciweb1/shared/firedanger/download-tool/source_rasters/wfpi-forecast-1/emodis-wfpi-forecast-1_data_2021" + month + day + "_2021" + month + day + ".zip")
#