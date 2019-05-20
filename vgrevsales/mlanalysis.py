# -*- coding: utf-8 -*-

# =============================================================================
# SOC 765 | Introduction to Computational Social Science
# Spring 2019
# Project II
# Names: Jaqueline Papp and Joshua Megnauth
# (Working) Project Title: Do review scores affect video game sales?
# =============================================================================

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from pandas.core.dtypes.dtypes import CategoricalDtype
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import RobustScaler
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.cluster import KMeans


def mean_jitter(val, mean, quantdiff, rand):
    """
    The function mean_jitter is designed to be a callback for DataFrame.apply()
    that replaces nulls with the column mean plus some noise/jitter.

    :param val: The value passed in from DataFrame.apply().
    :mean: The column mean.
    :rand: A numpy.random.RandomState object.
    """
    if pd.isna(val):
        return mean + float(rand.randint(-1 * quantdiff, quantdiff))
    else:
        return val


def pre_preprocess_features(vgsales):
    """
    """
    # We explictly want to work with a copy here.
    vgsales_copy = vgsales.copy()
    # Turn ESRB into a ordinal variable (type: Int64 now).
    vgsales_copy.ESRB = vgsales.ESRB.factorize(True)[0]
    # Random generator for mean jitter
    jittergen = np.random.RandomState(42)

# =============================================================================
#     Here, we'll loop through each column to impute missing values.
#     Some features are more complete than others. Categorical features are
#     largely complete and also hard to impute, so we simply replace nulls with
#     "NA." Numerical features are imputed with jitter based on the difference
#     between the 75th and 25th quantiles.
# =============================================================================

    for col in vgsales_copy.columns:
        if isinstance(vgsales_copy[col].dtype, CategoricalDtype):
            # Add an NA category to each categorical feature if required...
            if "NA" not in vgsales_copy[col].cat.categories:
                vgsales_copy[col].cat.add_categories("NA", inplace=True)
            # ...and fill nulls with "NA."
            vgsales_copy[col].fillna("NA", inplace=True)
        else:
            # print("Col: {0} Type: {1}".format(col, vgsales_copy[col].dtype))
            vgsales_copy[col] = vgsales_copy[col].apply(
                    mean_jitter,
                    mean=vgsales_copy[col].mean(),
                    quantdiff=vgsales_copy[col].quantile(.75) -
                    vgsales_copy[col].quantile(.25),
                    rand=jittergen)

    return vgsales_copy


def preprocess_vgsales(vgsales_nonulls):
    """
    """
    # pandas.get_dummies() is like sklearn's OneHotEncoder except easier to use
    # because it doesn't return a matrix.
    vgdummies = pd.get_dummies(vgsales_nonulls)
    vgdummies.drop("Metacritic_N", axis="columns", inplace=True)

# =============================================================================
#     According to the sklearn documents, a RobustScaler is better to use for
#     data with many outliers. We fit and transform our dataset after creating
#     dummy variables. Scikit-learn returns NumPy arrays, thus we recreate a
#     Pandas DataFrame using the scaled matrix with the columns from vgdummies.
#
#     You may wonder why we didn't make a pipeline. We can reuse our scaled
#     variable for other ML algorithms. I'm not sure if that's possible with
#     a pipeline. And there's no time to try.
#
#     Source: https://scikit-learn.org/stable/modules/preprocessing.html
# =============================================================================

    vgscaled = RobustScaler().fit_transform(vgdummies)
    vgscaled = pd.DataFrame(vgscaled, columns=vgdummies.columns)

    return vgscaled


def linear_regression(vgsales):
    """
    """
    # X: Everything BUT Sales
    # y: Sales
    X_train, X_test, y_train, y_test = train_test_split(
            vgsales.loc[:, vgsales.columns != "Sales"],
            vgsales[["Sales"]],
            test_size=.3,
            random_state=42)

    ridge_param = {"alpha": np.append(np.array(range(1, 11))/10,
                                      np.array(range(0, 55, 5)))}

    ridge_gridsearch = GridSearchCV(Ridge(),
                                    ridge_param,
                                    scoring="neg_mean_squared_error",
                                    n_jobs=-1,
                                    cv=10)

    ridge_gridsearch.fit(X_train, y_train)

    reg = LinearRegression()
    X = vgsales["Metacritic"].values.reshape(-1, 1)
    Y = vgsales["Sales"].values.reshape(-1, 1)
    reg.fit(X, Y)
    Y_pred = reg.predict(X)


    scatter = plt.scatter(X, Y)
    plt.title('Linear Regression')
    plt.yscale('log')
    plt.plot(X, Y_pred, color='red')
    plt.show()

    return scatter


def K_Means(vgsales):

    df = pd.DataFrame(vgsales.filter(['Metacritic', 'Sales']))
    kmeans = KMeans(n_clusters=3).fit(df)
    centroids = kmeans.cluster_centers_
    print(centroids)

    kscatter = plt.scatter(df['Metacritic'], df['Sales'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
    plt.ylim(0, 10)
    plt.show()

    return kscatter
