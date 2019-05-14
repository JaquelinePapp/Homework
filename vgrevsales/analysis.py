# -*- coding: utf-8 -*-

# =============================================================================
# SOC 765 | Introduction to Computational Social Science
# Spring 2019
# Project II
# Names: Jaqueline Papp and Joshua Megnauth
# (Working) Project Title: Do review scores affect video game sales?
# =============================================================================

# =============================================================================
# Notes:
# https://stackoverflow.com/questions/13851535/how-to-delete-rows-from-a-pandas-dataframe-based-on-a-conditional-expression
#
# Get gen 3/4.
#
# Use groupby.
# =============================================================================

import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.distributions.empirical_distribution import ECDF


def review_sales_hexbins(vgsales):
    """
    Creates and returns a hexbin plot of video game sales distributed over
    Metacritic scores.

    :param vgsales: DataFrame of the Video_Games_Sales_as_at_22_Dec_2016
    dataset or equivalent.
    """
# =============================================================================
#     A hexbins plot was the most fruitful EDA for this data. Scores (x) and
#     sales (y) consist of thousands of observations, most of which are very
#     clustered within a certain range. A hexbins plot captures this data
#     well with deeper hues (or higher luminosity) representing particularly
#     busy intersections between score/sales.
#
#     We used a logarithmic y scale because of the large range of y values.
# =============================================================================

    hexgraph = sns.jointplot("Metacritic", "Sales", vgsales, "hex", height=10,
                             joint_kws={"yscale": "log", "bins": "log",
                                        "cmap": "viridis"})

    # Titles and labels
    hexgraph.set_axis_labels(xlabel="Metacritic review scores",
                             ylabel="Global sales (millions)")

    hexgraph.ax_marg_x.set_title("Sales by review scores")

    plt.show()

    return hexgraph


def genre_sales_boxen(vgsales, sizex=10, sizey=10):
    """
    Creates and returns a boxen categorical plot of sales by video game genre.

    :param vgsales: DataFrame of the Video_Games_Sales_as_at_22_Dec_2016
    dataset or equivalent.

    :param sizex: Size in inches(?) of the width of the plot.

    :param sizey: Size in inches(?) of the height of the plot.
    """
    gensales = sns.catplot("Genre", "Sales", data=vgsales, kind="boxen")

    # We use a logarithmic y scale due to the range of y values.
    # The figure size is debatable, but the plot looks weird when it's smaller.

    gensales.set_xticklabels(rotation=45)
    gensales.ax.set_yscale("log")
    gensales.fig.set_size_inches(sizex, sizey, forward=True)

    gensales.ax.set_title("Game sales distributed by genre")
    gensales.set_axis_labels(y_var="Global sales (millions)")

    plt.show()

    return gensales


def sales_review_ecdf(vgsales):
    """
    ECDF
    """
    rev_ecdf = ECDF(vgsales.Metacritic)
    sales_ecdf = ECDF(vgsales.Sales)
    fig, ax = plt.subplots()
    ax.set_ylabel("ECDF")

    sns.lineplot(rev_ecdf.x, rev_ecdf.y, ax=ax)
    ax.set_xlabel("Review probability (0 to 100)")

    twin_y = ax.twiny()
    sns.lineplot(sales_ecdf.x, sales_ecdf.y, ax=twin_y)
    twin_y.set_xlabel("Sales probability (millions)")

    plt.show()
