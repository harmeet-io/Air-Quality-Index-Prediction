
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 10:54:05 2023

@author: srivastavashantam
"""


## Data Collection - we will use this url - "https://en.tutiempo.net/"
# step 1 - At first, we will collect all the html files that contains data for bangalore city.
# from these url's well can get all the independent features required for this project but they dont contain the output feature i.e. AQI, so we'' fetch AQI from a different source.
# output feature is taken from 3rd party api = weathermap.com

import os
import time
import requests
import sys
import os
os.chdir("C:\\Users\\sriva\\Downloads\\Data_Science\\ML_Projects\AQI")

def retrieve_html():
    for year in range(2013,2019):
        for month in range(1,13):
            if(month<10):
                url='http://en.tutiempo.net/climate/0{}-{}/ws-421820.html'.format(month
                                                                          ,year)
            else:
                url='http://en.tutiempo.net/climate/{}-{}/ws-421820.html'.format(month
                                                                          ,year)
            texts=requests.get(url)
            text_utf=texts.text.encode('utf=8')
            
            if not os.path.exists("Data/Html_Data/{}".format(year)):
                os.makedirs("Data/Html_Data/{}".format(year))
            with open("Data/Html_Data/{}/{}.html".format(year,month),"wb") as output:
                output.write(text_utf)
            
        sys.stdout.flush()
        
if __name__=="__main__":
    start_time=time.time()
    retrieve_html()
    stop_time=time.time()
    print("Time taken {}".format(stop_time-start_time))
        
    