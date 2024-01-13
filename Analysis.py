import json
import yaml 
import argparse
import requests
import logging
import pprint
import base64

logging.basicConfig(level=logging.DEBUG, filename='logging.log')

class Analysis:
  
    current_config_path='./configs/job_config.yml'

    #constructor will load configuration file upon object instantiation
    def __init__(self, analysis_config=current_config_path):

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

        self.analysis_config = analysis_config

        CONFIG_PATHS = ['configs/system_config.yml', 'configs/user_config.yml']

        paths_to_load = CONFIG_PATHS + [self.analysis_config]

        config = {}

        for path in paths_to_load:
            print(f'Loading... {path}\n')
            with open(path, 'r') as f:
                self.this_config = yaml.safe_load(f)

            config.update(self.this_config)

            print(f'{self.this_config} \n')


    def load_data(self):

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
        
        print(f'{self.this_config} \n')

        #we retrieve our github api token from our config file and set its value to a unique variable
        token = self.this_config.get('github_api_token')

        owner = 'Bwsmorgan'
        repo = 'building_software_project'

        url = 'https://api.github.com/repos/Bwsmorgan/building_software_project/contents/configs/job_config.yml'
        # url_2 = "https://api.github.com/user/'building_software_project'/contents/'/configs/system_config.yml'"
        headers = {'Authorization': 'Bearer ' + token}
        
        try:
            #get response from first API
            response = requests.get(url, headers=headers)
            print('success from first API.')

        except requests.exceptions.ConnectionError:
            print('Connection Error from first API.')
            #connection error to first API. Try Second
            response = requests.get(url, headers=headers)
            print('success from second API.')

        response_json = json.loads(response.text)
      

        print(f'{response.status_code}\n') 
        print(f'{response_json}\n')
        print(response_json['content'])

        file_content_encoding = response_json.get('encoding')

        if file_content_encoding == 'base64':
            file_content = base64.b64decode(response_json['content']).decode()
        
        print(file_content)
        print(token)

        return response_json
        # print(self.analysis_config['github_api_token'])
    

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
