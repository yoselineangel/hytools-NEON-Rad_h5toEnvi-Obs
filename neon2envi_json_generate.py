"""
Modified by @yoselineangel from:

https://github.com/TESTgroup-BNL/hytools_helpers/blob/main/modex_examples/create_config_aviris.py 

Created on Sat Mar  17 16:04:00 2022
@author: queally, Shawn P. Serbin
"""
'''Template script for generating neon2envi configuration JSON files.
    
    These settings are meant only as an example, are not appropriate for
    all situations and may need to be adjusted
'''

import json
import glob
import numpy as np
import os,argparse
import configparser
from os.path import expanduser

### get info about machine and set config file
print("Running on:")
print(os.environ.get('HOSTNAME'))
print(" ")

#-- setup config file here
# get config file from script call
parser = argparse.ArgumentParser()
parser.add_argument('--config', help='path to configuration file to use',
    required=True)
args = parser.parse_args()
print(f'Config file: {args.config}')
config = configparser.ConfigParser()
config_file_in = args.config
config.read(config_file_in)
print(" ")
#--

#---- Set options based on config file options
# main image output directory
output_dir = config.get("rundirs", "output_dir")
os.makedirs(output_dir, exist_ok=True) # make ouput folder
print("Output directory: "+output_dir)
print(" ")

#Output path for configuration file
config_dir = config.get("jsonconfig", "json_config_dir")
os.makedirs(config_dir, exist_ok=True) # make ouput config_dir folder
json_name = config.get("jsonconfig", "json_config_name")
config_file = os.path.join(config_dir,json_name)
print("JSON config file: "+config_file)
print(" ")

# create blank dictionary to populate the rest of the options
config_dict = {}

# -- 
image_dir = config.get("rundirs", "image_dir")
image_ext = config.get("imginfo", "extension")
images_dir = os.path.join(image_dir,'*'+image_ext)
print("Input Image Directory: "+images_dir)
images = glob.glob(images_dir)
images.sort()
config_dict["input_files"] = images
print("Input Images: ")
print(*config_dict["input_files"], sep = "\n")
print(" ")

  
    # Export settings
#################################################################
''' Options for subset waves:
    1. List of subset wavelenths
    2. Empty list, this will output all good bands, if resampler is
    set it will also resample.
    - Currently resampler cannot be used in conjuction with option 1
'''

config_dict['export'] = {}
config_dict['export']['output_dir'] = output_dir


## define parallel options
ptype = config.get("parallel", "ptype")
print("Parallel type: "+ptype)
if ptype == "dynamic" :
    config_dict['num_cpus'] = len(images)
elif ptype == "fixed" :
    numcpus = config.get("parallel", "num_cpus")
    config_dict['num_cpus'] = numcpus
#print("Number of CPUs in Processing: "+config_dict['num_cpus'])
print("Number of CPUs in Processing: ",config_dict["num_cpus"])
print(" ")

with open(config_file, 'w') as outfile:
    json.dump(config_dict,outfile,indent=3)