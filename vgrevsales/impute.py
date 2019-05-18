# -*- coding: utf-8 -*-

# =============================================================================
# SOC 765 | Introduction to Computational Social Science
# Spring 2019
# Project II
# Names: Jaqueline Papp and Joshua Megnauth
# (Working) Project Title: Do review scores affect video game sales?
# =============================================================================

import pandas.core.dtypes.dtypes as pdtypes


def impute_vgsales_features(vgsales):
    for col in vgsales.columns:
        if isinstance(vgsales[col], pdtypes.CategoricalDtype):
            pass
        else: # float64, Int64
            pass
