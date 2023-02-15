import cdsapi
import numpy as np

#V.2.1
#get_ERA5 is a script that requests all the needed ERA5 data from Copuricus.eu
#   With the transition to monthly data, the variables requested has become an
#   issue, as the API seemingly wont process multiple variables at a time,
#   which neccesitates the seperation of this script from the previous ones. 


#Input to specify year to attain data for
year = input("Specify the year you wish to request ERA5 data from (ex: 2021): ")

#array of variables to request    
requestVars = np.array(['10m_u_component_of_wind', '10m_v_component_of_wind','snow_depth', 'snowfall',
                'surface_latent_heat_flux', 'surface_net_solar_radiation', 'surface_net_thermal_radiation',
                'surface_pressure','total_precipitation'])

#changes requested variable
c = cdsapi.Client()
for currVar in requestVars:    
    
    print("\n")
    print("Requesting Monthly: " + currVar + "\n")
    
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
    print("Requesting Monthly/per hour: " + currVar + "\n")
    
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