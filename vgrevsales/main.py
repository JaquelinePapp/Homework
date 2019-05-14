# -*- coding: utf-8 -*-

# =============================================================================
# SOC 765 | Introduction to Computational Social Science
# Spring 2019
# Project II
# Names: Jaqueline Papp and Joshua Megnauth
# (Working) Project Title: Do review scores affect video game sales?
# =============================================================================

from argparse import ArgumentParser

from loadprep import loadprep_vgsales
from loadprep import year_range_vgsales
from loadprep import set_seaborn_opts
from descriptivestats import print_descriptive
from analysis import review_sales_hexbins
from analysis import genre_sales_boxen


def parse_args():
    """
    """

    varargsparser = ArgumentParser()
    varargsparser.add_argument("-vgsales",
                               help="Path to a dataset compatible with "
                               "Video_Games_Sales_as_at_22_Dec_2016.csv")

    # Set a default path if vgsales is null
    varargs = varargsparser.parse_args()

    if not varargs.vgsales:
        varargs.vgsales = "Video_Games_Sales_as_at_22_Dec_2016.csv"

    return varargs


def main_error_handler(e, path):
    print("Error: Unable to load the required dataset. Tried: {0}"
          .format(path))

    print("Python error: {0}".format(e))


if __name__ == "__main__":
    vgsales = None

    try:
        arguments = parse_args()
        vgsales = loadprep_vgsales(arguments.vgsales)
    except ValueError as e:
        main_error_handler(e, arguments.vgsales)
    except FileNotFoundError as e:
        main_error_handler(e, arguments.vgsales)

    # Now that that's out of the way, we can run all of our projects' functions
    # here.
    set_seaborn_opts()
    print_descriptive(vgsales)
    review_sales_hexbins(vgsales)
    genre_sales_boxen(vgsales)
