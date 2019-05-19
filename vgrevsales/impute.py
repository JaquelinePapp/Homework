# -*- coding: utf-8 -*-

# =============================================================================
# SOC 765 | Introduction to Computational Social Science
# Spring 2019
# Project II
# Names: Jaqueline Papp and Joshua Megnauth
# (Working) Project Title: Do review scores affect video game sales?
# =============================================================================

import pandas.core.dtypes.dtypes as pdtypes


# =============================================================================
# So, we have an idea we can't implement yet but I'll explain it so I can try
# to implement it later. Means or medians are sometimes used to fill in nulls
# as an imputation method. As an imputation method, filling nulls with means
# is poor compared to using ML to impute the data. However, sklearn's imputer
# that can use ML is experimental and not available yet.
#
# Our plan was to mitigate the flaws of using an entire feature's mean to fill
# up our nulls. So, instead of taking the mean Metacritic average from decades
# of reviews, we intended to use the mean when grouped by certain columns
# to get a better estimate.
#
# For example, if an action game for PlayStation 3 was missing its review
# average, we could take the average of all PlayStation 3 action games
# as a default value for that game.
#
# Unfortunately, it's pretty hard to implement this with Pandas. So, this idea
# is shelved for now and definitely won't be done by the time this assignment
# is turned in. We'll just drop the nulls.
# =============================================================================

class VgsalesImputer:
    def __init__(self, vgsales):
        self._vgsales = vgsales

# =============================================================================
#         Every generation covered by the dataset is listed here.
#         (Well, sort of, as the first console generation wasn't included in
#         the dataset.) The years and consoles are listed as dictionaries
#         set as attributes to the class. This can be refactored to make them
#         static variables later. Note that not every console is covered here.
#         The consoles covered are more or less equivalent to
#         vgsales.Platform.unique().
# =============================================================================

        self._gen_one = {
                "years": list(range(1972, 1979)),
                "consoles": ["Coleco Telstar", "Magnavox Odyssey"]
                }

        self._gen_two = {
                "years": list(range(1976, 1993)),
                "consoles": ["2600", "5200"]
                }

        self._gen_three = {
                "years": list(range(1983, 2004)),
                "consoles": ["NES"]
                }

        self._gen_four = {
                "years": list(range(1987, 2005)),
                "consoles": ["GB", "SCD", "NG", "TG16", "GG", "GEN"]
                }

        self._gen_five = {
                "years": list(range(1993, 2006)),
                "consoles": ["N64", "PS", "SAT", "WS", "PCFX", "3DO"]
                }

        self._gen_six = {
                "years": list(range(1998, 2016)),
                "consoles": ["PS2", "SNES", "GBA", "XB", "GC", "DC"]
                }

        self._gen_seven = {
                "years": list(range(2005, 2019)),
                "consoles": ["Wii", "DS", "X360", "PS3"]
                }

        self._gen_eight = {
                "years": list(range(2012, 2020)),
                "consoles": ["PS4", "3DS", "XOne", "PSP", "WiiU", "PSV"]
                }

        self._genlist = [self._gen_one, self._gen_two, self._gen_three,
                         self._gen_four, self._gen_five, self._gen_six,
                         self._gen_seven, self._gen_eight]

    def _platform_handler(self, vgsales, col):
        for gen in self._genlist:
            pass

    def impute_vgsales_features(self):
        for col in self._vgsales.columns:
            if isinstance(self._vgsales[col], pdtypes.CategoricalDtype):
                pass
        else:  # float64, Int64
            pass
