def outlier_identifier(dataframe, columns=None, identifier = 'IQR', return_df=False):
    """
    A function that identify and summarize the count and range of based on the method the user choose
    Parameters
    ----------
    dataframe : pandas.core.frame.DataFrame
        The target dataframe where the function is performed.
    columns : list, default=None
        The target columns where the function needed to be performed. Default is None, the function will check all columns
    identifier : string, default='IQR'
        The method of identifying outliers.
        - if "Z_score" : Use z-test with threshold of 3
        - if "IQR" : Use IQR (Inter Quantile range) to identify outliers (default)
    return_df : bool, default=False
        Can be set to True if want output as dataframe identified with outliers in rows

    Returns
    -------
    pandas.core.frame.DataFrame 
    (a dataframe with the summary of the outlier identified by the method) if return_df = False , 
    (a dataframe with additional column having if row has outlier or not) if return_df = True
    
    Examples
    --------
    >>> import pandas as pd
        
    >>> df = pd.DataFrame({
    >>>    'SepalLengthCm' : [5.1, 4.9, 4.7, 5.5, 5.1, 50, 54, 5.0, 5.2, 5.3, 5.1],
    >>>    'SepalWidthCm' : [1.4, 1.4, 20, 2.0, 0.7, 1.6, 1.2, 1.4, 1.8, 1.5, 2.1],
    >>>    'PetalWidthCm' : [0.2, 0.2, 0.2, 0.3, 0.4, 0.5, 0.5, 0.6, 0.4, 0.2, 5]
    >>> })
    >>> outlier_identifier(df)
    	                SepalLengthCm SepalWidthCm PetalWidthCm
    outlier_count                  2            1            1
    outlier_percentage        18.18%        9.09%        9.09%
    mean                       13.63         3.19         0.77
    median                       5.1          1.5          0.4
    std                        18.99         5.59         1.41
    lower_range                  NaN          NaN          NaN
    upper_range         (50.0, 54.0)         20.0          5.0
    """