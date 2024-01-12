import json
import yaml 
import argparse
import requests


class Analysis:

    ''' Load config into an Analysis object

    Load system-wide configuration from `configs/system_config.yml`, user configuration from
    `configs/user_config.yml`, and the specified analysis configuration file

    Parameters
    ----------
    analysis_config : str
        Path to the analysis/job-specific configuration file

    Returns
    -------
    analysis_obj : Analysis
        Analysis object containing consolidated parameters from the configuration files

    Notes
    -----
    The configuration files should include parameters for:
        * GitHub API token
        * Plot color
        * Plot title
        * Plot x and y axis titles
        * Figure size
        * Default save path

    '''
  
    current_config_path='./configs/system_config.yml'

    #constructor will load configuration file upon object instantiation
    def __init__(self, analysis_config=current_config_path):
        self.analysis_config = analysis_config

        with open(self.analysis_config, 'r') as f:
            self.this_config = yaml.safe_load(f)

            print(self.this_config)





    def load_data(self):
        
        print(self.this_config)

    ''' Retrieve data from the GitHub API

    This function makes an HTTPS request to the GitHub API and retrieves your selected data. The data is
    stored in the Analysis object.

    Parameters
    ----------
    None

    Returns
    -------
    None

    '''

obj_1 = Analysis()
obj_1.load_data()
    # def compute_analysis() -> Any:

    # '''Analyze previously-loaded data.

    # This function runs an analytical measure of your choice (mean, median, linear regression, etc...)
    # and returns the data in a format of your choice.

    # Parameters
    # ----------
    # None

    # Returns
    # -------
    # analysis_output : Any

    # '''
