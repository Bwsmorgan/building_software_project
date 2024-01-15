import Analysis
import pytest

def test_compute_analysis():

    inputs = ['./configs/job_config.yml', './configs/system_config.yml', './configs/user_config.yml']
    exp_output = 100

    sum_of_figure_size = 0

    for i in inputs:

        sum_of_figure_size += Analysis(i).this_config['figure_size']
    
    median_figure_size = sum_of_figure_size/len(inputs)
    
    actual_output = Analysis.compute_analysis(self)


