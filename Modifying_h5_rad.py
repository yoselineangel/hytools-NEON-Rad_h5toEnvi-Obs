#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 16:44:11 2022

@author: yangello
"""

import sys
import numpy as np
import h5py
import gdal, osr, os
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')

# assign directory
# modify directory to your own path where you store the h5 radiance files
directory = '/Users/yangello/Documents/Data/NEON_rad_sensor-ortho-line/h5/'


# iterate over files in that directory
for filename in os.listdir(directory):
    if not filename.startswith('.') and os.path.isfile(os.path.join(directory, filename)):
        #print item
        file = os.path.join(directory, filename)
        print('Modifying Radiance')
        
        f = h5py.File(file,'r+')
        # modify the NEON site, e.g. SERC , accordingly to your data
        rad_dec = f['SERC']['Radiance']['RadianceDecimalPart']
        rad_int = f['SERC']['Radiance']['RadianceIntegerPart']
        rad = (rad_int[:,:,:] + (rad_dec [:,:,:]/50000))
        rad[rad > 255] = -9999
        rad = rad.astype(np.float32)
        f.create_dataset('/SERC/Radiance/Radiance_total', data=rad, dtype=np.float32)
        f.close()