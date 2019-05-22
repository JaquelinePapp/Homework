# -*- coding: utf-8 -*-

# =============================================================================
# SOC 765 | Introduction to Computational Social Science
# Spring 2019
# Project III
# Names: Jaqueline Papp and Joshua Megnauth
# Project Title: Do review scores affect video game sales?
# =============================================================================

from argparse import ArgumentParser
import sys

from loadprep import loadprep_vgsales
from loadprep import clean_features
from loadprep import set_seaborn_opts
from descriptivestats import print_descriptive
from analysis import review_sales_hexbins
from analysis import genre_sales_boxen
from analysis import review_sales_ecdf
from mlmodels import chisquare_salesmeta
from mlmodels import all_features_ridgemodel
from mlmodels import drop_nulls_ridgemodel


def parse_args():
    """
    This function handles arguments passed into the script when run.
    """

    varargsparser = ArgumentParser()
    varargsparser.add_argument("-v", "--vgsales",
                               help="Path to a dataset compatible with "
                               "Video_Games_Sales_as_at_22_Dec_2016.csv")

    # Set a default path if vgsales is null
    varargs = varargsparser.parse_args()

    if not varargs.vgsales:
        varargs.vgsales = "Video_Games_Sales_as_at_22_Dec_2016.csv"

    return varargs


if __name__ == "__main__":
    vgsales = None

    try:
        arguments = parse_args()
        vgsales = loadprep_vgsales(arguments.vgsales)
        clean_features(vgsales)
    except (ValueError, FileNotFoundError) as e:
        sys.exit("Error {0}: Unable to load the required dataset. Tried: {1}\n"
                 "You may pass in a path using the --vgsales or -v "
                 "switches if the dataset is in another directory."
                 .format(e.errno, arguments.vgsales))

    # Now that that's out of the way, we can run all of our projects' functions
    # here. This is temporary for the submission.
    set_seaborn_opts()
    print_descriptive(vgsales)
    review_sales_hexbins(vgsales)
    genre_sales_boxen(vgsales)
    review_sales_ecdf(vgsales)
    all_features_ridgemodel(vgsales)
    drop_nulls_ridgemodel(vgsales)
