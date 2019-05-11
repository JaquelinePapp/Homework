# -*- coding: utf-8 -*-

# =============================================================================
# SOC 765 | Introduction to Computational Social Science
# Spring 2019
# Project II
# Names: Jaqueline Papp and Joshua Megnauth
# (Working) Project Title: Do review scores affect video game sales?
# =============================================================================


def print_descriptive(vgsales, header="=" * 60, begin=2005, end=2016):
    print(header + "\nDescriptive Statistics\n" + header)

    # Mean and standard deviation of Metacritic scores
    print("The average Metacritic score for video games released from {0} "
          "to {1} is {2:.3f} with a standard deviation of {3:.3f}.\n"
          .format(begin, end, vgsales.Metacritic.mean(),
                  vgsales.Metacritic.std()))

    # Median for Metacritic scores
    print("The median for Metacritic scores of that era is {0} "
          "indicating a negative skew for the mean.\n".format(
                  vgsales.Metacritic.median()))

    # Mean, median, and standard deviation for global sales
    print("Average global sales from {0} to {1} is {2:.3f} (millions) "
          "with a median of {3} and a standard deviation of {4:.3f} indicating"
          " a positive skew.\n"
          .format(begin, end, vgsales.Sales.mean(), vgsales.Sales.median(),
                  vgsales.Sales.std()))

    # Metacritic Min/Max
    print("The lowest Metacritic average during these years was {0}. The game "
          "with this dubious honor is {1}. On the other end of the spectrum, "
          "the highest average rating of {2} to {3} was {4} held by {3}.\n"
          .format(vgsales.Metacritic.min(), vgsales.Metacritic.idxmin(),
                  begin, end, vgsales.Metacritic.max(),
                  vgsales.Metacritic.idxmax()))

    # Quantiles
    print(vgsales.Sales.quantile([.25, .50, .75]))
    print(vgsales.Metacritic.quantile([.25, .50, .75]))
