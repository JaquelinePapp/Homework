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

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.cluster import KMeans
from pandas.core.dtypes.dtypes import CategoricalDtype


def mean_jitter(val, mean, rand):
    if pd.isna(val):
        return mean + float(rand.randint(1, 100) / 10)
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

    for col in vgsales_copy.columns:
        if isinstance(vgsales_copy[col], CategoricalDtype):
            # Add an NA category to each categorical feature if required
            if "NA" not in vgsales_copy[col].cat.categories:
                vgsales_copy[col].cat.add_categories("NA", inplace=True)
            vgsales_copy[col].fillna("NA", inplace=True)
        else:
            vgsales_copy[col] = vgsales_copy[col].apply(mean_jitter,
                        mean = vgsales_copy[col].mean(),
                        rand=jittergen)


    #vgsales.Genre.dtypes.categories.append(pd.Index(catd))
    #isinstance(vgsales["Platform"].dtype, pd.core.dtypes.dtypes.CategoricalDtype)

    #onehot =

def preprocess_vgsales(vgsales):
    pass

def linear_regression(vgsales):

    reg = LinearRegression()
    X = vgsales["Metacritic"].values.reshape(-1, 1)
    Y = vgsales["Sales"].values.reshape(-1, 1)
    reg.fit(X, Y)  #perform linear regression
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
