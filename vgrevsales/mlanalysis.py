# -*- coding: utf-8 -*-

# =============================================================================
# SOC 765 | Introduction to Computational Social Science
# Spring 2019
# Project II
# Names: Jaqueline Papp and Joshua Megnauth
# (Working) Project Title: Do review scores affect video game sales?
# =============================================================================

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.cluster import KMeans

def pre_preprocess_features(vgsales):
    """
    """
    # Oh dear, this is a mess.
    vgsales_copy = vgsales.copy()
    vgsales_copy.ESRB = vgsales.ESRB.factorize(True)[0]



    #vgsales.Genre.dtypes.categories.append(pd.Index(catd))
    #isinstance(vgsales["Platform"].dtype, pd.core.dtypes.dtypes.CategoricalDtype)

    #onehot =

def preprocess_vgsales(vgsales):
    for x in range(1984, 2017):
        vgsales[vgsales.Release == x].info()