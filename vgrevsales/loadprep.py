# -*- coding: utf-8 -*-

# =============================================================================
# SOC 765 | Introduction to Computational Social Science
# Spring 2019
# Project II
# Names: Jaqueline Papp and Joshua Megnauth
# (Working) Project Title: Do review scores affect video game sales?
# =============================================================================

import pandas as pd


def loadprep_vgsales(path):
    """
    This function's sole purpose is to clean Rush Kirubi's video game sales
    and reviews dataset from Kaggle for Jaqueline and Josh's class project.

    Source: https://www.kaggle.com/rush4ratio/video-game-sales-with-ratings
    File: Video_Games_Sales_as_at_22_Dec_2016.csv

    We don't use regional sales as they're not useful for our purposes.
    The features 'User_Score' and 'User_Count' are the non-critic, user scores
    from Metacritic. These features aren't used as they're rather low quality
    data. Review bombs and overly positive/negative reviews coupled with a low
    N means that the data isn't too useful to us. Furthermore, Metacritic
    is only one site whereas many video game review sites have their own
    user reviews.

    :param path: A path to a Video_Games_Sales_as_at_22_Dec_2016.csv compatible
    dataset as noted above.
    """

    # These are the columns to keep.
    columns_to_use = ["Name", "Platform", "Year_of_Release", "Genre",
                      "Publisher", "Global_Sales", "Critic_Score",
                      "Critic_Count", "Developer", "Rating"]

# =============================================================================
#     We specifically cast some of the strings/objects to categorical variables
#     as categorical variables are more efficient to use as well as the proper
#     variable type. The original column names must be used here.
#
#     Note on Int64:
#     Int64 is an impermanent name according to the following source.
#     https://pandas.pydata.org/pandas-docs/version/0.24/whatsnew/v0.24.0.html
#
#     Note on Index type:
#     The read_csv function does not typecast indexes appropriately.
#     However, this is a minor concern so we shouldn't refactor to use
#     astype instead.
#     https://github.com/pandas-dev/pandas/issues/9435
# =============================================================================
    columns_typecast = {"Platform": "category",
                        "Genre": "category",
                        "Publisher": "category",
                        "Developer": "category",
                        "Rating": "category",
                        "Critic_Score": "float64",
                        "Critic_Count": "Int64",
                        "Year_of_Release": "Int64",
                        "Name": str}

    # This seemed like a good idea at the time but now I don't know.
    columns_new_names = {"Year_of_Release": "Release",
                         "Global_Sales": "Sales",
                         "Critic_Score": "Metacritic",
                         "Critic_Count": "Metacritic_N",
                         "Rating": "ESRB"}

    # DataFrame.rename() is used here because the 'names' argument
    # doesn't seem to work if we select specific columns.
    # axis="columns" is specified because the documentation says to be specific
    return (pd.read_csv(path, index_col="Name", usecols=columns_to_use,
                        dtype=columns_typecast)
            .rename(columns_new_names, axis="columns"))


def year_range_vgsales(vgsales, begin=2005, end=2016):
    """
    This function will further clean up vgsales then return a tuple of useful,
    reusable observations. Currently it returns a slice from 'begin' to 'end'
    in terms of years. Will return other stuff later.
    The notes for the dataset states that it ends at 2016, but there seems to
    be noise after 2016.
    """
    years = vgsales.loc[(vgsales.Release >= begin) & (vgsales.Release <= end)]

    mfivemil = years.loc[years.Sales > 5]
    lfivemil = years.loc[years.Sales < 5]
    ltwomil = years.loc[years.Sales < 2]

    return (years, mfivemil, lfivemil, ltwomil)
