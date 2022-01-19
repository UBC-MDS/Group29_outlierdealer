from outliers.visualize_outliers import visualize_outliers
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

def test_visualize_outliers():

    ## Test the type of function result
    dft = visualize_outliers(df(), columns = ['a', 'b', 'd'], type='violin')
    assert isinstance(
        dft, alt.vegalite.v4.api.FacetChart
    ), "Altair Chart object should be returned."

    ## Test the exceptions of invalid input
    with raises(TypeError):
        visualize_outliers("572")

    with raises(TypeError):
        visualize_outliers(df(), column = "gsgs")

    with raises(ValueError):
        visualize_outliers(df(), type='scatter')
        