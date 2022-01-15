def visualize_outliers(dataframe, columns=None):
    """
    A function that plot out the given data with outliers marked.
    Parameters
    ----------
    dataframe : pandas.core.frame.DataFrame
        The target dataframe where the function is performed.
    columns : list, default=None
        The target columns where the function needed to be performed. Default is None, the function will check all columns.
    Returns
    -------
    altair.vegalite.v4.api.Chart
        an altair plot with data distribution as well as marked outliers.
    Examples
    --------
    >>> import pandas as pd
    >>> import altair as alt
        
    >>> df = pd.DataFrame({
    >>>    'SepalLengthCm' : [0.1, 4.9, 52.7, 5.5, 5.1, 50, 5.4, 179.0, 5.2, 5.3, 5.1],
    >>>    'SepalWidthCm' : [1.4, 1.4, 20, 2.0, 0.7, 1.6, 1.2, 14, 1.8, 1.5, 2.1],
    >>>    'PetalWidthCm' : [0.2, 0.2, 0.2, 0.3, 0.4, 0.5, 0.5, 0.6, 0.4, 0.2, 5]
    >>> })

    >>> visualize_outliers(df, columns=['SepalLengthCm', 'SepalWidthCm'])
    """