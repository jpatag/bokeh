#-----------------------------------------------------------------------------
# Copyright (c) 2012 - 2022, Anaconda, Inc., and Bokeh Contributors.
# All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
#-----------------------------------------------------------------------------
''' US Unemployment rate data by month and year, from 1948 to 2013.

License: `Public Domain`_

Sourced from: https://www.bls.gov

This module contains one pandas Dataframe: ``data``.

.. rubric:: ``data``

:bokeh-dataframe:`bokeh.sampledata.unemployment1948.data`

.. bokeh-sampledata-xref:: unemployment1948
'''

#-----------------------------------------------------------------------------
# Boilerplate
#-----------------------------------------------------------------------------
from __future__ import annotations

import logging # isort:skip
log = logging.getLogger(__name__)

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# Bokeh imports
from ..util.sampledata import package_csv

#-----------------------------------------------------------------------------
# Globals and constants
#-----------------------------------------------------------------------------

__all__ = (
    'data',
)

#-----------------------------------------------------------------------------
# General API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Dev API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Private API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------

data = package_csv('unemployment1948', 'unemployment1948.csv')
