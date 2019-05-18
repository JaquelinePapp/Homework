# -*- coding: utf-8 -*-

# =============================================================================
# SOC 765 | Introduction to Computational Social Science
# Spring 2019
# Project II
# Names: Jaqueline Papp and Joshua Megnauth
# (Working) Project Title: Do review scores affect video game sales?
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

    hexgraph.ax_marg_x.set_title("Sales by review scores", weight="bold")

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

    gensales.ax.set_title("Game sales distributed by genre", weight="bold")
    gensales.set_axis_labels(y_var="Global sales (millions)")

    plt.show()

    return gensales


def review_sales_ecdf(vgsales, sizex=10, sizey=10):
    """
    Plots ECDFs for review scores and sales on the same axes.

    :param vgsales: DataFrame of the Video_Games_Sales_as_at_22_Dec_2016
    dataset or equivalent.

    :param sizex: Size in inches(?) of the width of the plot.

    :param sizey: Size in inches(?) of the height of the plot.
    """
    fig, ax = plt.subplots()
    fig.set_size_inches(sizex, sizey, forward=True)

    # Review ECDF and plot
    rev_ecdf = ECDF(vgsales.Metacritic)
    sns.lineplot(rev_ecdf.x, rev_ecdf.y, color="firebrick", label="Reviews",
                 linestyle="--", marker="D", ax=ax)

    # Sales ECDF and plot (shares y axis with ECDF above)
    twin_y = ax.twiny()
    twin_y.set_xscale("log")

    sales_ecdf = ECDF(vgsales.Sales)
    sns.lineplot(sales_ecdf.x, sales_ecdf.y, label="Sales", color="slateblue",
                 linestyle="-.", marker="o", ax=twin_y)

# =============================================================================
#     Labels, legend, and title for both plots
# =============================================================================
    ax.set_title("ECDF review averages and sales", weight="bold")
    ax.set_ylabel("ECDF")
    ax.set_xlabel("Review probability (0 to 100)")
    twin_y.set_xlabel("\nSales probability (millions)")

    # The per Axes legends overlap with the plots, so we remove both and set
    # a Figure legend which uses each label from every line object in each
    # Axes
    ax.get_legend().remove()
    twin_y.get_legend().remove()
    fig.legend(loc=2, bbox_to_anchor=(1, 1))  # Fix later

    plt.show()

    return fig, ax
