from py_outlier_utils.outliers import visualize_outliers
import pandas as pd
import numpy as np
import pytest
import altair as alt

def df():

    df =df = pd.DataFrame({"a":np.random.normal(100, 30, 100),
                  "b":np.random.normal(8, 5, size=100),
                  "c":np.random.randint(100, size=100),
                 "d":["A","B", "C", "D"] * 25})

    return df

def test_visualize_outliers():

    ## Test the type of return
    result = visualize_outliers(df, columns = ['a', 'b', 'd'], type='violin')
    assert isinstance(
        result, alt.vegalite.v4.api.FacetChart
    ), "Altair Chart object should be returned."

    ## Test the exceptions of invalid input
    with pytest.raises(Exception):
        visualize_outliers([5, 7, 2])

    with pytest.raises(Exception):
        visualize_outliers(df(), column = "gsgs")

    with pytest.raises(Exception):
        visualize_outliers(df(), type='scatter')
        