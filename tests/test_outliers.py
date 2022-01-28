import pandas as pd
from pandas._testing import assert_frame_equal
import numpy as np
import pytest
from pytest import raises
from py_outliers_utils.outliers import outlier_identifier

# Arrange
@pytest.fixture
def input_iqr():
    df = pd.DataFrame({ 'SepalLengthCm' : [5.2, 4.9, 4.7, 5.5, 5.1, 5.0, 6.0, 54, 50, 5.3, 5.1],
                        'SepalWidthCm' :  [-5.4, 1.4, -5.7, 0.2, 0.7, 1.6, 1.2, 1.4, 1.8, 1.5, 2.1],
                        'PetalWidthCm' :  [-40, 0.2, 0.2, 0.3, 0.2, 0.5, 0.5, 0.6, 0.4, 0.2, 5],
                        'class': ['Iris Setosa', 'Iris Versicolour', 'Iris Virginica', 'Iris Setosa', 'Iris Versicolour', 'Iris Virginica', 'Iris Virginica', 
                                'Iris Setosa', 'Iris Versicolour', 'Iris Setosa', 'Iris Versicolour']
})
    return df

# Arrange
@pytest.fixture
def input_zscore():
    df = pd.DataFrame({ 'SepalLengthCm' : [5.1, 9, 6.5, 5.5, 6.7, 10.4, -54, 15, 5.2, 5.3, 5.1, 5.1, 4.9, 5.6, 6.5, 5.5, 6.7, 10.4, -55, 15, 5.2, 5.3, 5.1],
                        'SepalWidthCm' : [5.1, 9, 6.5, 5.5, 6.7, 10.4, 68, 15, 5.2, 5.3, 5.1, 5.1, 4.9, 5.6, 6.5, 5.5, 6.7, 10.4, 70, 15, 5.2, 5.3, 5.1],
                        'PetalWidthCm' :  [-40, 0.2, 0.2, 0.3, 0.2, 0.5, 0.5, 0.6, 0.4, 0.2, 5, 6, 7, 0.2, 0.2, 0.3, 0.2, 0.5, 0.5, 0.6, 0.4, 0.2, 5],
                        'RootLengthCm': [60, 0.2, 0.2, 0.3, 0.2, 0.5, 0.5, 0.6, 0.4, 0.2, 5, 6, 7, 0.2, 0.2, 0.3, 0.2, 0.5, 0.5, 0.6, 0.4, 0.2, 5],
                        'class': ['Iris Setosa', 'Iris Versicolour', 'Iris Virginica', 'Iris Setosa', 'Iris Versicolour', 'Iris Virginica', 'Iris Virginica', 
                                  'Iris Setosa', 'Iris Versicolour', 'Iris Setosa', 'Iris Versicolour', 'Iris Setosa', 'Iris Versicolour', 'Iris Virginica', 
                                  'Iris Setosa', 'Iris Versicolour', 'Iris Virginica', 'Iris Virginica', 'Iris Setosa', 'Iris Versicolour', 'Iris Setosa', 
                                  'Iris Versicolour', 'Iris Setosa']
                   })
    return df


# Arrange
@pytest.fixture
def summary_Zscore():
    compare_df = pd.DataFrame({'SepalLengthCm' : [2, '8.7%', 1.74, 5.5, 17.99, (-55.0, -54.0), np.nan],
                               'SepalWidthCm' :  [2, '8.7%', 12.48, 5.6, 18.08, np.nan, (68.0, 70.0)],
                               'PetalWidthCm' :  [1, '4.35%', -0.47, 0.4, 8.87, -40.0, np.nan],
                               'RootLengthCm' :  [1, '4.35%', 3.88, 0.4, 12.42, np.nan, 60.0]}, 
                               index=['outlier_count', 'outlier_percentage', 'mean', 'median', 'std', 'lower_range', 'upper_range'])
    return compare_df

# Arrange
@pytest.fixture
def summary_IQR():
    compare_df_iqr = pd.DataFrame({'SepalLengthCm' : [2, '18.18%', 13.71, 5.2, 18.96, np.nan, (50.0, 54.0)],
                                   'SepalWidthCm' :  [2, '18.18%', 0.07, 1.4, 2.83, (-5.7, -5.4), np.nan],
                                   'PetalWidthCm' :  [2, '18.18%', -2.9, 0.3, 12.38, -40.0, 5.0]}, 
                               index=['outlier_count', 'outlier_percentage', 'mean', 'median', 'std', 'lower_range', 'upper_range'])
    return compare_df_iqr

# Arrange
@pytest.fixture
def outlier_Zscore():
    compare_outlier_df = pd.DataFrame({'SepalLengthCm' : [5.1, 9, 6.5, 5.5, 6.7, 10.4, -54, 15, 5.2, 5.3, 5.1, 5.1, 4.9, 5.6, 6.5, 5.5, 6.7, 10.4, -55, 15, 5.2, 5.3, 5.1],
                                       'SepalWidthCm' : [5.1, 9, 6.5, 5.5, 6.7, 10.4, 68, 15, 5.2, 5.3, 5.1, 5.1, 4.9, 5.6, 6.5, 5.5, 6.7, 10.4, 70, 15, 5.2, 5.3, 5.1],
                                       'PetalWidthCm' :  [-40, 0.2, 0.2, 0.3, 0.2, 0.5, 0.5, 0.6, 0.4, 0.2, 5, 6, 7, 0.2, 0.2, 0.3, 0.2, 0.5, 0.5, 0.6, 0.4, 0.2, 5],
                                       'RootLengthCm': [60, 0.2, 0.2, 0.3, 0.2, 0.5, 0.5, 0.6, 0.4, 0.2, 5, 6, 7, 0.2, 0.2, 0.3, 0.2, 0.5, 0.5, 0.6, 0.4, 0.2, 5],
                                       'outlier': [True, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False]
                                  })
    return compare_outlier_df

# Arrange
@pytest.fixture
def outlier_IQR():
    compare_outlier_IQR_df = pd.DataFrame({'SepalLengthCm' : [5.2, 4.9, 4.7, 5.5, 5.1, 5.0, 6.0, 54, 50, 5.3, 5.1],
                                           'SepalWidthCm' :  [-5.4, 1.4, -5.7, 0.2, 0.7, 1.6, 1.2, 1.4, 1.8, 1.5, 2.1],
                                           'PetalWidthCm' :  [-40, 0.2, 0.2, 0.3, 0.2, 0.5, 0.5, 0.6, 0.4, 0.2, 5], 
                                           'outlier': [True, False, True, False, False, False, False, True, True, False, True]
                                  })  
    return compare_outlier_IQR_df               

def test_outlier_identifier(input_iqr, input_zscore, summary_Zscore, summary_IQR, outlier_Zscore, outlier_IQR):
    """
    Test existing functionalities of outlier_identifier(), which include
    returning a dataframe in the right format with input arguments as columns, identifier and return_df argument.
    6 tests in total.
    """

   # Tests whether data is not of dataframe raises TypeError
    with raises(TypeError, match=r"passed dataframe is of type list, should be DataFrame"):
        outlier_identifier([4, None, 4, 7])

   # Tests whether columns passed in incorrect type raises TypeError
    with raises(TypeError, match=r"passed columns is of type set, should be list or NoneType"):
        outlier_identifier(input_iqr, columns= {'SepalLengthCm'})

    # Tests whether return_df passed in incorrect type raises TypeError
    with raises(TypeError, match=r"passed return_df is of type str, should be bool with value as True or False"):
        outlier_identifier(input_iqr, return_df='True')

    # Tests whether if columns are None or type list
    with raises(TypeError, match=r"passed columns is of type set, should be list or NoneType"):
        outlier_identifier(input_iqr, columns={'SepalLengthCm'})

    # Tests whether if identifier is of type str
    with raises(TypeError, match=r"passed identifier is of type list, should be string with value 'Z_score' or 'IQR'"):
        outlier_identifier(input_iqr, columns=['SepalLengthCm'], identifier=['Z_score'])

    # Tests whether wrong identifier passed raises ValueError
    with raises(ValueError):
        outlier_identifier(input_iqr, columns= ['SepalLengthCm'], identifier='both')

    # Tests whether empty dataframe or dataframe with all NAN raises ValueError
    with raises(ValueError):
        outlier_identifier(pd.DataFrame(), columns= ['SepalLengthCm'])

    


    ## Unit test cases

    # Test if output with identifier = 'Z_score' and return_df = False (default) matches with expected output summary_Zscore 
    # (checks if condition - 1)
    assert_frame_equal(outlier_identifier(input_zscore, identifier='Z_score'), summary_Zscore), "The returned dataframe using outlier_identifier is not correct"

    # Test if output with identifier = 'Z_score' and return_df = True matches with expected output outlier_Zscore 
    # (checks if condition - 2)
    assert_frame_equal(outlier_identifier(input_zscore, identifier='Z_score', return_df=True), outlier_Zscore), "The returned dataframe using outlier_identifier is not correct"

    # Test if output with identifier = 'IQR' (default) and return_df = False (default) matches with expected output summary_IQR 
    # (checks if condition - 3)
    assert_frame_equal(outlier_identifier(input_iqr, identifier='IQR'), summary_IQR), "The returned dataframe using outlier_identifier is not correct"

    # Test if output with identifier = 'IQR' (default) and return_df = True matches with expected output outlier_IQR 
    # (checks if condition - 4)
    assert_frame_equal(outlier_identifier(input_iqr, identifier='IQR', return_df=True), outlier_IQR), "The returned dataframe using outlier_identifier is not correct"
    
    # Test if output has all numeric columns from the list of columns passed 
    assert outlier_identifier(input_iqr, columns=['SepalLengthCm', 'SepalWidthCm', 'class']).columns.tolist() == ['SepalLengthCm', 'SepalWidthCm'], "The columns returned in the dataframe is not correct"
