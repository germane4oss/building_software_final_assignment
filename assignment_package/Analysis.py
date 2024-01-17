from typing import Any, Optional
import matplotlib
import matplotlib.pyplot as plt
import yaml
import argparse
import requests
import json
import logging


class Analysis():
    
    def __init__(self, analysis_config:str):
        CONFIG_PATHS = ['configs/system_config.yml', 'configs/user_config.yml']

        # add the analysis config to the list of paths to load
        paths = CONFIG_PATHS + [analysis_config]

        # initialize empty dictionary to hold the configuration
        config = {}

        # load each config file and update the config dictionary
        for path in paths:
            with open(path, 'r') as f:
                this_config = yaml.safe_load(f)
            
            # verify that a configuration was loaded    
            if this_config:
                config.update(this_config)

        self.config = config
        

    def load_data(self)->dict:
        
        headers = {'Authorization': 'Bearer ' + self.config['token']}
        
        try:
            # send request to GitHub
            github_response = requests.get(self.config['url'], headers=headers)

        except requests.exceptions.ConnectionError:
            logging.warning('Unable to retrieve Information from GitHub') 

        self.raw_data = github_response
        

    def compute_analysis(self):
        
        # convert the collected data into json
        json_data = json.loads(self.raw_data.text)
        
        # Load json into a dictionary

        items = json_data['items']
        
        # Define repo_name and repo_starts arrays for plotting

        repo_name=[]
        repo_stars=[]

        # Iterate the received data to populate repo_name and repo_stars
        
        for item in items:
          repo_name.append(item['name'])
          repo_stars.append(item['stargazers_count'])
          
          self.repo_name = repo_name
          self.repo_stars = repo_stars
      
    
    
#    def plot_data(self, save_path:Optional[str] = None) -> plt.Figure:

    def plot_data(self, save_path: Optional[str] = None):

        # Create a bar plot
        plt.barh(self.repo_name, self.repo_stars)
        plt.xlabel(self.config['xlabel'])
        plt.ylabel(self.config['ylabel'])
        plt.title(self.config['title'])
        plt.show()
