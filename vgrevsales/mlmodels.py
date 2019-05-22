# -*- coding: utf-8 -*-

# =============================================================================
# SOC 765 | Introduction to Computational Social Science
# Spring 2019
# Project III
# Names: Jaqueline Papp and Joshua Megnauth
# Project Title: Do review scores affect video game sales?
# =============================================================================

from scipy.stats import chisquare
from mlanalysis import pre_preprocess_features
from mlanalysis import preprocess_vgsales
from mlanalysis import ridge_model
from mlanalysis import plot_ridge_model
from mlanalysis import knn_model


def chisquare_all(vgsales):
    vg_imputed = pre_preprocess_features(vgsales)
    return chisquare(vg_imputed, axis=None)


def chisquare_salesmeta(vgsales):
    return chisquare(vgsales[["Metacritic", "Sales"]].dropna(), axis=None)


def all_features_ridgemodel(vgsales):
    """
    """
    vg_imputed = pre_preprocess_features(vgsales)
    vg_preproc = preprocess_vgsales(vg_imputed)

    return plot_ridge_model(*ridge_model(vg_preproc))


def drop_nulls_ridgemodel(vgsales):
    """
    """
    vg_scaled = preprocess_vgsales(vgsales.dropna())
    return plot_ridge_model(*ridge_model(vg_scaled[["Metacritic", "Sales"]]))


def drop_nulls_knnmodel(vgsales):
    """
    """
    vg_scaled = preprocess_vgsales(vgsales.dropna())
    return knn_model(vg_scaled[["Sales"]].values.reshape(-1))
