#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 16:44:11 2022

@author: yangello
"""

import sys
import numpy as np
import h5py
#import gdal, osr, os
import os
#import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')

# assign directory
# modify directory to your own path where you store the h5 radiance files
directory = '/Users/yangello/Documents/Data/NEON_rad_sensor_ortho_line/h5/'


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
        #rad[rad > 255] = -9999
        rad[rad > 255] = np.nan
        rad = rad.astype('f4')
        
     
        print('Start writing new file')
        dset = f.create_dataset('/Users/yangello/Documents/Data/NEON_rad_sensor_ortho_line/Envi/Radiance/Radiance_total', data=rad, dtype='f4')
        
        dset.attrs['Dimension_Labels'] = ['Line', 'Sample', 'Wavelength']
        dset.attrs['Interleave'] = 'bil'
        
        
        f.close()
