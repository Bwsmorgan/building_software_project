from Analysis import Analysis
# import pytest
import random

def test_compute_analysis():

    # inputs = './configs/job_config.yml'
   
    #create an instance of Analysis
    analysis_obj1 = Analysis()

    #when our instance is created we will output a list containing a dictionary of each config
    #where each paramater is listed with its respective value
    list_of_configs = analysis_obj1.configs

    sum_of_figure_size = 0

    #for each config we create a random figure size and calculate the mean value of all 3 figure sizes 
    for config in list_of_configs:
        new_figure_size = random.randint(1, 10)
        config['figure_size'] = new_figure_size
        sum_of_figure_size += new_figure_size

    
    median_figure_size = sum_of_figure_size/3
    exp_output = median_figure_size
    
    actual_output = analysis_obj1.compute_analysis()
    print('actual output')
    print(actual_output)
    print('expected input')
    print(exp_output)
    assert actual_output == exp_output

test_compute_analysis()