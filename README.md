# py_outlier_utils

## Overview
As data rarely comes ready to be used and analyzed for machine learning right away, this package aims to help speed up the process of cleaning and doing initial exploratory data analysis specific to outliers. The package focuses on the tasks of identifying univariate outliers, providing summary of outliers like count, range of outliers, visualize them and giving functionality to remove them from data.

## Installation

```bash
$ pip install py_outlier_utils
```

## Functions
The three functions contained in this package are as follows:

- `outlier_identifier`: A function to identify outliers in the dataset and provide their summary as an output
- `visualize_outliers`: A function to generate the eda plots highlighting outliers providing additional functionality to visualize them
- `drop_outliers`: A function to generate outlier free dataset.

## Our Place in the Python Ecosystem
While Python packages with similar functionalities exist, this package aims to provide summary, visualization of outliers in a single package with an additional functionality to generate outlier-free dataset. Few packages with similar functionality are as follows:

- [pyod](https://pypi.org/project/pyod/)
- [python-outlier](https://pypi.org/project/python-outlier/)

## Usage

- TODO

## Contributing

This package is authored by Karanpreet Kaur, Linhan Cai, Qingqing Song as part of the course project in DSCI-524 (UBC-MDS program). You can see the list of all contributors in the contributors tab.

We welcome and recognize all contributions. If you wish to participate, please review our [Contributing guidelines](CONTRIBUTING.md)

## License

`py_outlier_utils` is licensed under the terms of the MIT license.

## Credits

`py_outlier_utils` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
