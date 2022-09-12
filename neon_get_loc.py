#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 14:29:31 2022

@author: yangello
"""

import sys
import numpy as np
import h5py
import gdal, osr, os
import matplotlib.pyplot as plt
import warnings
from spectral import *

warnings.filterwarnings('ignore')

# assign directory
directory = '/Users/yangello/Documents/Data/NEON_rad_sensor_ortho_line/h5/'


# iterate over files in that directory
for filename in os.listdir(directory):
    if not filename.startswith('.') and os.path.isfile(os.path.join(directory, filename)):
        #print ('Hola')
        file = os.path.join(directory, filename)
        #print(file)
        f = h5py.File(file,'r')
        #list_dataset lists the names of datasets in an hdf5 file
        
        def list_dataset(name,node):
            if isinstance(node, h5py.Dataset):
                print(name)
        #f.visititems(list_dataset)

        #ls_dataset displays the name, shape, and type of datasets in hdf5 file
        def ls_dataset(name,node):
            if isinstance(node, h5py.Dataset):
                print(node)
        #f.visititems(ls_dataset)
        
        igm = f['SERC']['Radiance']['Metadata']['Ancillary_Rasters']['IGM_Data']
        #print(igm)
        
        loc = np.array(igm)
        md = {'lines': igm.shape[0],
          'samples': igm.shape[1],
          'bands': igm.shape[2],
          'header offset' : 0,
          'data ignore value' : -9999,
          'band names': {'1East','2North','3Elevation'}}
        name = filename[:-3]
        outpath= '/Users/yangello/Documents/Data/NEON_rad_sensor_ortho_line/Envi/'
        envi.save_image(outpath+name+'_loc.hdr', loc, dtype=np.float64, interleave = 'bil', byteorder = 0, metadata = md)
        