# Final Project : Building Software

## Overview

This project is an installable Python package that analyzes data retrieved from the GitHub API.

The development process for this project involved implementing a list of unique features/requirements that are essential to building software with Python. Implemeting these features gave me an opportunity to refine/develop my skills as well as glimpse of what is needed to develop software in the real world.

The following features/requirements were necessary in this project:

    - create configuration files using valid YAML 
    - installable using pip: pip install git+https://github.com/user/yourteamrepo
    - include a module named Analysis
    - include a README.md, LICENSE, and CONDUCT.md file
    - include unit tests, as appropriate
    - include a TESTS.md file detailing in point-form the non-automated tests to be performed, as appropriate
    - use the logging library to output debug, info, and error messages as appropriate
    - be documented using Python docstrings in the numpy style
    - use try/except to handle errors, must raise useful error messages, and must include at least one assertion

## Installation

Users should be able to use this package by running the following code on Colab.

> !pip install git+https://github.com/user/yourteamrepo
> from yourteamrepo import Analysis

> analysis_obj = Analysis.Analysis('config.yml')
> analysis_obj.load_data()

> analysis_output = analysis_obj.compute_analysis()
> print(analysis_output)

> analysis_figure = analysis_obj.plot_data()

## Learning Objectives

    - interpret and write simple YAML files
    - loading YAML files into Python
    - use a Python or HTTP API
    - write API documentation
    - write docstrings compliant with the numpy docstring specifications 
    - write Python class and function headers 
    - catch and handle errors using try/except
    - write helpful error messages
    - use the Python logging library to control output from my code
    - write unit tests and integration tests using pytest
    - write a basic setup.py configuration file for setuptools
    - install a package from GitHub using pip

# Helpful links/References

https://stackoverflow.com/questions/9272535/how-to-get-a-file-via-github-apis

