# -*- coding: utf-8 -*-

# =============================================================================
# SOC 765 | Introduction to Computational Social Science
# Spring 2019
# Project III
# Names: Jaqueline Papp and Joshua Megnauth
# Project Title: Do review scores affect video game sales?
# =============================================================================


def print_descriptive(vgsales, header="=" * 60, begin=1984, end=2016):
    """
    Prints descriptive statistics for the Metacritic average and Sales.
    """
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
          "the highest average rating of {2} to {3} was {4} held by {5}.\n"
          .format(vgsales.Metacritic.min(), vgsales.Metacritic.idxmin(),
                  begin, end, vgsales.Metacritic.max(),
                  vgsales.Metacritic.idxmax()))

    # Quantiles
    sales_quant = vgsales.Sales.quantile([.25, .50, .75])
    print("Sales quantiles:\n"
          "25th: {0}\n"
          "50th: {1}\n"
          "75th: {2}\n"
          .format(sales_quant[.25], sales_quant[.50], sales_quant[.75]))

    metacritic_quant = vgsales.Metacritic.quantile([.25, .50, .75])
    print("Metacritic quantiles:\n"
          "25th: {0}\n"
          "50th: {1}\n"
          "75th: {2}"
          .format(metacritic_quant[.25], metacritic_quant[.50],
                  metacritic_quant[.75]))
