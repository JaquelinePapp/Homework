# -*- coding: utf-8 -*-

# =============================================================================
# SOC 765 | Introduction to Computational Social Science
# Spring 2019
# Project III
# Names: Jaqueline Papp and Joshua Megnauth
# Project Title: Do review scores affect video game sales?
# =============================================================================

import pandas as pd
import seaborn as sns


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


def clean_features(vgsales):
    """
    This function cleans up some of the dataset's features. The dataset is
    quite messy as many values are missing from both categorical and numerical
    features. Many of these features are difficult to impute in a reasonable
    manner.

    <class 'pandas.core.frame.DataFrame'>
    Index: 16719 entries, Wii Sports to Winning Post 8 2016
    Data columns (total 9 columns):
    Platform        16719 non-null category
    Release         16450 non-null Int64
    Genre           16717 non-null category
    Publisher       16665 non-null category
    Sales           16719 non-null float64
    Metacritic      8137 non-null float64
    Metacritic_N    8137 non-null Int64
    Developer       10096 non-null category
    ESRB            9950 non-null category
    dtypes: Int64(2), category(5), float64(2)
    memory usage: 1.5+ MB

    Some of the hardest features to impute (genre or platform, for example)
    don't have many nulls. Others, like the review averages, can be imputed.

    :param path: A path to a Video_Games_Sales_as_at_22_Dec_2016.csv compatible
    dataset.
    """

    # A few of the release years are set to 2020 or other years past 2016.
    # Just setting them to 2016 here. They're not a lot of them anyway.
    vgsales.Release.loc[vgsales.Release > 2016] = 2016

# =============================================================================
#     https://en.wikipedia.org/wiki/Entertainment_Software_Rating_Board
#
#     The ESRB feature will be converted to an ordinal variable for machine
#     learning during preprocessing later. Thus, we organize them here and
#     add an NA for missing values.
# =============================================================================

    esrb_ordinal = ["NA", "RP", "EC", "E", "E10+", "T", "M", "AO"]
    vgsales.ESRB.cat.set_categories(esrb_ordinal, True, False, True)

    return vgsales


def set_seaborn_opts():
    sns.set(style="ticks", font_scale=1.25)
    sns.despine()
