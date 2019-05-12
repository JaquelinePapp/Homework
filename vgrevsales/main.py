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
from descriptivestats import print_descriptive
from analysis import review_sales_hexbins


def parse_args():
    """
    """
    varargs = ArgumentParser()

    varargs.add_argument("-vgsales", help="Path to a dataset compatible with "
                         "Video_Games_Sales_as_at_22_Dec_2016.csv")

    return varargs.parse_args()


if __name__ == "__MAIN__":
    vgsales = loadprep_vgsales(parse_args().vgsales)