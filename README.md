# hytools-NEON-Rad_h5toEnvi-Obs-Loc
Hytools-based tools to export NEON Radiance H5 swaths to Envi and creating Obs and Loc ancillary input files for ISOFIT atmospheric correction

This tool is based on Hytools, so you would require to install it. Link: https://github.com/EnSpec/hytools

It is advised to create and activate a conda environment to run Hytools. For Mac M1, create the environment with python=3.8 

Once you have activated your environment, follow the steps:

1. Copy/paste the here provided neonrad.py and neon.py scripts within the hytools/io folder, e.g following path:

          /Users/YourUsername/opt/anaconda3/envs/hytools_env/lib/python3.8/site-packages/hytools/io/neonrad.py
          /Users/YourUsername/opt/anaconda3/envs/hytools_env/lib/python3.8/site-packages/hytools/io/envi.py

3. Make a copy of the original base.py script (for instance: base copy.py), and copy/paste the here provided base.py:

         /Users/YourUsername/opt/anaconda3/envs/hytools_env/lib/python3.8/site-packages/hytools/base.py


5. Create an open a folder for your own hytools-based script and config files, e.g.:
~/hytools/
          
          |_neon/
                |_scripts/
               
       cd /Users/YourUsername/hytools/neon/scripts

4. Copy/paste the here provided scripts, e.g.: ~/hytools/neon/scripts/

        |_Modyfying_h5_rad.py
        |_neon_get_loc.py
        |_neon2envi_json_generate.py
        |_neonrad2envi.py
        |_neon2envi_run_setup_config.cfg

5. The NEON L1 at-sensor radiance image data is provided in H5 format. Data are delivered in two separate images. The first contains the integer portion of the at-sensor radiance value, and the second provides the decimal part scaled by 50000. To achieve the observed at-sensor radiance value, the integer portion must be added to the decimal portion, after the decimal portion is divided by 50000. 

Open and update the provided Modifying_h5_rad.py accordingly to your own working path and data. This script joins the integer and decimal, creating a new layer 'Radiance_total' that we will use for creating the ENVI files. Run the updated script:

        python Modifying_h5_rad.py
        
6. Open and update the provided neon_get_loc.py accordingly to your own working and output path and data. This script export the IGM layers as a 3-band 'loc' ENVI file. Run the updated script:

        python neon_get_loc.py

7. Open and update the provided neon2envi_run_setup_config.cfg file including input h5 radiance files/output Envi files directory, etc. Then run:

        python neon2envi_json_generate.py --config neon2envi_run_setup_config.cfg

8. The previous step have created a .json file within your scripts folder (see provided exampled), which will be used to set and run the neonrad2envi.py script. Run:

        python neonrad2envi.py --config neon2envi_config.json

9. That's all. Look for the radiance, obs and loc files in your output directory. 
