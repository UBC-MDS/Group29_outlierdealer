import pandas as pd
import numpy as np

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

        a dataframe which the outlier has already process by the chosen method.
        
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


    # Handle dataframe type error (Check if dataframe is of type Pandas DataFrame)
    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError(f"passed dataframe is of type {type(dataframe).__name__}, should be DataFrame")
        
    # Handle empty dataframe or dataframe with all NAN
    if dataframe.empty or dataframe.dropna().empty:
        raise ValueError("passed dataframe is None")
    
    # Handle columns type error (Check if columns are None or type list)
    if not columns is None and not isinstance(columns, list):
        raise TypeError(f"passed columns is of type {type(columns).__name__}, should be list or NoneType")
    
    # Handle identifier type error (Check if identifier is of type str)
    if not isinstance(identifier, str):
        raise TypeError(f"passed identifier is of type {type(identifier).__name__}, should be string with value 'Z_score' or 'IQR'")
    
    # Handle identifier Value error (Check if identifier has value 'Z_score' or 'IQR')
    if identifier!='Z_score' and identifier!='IQR':
        raise ValueError("passed identifier should have value 'Z_score' or 'IQR'")
        
    # Handle method type error (Check if identifier method is 'trim', 'median' or 'mean')
    if method not in ("trim", "median", "mean"):
        raise Exception("The method must be -trim- or -median- or -mean-")


    if columns is None:
        columns = dataframe.columns
    df_filtered = dataframe[columns]
    numeric_columns = df_filtered.select_dtypes('number').columns
    df_selected = df_filtered[numeric_columns]
    df_selected['outlier'] = False
    
    output = pd.DataFrame(columns=numeric_columns)
    if identifier == 'Z_score':
        df = dataframe.copy()
        target_columns = []
        if columns is None:
            target_columns = list(df.columns.values.tolist())
        else:
            target_columns = columns

        outlier_index = []
        for column in target_columns:
            current_column = df[column]
            mean = np.mean(current_column)
            std = np.std(current_column)
            threshold = 3

            for i in range(len(current_column)):
                current_item = current_column[i]
                z = (current_item - mean) / std
                if z >= threshold:
                    if i not in outlier_index:
                        outlier_index.append(i)
                    if method == "mean":
                        df.at[i, column] = round(mean, 2)
                    if method == "median":
                        df.at[i, column] = np.median(current_column)

        if method == "trim":
            df = df.drop(outlier_index)

        df.index = range(len(df))
        return df


    elif identifier == 'IQR':
        df = dataframe.copy()
        target_columns = []
        if columns is None:
            target_columns = list(df.columns.values.tolist())
        else:
            target_columns = columns

        outlier_index = []
        for column in target_columns:
            current_column = df[column]
            mean = np.mean(current_column)
            std = np.std(current_column)

            for i in range(len(current_column)):
                current_item = current_column[i]
                iqr = np.percentile(current_column, 75) - np.percentile(current_column, 25)
                outlier_index = df_selected[np.abs((current_item - mean) / std) > 1.5*iqr]

                if i not in outlier_index:
                    outlier_index.append(i)
                else:
                    if method == "mean":
                        df.at[i, column] = round(mean, 2)
                    if method == "median":
                        df.at[i, column] = np.median(current_column)

        if method == "trim":
            df = df.drop(outlier_index)

        df.index = range(len(df))
        return df
