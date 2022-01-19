# from outliers import outliers
import pandas as pd
from pandas._testing import assert_frame_equal
import numpy as np
from pytest import raises
from outliers.outliers import outlier_identifier

# Arrange
@pytest.fixture
def input():
    df = pd.DataFrame({ 'SepalLengthCm' : [5.1, 4.9, 4.7, 5.5, 5.1, 50, 54, 5.0, 5.2, 5.3, 5.1],
                        'SepalWidthCm' :  [1.4, 1.4, 20, 2.0, 0.7, 1.6, 1.2, 1.4, 1.8, 1.5, 2.1],
                        'PetalWidthCm' :  [0.2, 0.2, 0.2, 0.3, 0.4, 0.5, 0.5, 0.6, 0.4, 0.2, 5],
                        'class': ['Iris Setosa', 'Iris Versicolour', 'Iris Virginica', 'Iris Setosa', 'Iris Versicolour', 'Iris Virginica', 'Iris Virginica', 
                                'Iris Setosa', 'Iris Versicolour', 'Iris Setosa', 'Iris Versicolour']
})

# Arrange
@pytest.fixture
def summary_Zscore():
    compare_df = pd.DataFrame({'SepalLengthCm' : [0, '0.0%', 13.63, 5.1, 18.99, np.nan, np.nan],
                               'SepalWidthCm' :  [1, '9.09%', 3.19, 1.5, 5.59, np.nan, 20.0],
                               'PetalWidthCm' :  [0, '0.0%', 0.77, 0.4, 1.41, np.nan, np.nan]}, 
                               index=['outlier_count', 'outlier_percentage', 'mean', 'median', 'std', 'lower_range', 'upper_range'])

# Arrange
@pytest.fixture
def summary_IQR():
    compare_df_iqr = pd.DataFrame({'SepalLengthCm' : [2, '18.18%', 13.63, 5.1, 18.99, np.nan, (50.0, 54.0)],
                                   'SepalWidthCm' :  [1, '9.09%', 3.19, 1.5, 5.59, np.nan, 20.0],
                                   'PetalWidthCm' :  [1, '9.09%', 0.77, 0.4, 1.41, np.nan, 5.0]}, 
                               index=['outlier_count', 'outlier_percentage', 'mean', 'median', 'std', 'lower_range', 'upper_range'])

# Arrange
@pytest.fixture
def outlier_Zscore():
    compare_outlier_df = pd.DataFrame({'SepalLengthCm' : [5.1, 4.9, 4.7, 5.5, 5.1, 50, 54, 5.0, 5.2, 5.3, 5.1],
                                       'SepalWidthCm' :  [1.4, 1.4, 20, 2.0, 0.7, 1.6, 1.2, 1.4, 1.8, 1.5, 2.1],
                                       'PetalWidthCm' :  [0.2, 0.2, 0.2, 0.3, 0.4, 0.5, 0.5, 0.6, 0.4, 0.2, 5], 
                                       'outlier': [False, False, True, False, False, False, False, False, False, False, False]
                                  })

# Arrange
@pytest.fixture
def outlier_IQR():
    compare_outlier_IQR_df = pd.DataFrame({'SepalLengthCm' : [5.1, 4.9, 4.7, 5.5, 5.1, 50, 54, 5.0, 5.2, 5.3, 5.1],
                                           'SepalWidthCm' :  [1.4, 1.4, 20, 2.0, 0.7, 1.6, 1.2, 1.4, 1.8, 1.5, 2.1],
                                           'PetalWidthCm' :  [0.2, 0.2, 0.2, 0.3, 0.4, 0.5, 0.5, 0.6, 0.4, 0.2, 5], 
                                           'outlier': [False, False, True, False, False, True, True, False, False, False, True]
                                  })                  

def test_outlier_identifier(input, summary_Zscore, summary_IQR, outlier_Zscore, outlier_IQR):
    """
    Test existing functionalities of outlier_identifier(), which include
    returning a dataframe in the right format with input arguments as columns, identifier and return_df argument.
    6 tests in total.
    """

    # Exception Handling test cases

    # Tests whether data is not of dataframe raises TypeError
    with raises(TypeError):
        outlier_identifier([4, None, 4, 7])

    # Tests whether columns passed in incorrect type raises TypeError
    with raises(TypeError):
        outlier_identifier(input, columns= {'SepalLengthCm'})

    # Tests whether return_df passed in incorrect type raises TypeError
    with raises(TypeError):
        outlier_identifier(input, return_df='True')

    # Tests whether wrong identifier passed raises ValueError
    with raises(ValueError):
        outlier_identifier(input, columns= ['SepalLengthCm'], identifier='both')
