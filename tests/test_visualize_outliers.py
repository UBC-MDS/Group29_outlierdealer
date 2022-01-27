from cmath import nan
from py_outlier_utils.visualize_outliers import visualize_outliers
import pandas as pd
import numpy as np
from pytest import raises
import altair as alt

def df():

    df = pd.DataFrame({"a":np.random.normal(100, 30, 100),
                  "b":np.random.normal(8, 5, size=100),
                  "c":np.random.randint(100, size=100),
                 "d":["A","B", "C", "D"] * 25})

    return df

def test_output_columns():

    ## Test the used columns of function result
    assert visualize_outliers(df(), columns = ['a']).data.variable.unique() == ['a'], 'Given columns should be mapped to the facet.'

def test_output_chart():

    ## Test the type of function result
    output_t = visualize_outliers(df(), columns = ['a', 'b', 'd'], type='violin')
    assert isinstance(
        output_t, alt.vegalite.v4.api.FacetChart
    ), "Altair Facet Chart object should be returned."

def test_output_type():

    ## Test the type of function result
    assert visualize_outliers(df(), type='violin').columns == 5, 'Return chart is not of the given type.'

def test_invalid_df():
    ## Test the exceptions of invalid input
    with raises(TypeError):
        visualize_outliers("572")

def test_invalid_df_non():
    ## Test the exceptions of invalid input
    dfn = pd.DataFrame({"a":[nan, nan],
    "b":[1,2]})
    with raises(ValueError):
        visualize_outliers(dfn)

def test_invalid_col():
    with raises(TypeError):
        visualize_outliers(df(), column = "gsgs")

def test_invalid_type():
    with raises(ValueError):
        visualize_outliers(df(), type='scatter')
        