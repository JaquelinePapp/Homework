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
    hexgraph = sns.jointplot("Metacritic", "Sales", vgsales, "hex", height=10,
                             kwargs={"yscale": "log", "bins": "log",
                                     "cmap": "viridis"})

    hexgraph.set_axis_labels(xlabel="Metacritic review scores",
                             ylabel="Global sales")
    hexgraph.ax_joint.set_title("Sales by review scores")

    plt.show()

    return hexgraph