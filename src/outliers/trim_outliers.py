def trim_outliers(dataframe, columns=None, identifier='Z_score', method='trim'):

    """
    A function to generate outlier free dataset by imputing them with mean, median or trim entire row with outlier from dataset.
     ----------
    dataframe : pandas.core.frame.DataFrame
        The target dataframe where the function is performed.
    columns : list, default=None
        The target columns where the function needed to be performed. Default is None, the function will check all columns
    identifier : string
        The method of identifying outliers.
        - if "Z_score" : Use z-test with threshold of 3
        - if "IQR" : Use IQR (Inter Quantile range) to identify outliers
    method : string
        The method of dealing with outliers.
            - if "trim" :  remove completely rows with data points having outliers.
            - if "median" : replace outliers with median values
            - if "mean" : replace outliers with mean values
            
    Return
    -------
    pandas.core.frame.DataFrame
        a dataframe with the summary of the outlier identified by the method
        
    Examples
    --------
    >>> import pandas as pd
    
    >>> df = pd.DataFrame({
    >>>    'SepalLengthCm' : [5.1, 4.9, 4.7, 5.5, 5.1, 50, 5.4, 5.0, 5.2, 5.3, 5.1],
    >>>    'SepalWidthCm' : [1.4, 1.4, 20, 2.0, 0.7, 1.6, 1.2, 1.4, 1.8, 1.5, 2.1],
    >>>    'PetalWidthCm' : [0.2, 0.2, 0.2, 0.3, 0.4, 0.5, 0.5, 0.6, 0.4, 0.2, 5]
    >>> })
    >>> trim_outliers(df, columns=['SepalLengthCm', 'SepalWidthCm', 'PetalWidthCm'],identifier='Z_score', method='trim')
    	 SepalLengthCm  	SepalWidthCm	   PetalWidthCm
    0	5.1	                1.4	                0.2
    1	4.9	                1.4	                0.2
    2	5.5	                2.0	                0.3
    3	5.1	                0.7	                0.4
    4	5.4	                1.2             	0.5
    5	5.0	                1.4	                0.6
    6	5.2	                1.8	                0.4
    7	5.3	                1.5	                0.2
    """
