# hytools-NEON-Rad_h5toEnvi-Obs
Hytools-based tools to export NEON Radiance H5 swaths to Envi + Obs ancillary files for ISOFIT atmospheric correction

Instructions to convert NEON Radiance h5 swaths to Envi and to get ancillary Observation (obs) files

This tool is based on Hytools, so you would require to install it. Link: https://github.com/EnSpec/hytool

It is advised to create and activate a conda environment to run Hytools.

Once you have activated your environment, follow the steps:

1. Copy/paste the here provided neonrad.py script within the hytools/io folder, e.g following path:
/Users/yangello/opt/anaconda3/lib/python3.9/site-packages/hytools/io/neonrad.py

2. Make a copy of the original base.py script (for instance: base copy.py), and copy/paste the here provided base.py:
/Users/yangello/opt/anaconda3/lib/python3.9/site-packages/hytools/base.py

3. Create an open a folder for your own hytools-based script and config files, e.g.:
~/hytools/
          
          |_neon/
                |_configs/
                |_scripts/
               
cd /Users/yangello/Documents/conda_envs/hytools/neon/scripts

4. Copy/paste the here provided scripts, e.g.: ~/hytools/neon/scripts/

        |_Modyfying_h5_rad.py
        |_neon2envi_json_generate.py
        |_neonrad2envi.py
        |_neon2envi_run_setup_config.cfg

5. The NEON L1 at-sensor radiance image data is provided in H5 format. Data are delivered in two separate images. The first contains the integer portion of the at-sensor radiance value, and the second provides the decimal part scaled by 50000. To achieve the observed at-sensor radiance value, the integer portion must be added to the decimal portion, after the decimal portion is divided by 50000. 

Open and update the provided Modifying_h5_rad.py accordingly to your own working path adn data. This script joins the integer and decimal, creating a new layer 'Radiance_total' that we will use for creating the ENVI files. Run the updated script:

        python Modifying_h5_rad.py

6. Open and update the provided neon2envi_run_setup_config.cfg file including input h5 radiance files/output Envi files directory, etc. Then run:

        python neon2envi_json_generate.py --config neon2envi_run_setup_config.cfg

7. The previous step have created a .json file within your configs folder, which will be used to set and run the neonrad2envi.py script. Run:

        python neonrad2envi.py --config /Users/yangello/Documents/conda_envs/hytools/neon/configs/neon2envi_config.json

8. That's all. Check the radiance and obs files in your output directory. 
