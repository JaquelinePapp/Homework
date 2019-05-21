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
import seaborn as sns

from pandas.core.dtypes.dtypes import CategoricalDtype
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import PowerTransformer
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import explained_variance_score

from sklearn.linear_model import Ridge
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier


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

    vgscaled = PowerTransformer().fit_transform(vgdummies)
    vgscaled = pd.DataFrame(vgscaled, columns=vgdummies.columns)

    return vgscaled


def ridge_model(vgscaled):
    """
    """
    # X: Everything BUT Sales
    # y: Sales
    X_train, X_test, y_train, y_test = train_test_split(
            vgscaled.loc[:, vgscaled.columns != "Sales"],
            vgscaled[["Sales"]],
            test_size=.3,
            random_state=42)

    ridge_param = {"alpha": np.array(range(0, 11))/10,
                   "tol": [.001, .00001]}

    ridge_gridsearch = GridSearchCV(Ridge(random_state=42,
                                          fit_intercept=False),
                                    ridge_param,
                                    scoring="neg_mean_squared_error",
                                    n_jobs=-1,
                                    cv=10)

    ridge_gridsearch.fit(X_train, y_train)

    return ridge_gridsearch, vgscaled, X_train, X_test, y_train, y_test


def plot_ridge_model(model, vgscaled, X_train, X_test, y_train,
                     y_test, sizex=14, sizey=14):
    """
    """
    # Titles, labels, and pyplot objects
    fig, ax = plt.subplots()
    fig.set_size_inches(sizex, sizey, forward=True)
    ax.set_title("Ridge regression: Metacritic scores and game sales",
                 weight="bold")
    ax.set_xlabel("Metacritic review averages (normalized)")
    ax.set_ylabel("Sales (normalized)")

    # Plots
    sns.scatterplot(X_train.Metacritic, y_train.Sales, color="deepskyblue",
                    label="Training set", ax=ax)
    sns.scatterplot(X_test.Metacritic, y_test.Sales, color="slateblue",
                    label="Sales (true)", ax=ax)
    y_pred = model.predict(X_test)
    sns.scatterplot(X_test.Metacritic, y_pred.reshape(-1), color="crimson",
                    label="Sales (prediction)", ax=ax)

    # Text box for model information
# =============================================================================
#     coef_df = pd.DataFrame(model.best_estimator_.coef_,
#                            columns=vgscaled.drop("Sales", axis=1).columns)
# =============================================================================

    model_text = ("MSE: {0}\n"
                  "r^2: {1}\n"
                  "explained variance: {2}"
                  .format(mean_squared_error(y_test, y_pred),
                          r2_score(y_test, y_pred),
                          explained_variance_score(y_test, y_pred)))

    ax.text(.015, .89, model_text, transform=ax.transAxes, fontsize=12,
            verticalalignment="top", bbox={"boxstyle": "round", "alpha": .5,
                                           "facecolor": "lightcyan"})

    plt.show()

    return fig, ax


def knn_model(vgscaled):
    """
    """
    # X: Everything BUT Sales
    # y: Sales
    X_train, X_test, y_train, y_test = train_test_split(
            vgscaled.loc[:, vgscaled.columns != "Sales"],
            vgscaled[["Sales"]],
            test_size=.3,
            random_state=42)

    knn_param = {"n_neighbors": list(range(1, 33)),
                 "weights": ["uniform", "distance"]}

    knn_gridsearch = GridSearchCV(KNeighborsClassifier(n_jobs=-1),
                                  knn_param,
                                  scoring="accuracy",
                                  n_jobs=-1,
                                  cv=10)

    knn_gridsearch.fit(X_train, y_train)

    return knn_gridsearch, vgscaled, X_train, X_test, y_train, y_test


def plot_knn_model(model, vgscaled, X_train, X_test, y_train, y_test,
                   sizex=14, sizey=14):
    """
    """

    fig, ax = plt.subplots()
    ax.set_title("kNN", weight="bold")
    ax.set_size_inces(sizex, sizey, forward=True)
