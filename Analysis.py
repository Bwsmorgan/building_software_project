class Analysis:
  
  job_config_path='./configs/job_config.yml'

  #constructor will load job-specific configuration file upon object instantiation
  def __init__(self, analysis_config=job_config_path):
    self.analysis_config = analysis_config


  def load_data():

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


  def compute_analysis() -> Any

    '''Analyze previously-loaded data.

    This function runs an analytical measure of your choice (mean, median, linear regression, etc...)
    and returns the data in a format of your choice.

    Parameters
    ----------
    None

    Returns
    -------
    analysis_output : Any

    '''


  def plot_data(save_path:Optional[str] = None) -> matplotlib.Figure