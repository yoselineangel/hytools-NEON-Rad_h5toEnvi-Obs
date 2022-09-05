# -*- coding: utf-8 -*-
#modified by Yoseline Angel
#NEON Radiance
"""
HyTools:  Hyperspectral image processing library
Copyright (C) 2021 University of Wisconsin

Authors: Adam Chlus, Zhiwei Ye, Philip Townsend.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

NEON AOP HDF opener
"""
import h5py
import numpy as np


def open_neon(hy_obj, no_data = -9999):
    """Load and parse NEON formated HDF image into a HyTools file object.

    Args:
        src_file (str): pathname of input HDF file.
        no_data (float, optional): No data value. Defaults to -9999.

    Returns:
        HyTools file object: Populated HyTools file object.

    """

    hdf_obj = h5py.File(hy_obj.file_name,'r')
    print(hdf_obj)
    hy_obj.base_key = list(hdf_obj.keys())[0]
    print(hy_obj.base_key)
    metadata = hdf_obj[hy_obj.base_key]['Radiance']['Metadata']
    print(metadata)
    data = hdf_obj[hy_obj.base_key]['Radiance']['Radiance_total']
    print(data)

    hy_obj.projection = metadata['Coordinate_System']['Coordinate_System_String'][()].decode("utf-8")
    print(hy_obj.projection)
    hy_obj.map_info = metadata['Coordinate_System']['Map_Info'][()].decode("utf-8").split(',')
    hy_obj.transform = (float(hy_obj.map_info [3]),float(hy_obj.map_info [1]),0,float(hy_obj.map_info [4]),0,-float(hy_obj.map_info [2]))
    hy_obj.fwhm =  metadata['Spectral_Data']['FWHM'][()]
    hy_obj.wavelengths = metadata['Spectral_Data']['Wavelength'][()]
    hy_obj.wavelength_units = metadata['Spectral_Data']['Wavelength'].attrs['Units']
    hy_obj.lines = data.shape[0]
    hy_obj.columns = data.shape[1]
    hy_obj.bands = data.shape[2]
    hy_obj.bad_bands = np.array([False for band in range(hy_obj.bands)])
    hy_obj.no_data = no_data
       
    pathl = hdf_obj[hy_obj.base_key]['Radiance']['Metadata']['Ancillary_Rasters']['OBS_Data'][:,:,0]
    print(pathl)
    hy_obj.anc_path = {'path_length':['Ancillary_Rasters','OBS_Data']}
    #hy_obj.anc_path = {'path_length':['Ancillary_Rasters','OBS_Data'],
    #                    'sensor_az': ['Ancillary_Rasters','OBS_Data'],
    #                    'sensor_zn': ['Ancillary_Rasters','OBS_Data'],
    #                    'solar_az': ['Ancillary_Rasters','OBS_Data'],
    #                    'solar_zn': ['Ancillary_Rasters','OBS_Data'],
    #                    'solar_phase': ['Ancillary_Rasters','OBS_Data'],
    #                    'slope':['Ancillary_Rasters','OBS_Data'],
    #                    'aspect': ['Ancillary_Rasters','OBS_Data'],
    #                    'cosine_i': ['Ancillary_Rasters','OBS_Data'],
    #                    'utc_time': ['Ancillary_Rasters','OBS_Data']}

    print(hy_obj.anc_path)
    return hy_obj
