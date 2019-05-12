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


def review_sales_hexbins(vgsales):
    """
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
                             ylabel="Global sales")
    hexgraph.ax_joint.set_title("Sales by review scores")

    plt.show()

    return hexgraph
