def outlier_identifier(dataframe, columns=None, identifier = 'Z_score'):
    """
    A function that identify and summarize the count and range of based on the method the user choose
    Parameters
    ----------
    dataframe : pandas.core.frame.DataFrame
        The target dataframe where the function is performed.
    columns : list, default=None
        The target columns where the function needed to be performed. Default is None, the function will check all columns
    identifier : string
        The method of identifying outliers.
        - if "Z_score" : Use z-test with threshold of 3
        - if "IQR" : Use IQR (Inter Quantile range) to identify outliers

    Returns
    -------
    pandas.core.frame.DataFrame
        a dataframe with the summary of the outlier identified by the method
    Examples
    --------
    >>> import pandas as pd
        
    >>> df = pd.DataFrame({
    >>>    'SepalLengthCm' : [0.1, 4.9, 52.7, 5.5, 5.1, 50, 5.4, 179.0, 5.2, 5.3, 5.1],
    >>>    'SepalWidthCm' : [1.4, 1.4, 20, 2.0, 0.7, 1.6, 1.2, 14, 1.8, 1.5, 2.1],
    >>>    'PetalWidthCm' : [0.2, 0.2, 0.2, 0.3, 0.4, 0.5, 0.5, 0.6, 0.4, 0.2, 5]
    >>> })
    >>> outlier_identifier(df)
    	                SepalLengthCm  	    SepalWidthCm	   PetalWidthCm
    Outlier Count	         1	                3	                1
    Outlier Percentage       0.09               0.27                0.09
    Mean                     28.936364          4.336364            0.772727
    Median                   5.300000           1.600000            0.400000
    std                      53.196264          6.414557            1.409320
    Lower Range     	     NA	                NA	                NA
    Upper Range              179                (1.6, 20)           5.0
    """