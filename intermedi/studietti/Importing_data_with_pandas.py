
## Reading Files with pandas

# This block changes the directory to the location containing the data files.

# In[15]:

import os
os.chdir(r'C:\Anaconda\course')


# Pandas provides a number of useful readers for common file types, including csv, Excel, formatted text and Stata.  This first block is just the usual imports.

# In[16]:

import pandas as pd
import numpy as np


### `read_csv`

# Simple csv file can be directly read using `read_csv` without further options. `.head()` can be used to show the first 5 rows and `.tail()` can be used to show the last 5 rows.  `.head(`#`)` can be used to show a specific number of header rows.

# In[17]:

sp500 = pd.read_csv('sp_500.csv')
sp500.head(10)


# Out[17]:

#              Date     Open     High      Low    Close      Volume  Adj Close
#     0  2014-02-07  1776.01  1798.03  1776.01  1797.02  3775990000    1797.02
#     1  2014-02-06  1752.99  1774.06  1752.99  1773.43  3825410000    1773.43
#     2  2014-02-05  1753.38  1755.79  1737.92  1751.64  3984290000    1751.64
#     3  2014-02-04  1743.82  1758.73  1743.82  1755.20  4068410000    1755.20
#     4  2014-02-03  1782.68  1784.83  1739.66  1741.89  4726040000    1741.89
#     5  2014-01-31  1790.88  1793.88  1772.26  1782.59  4059690000    1782.59
#     6  2014-01-30  1777.17  1798.77  1777.17  1794.19  3547510000    1794.19
#     7  2014-01-29  1790.15  1790.15  1770.45  1774.20  3964020000    1774.20
#     8  2014-01-28  1783.00  1793.87  1779.49  1792.50  3437830000    1792.50
#     9  2014-01-27  1791.03  1795.98  1772.88  1781.56  4045200000    1781.56
#     
#     [10 rows x 7 columns]

# The index column can be set using the keyword argument `index_col` which takes a list or tuple containing the names (or locations, e.g. 0, 1 or 2) of the column(s) as an input.  Multiple columns can be used as an index, but further discussion of this is saved for later.

# In[18]:

sp500 = pd.read_csv('SP_500.csv',index_col=[0])
# These are the same
sp500 = pd.read_csv('SP_500.csv',index_col=['Date']) 
sp500.head()


# Out[18]:

#                    Open     High      Low    Close      Volume  Adj Close
#     Date                                                                 
#     2014-02-07  1776.01  1798.03  1776.01  1797.02  3775990000    1797.02
#     2014-02-06  1752.99  1774.06  1752.99  1773.43  3825410000    1773.43
#     2014-02-05  1753.38  1755.79  1737.92  1751.64  3984290000    1751.64
#     2014-02-04  1743.82  1758.73  1743.82  1755.20  4068410000    1755.20
#     2014-02-03  1782.68  1784.83  1739.66  1741.89  4726040000    1741.89
#     
#     [5 rows x 6 columns]

# Columns containing well formatted dates can be converted to Timestamps using the keyword argument `parse_date`, which accepts a list of column names or indices.  Timestamps allow fancy date-based indexing of DataFrames containing time-series data.

# In[19]:

sp500 = pd.read_csv('SP_500.csv',index_col=['Date'],parse_dates=['Date'])
sp500.index[0]


# Out[19]:

#     Timestamp('2014-02-07 00:00:00', tz=None)

### `read_excel`

# Excel files can be read using `read_excel` which requires at least 2 inputs: the filename and the sheet name.

# In[20]:

real_gdp = pd.read_excel('GDPC1.xls','GDPC1')
real_gdp.head()


# Out[20]:

#                      Title:                        Real Gross Domestic Product
#     0            Series ID:                                              GDPC1
#     1               Source:  U.S. Department of Commerce: Bureau of Economi...
#     2              Release:                             Gross Domestic Product
#     3  Seasonal Adjustment:                    Seasonally Adjusted Annual Rate
#     4            Frequency:                                          Quarterly
#     
#     [5 rows x 2 columns]

# This file contains extensive header information, and so it is necessary to skip some rows before the data reading should start.  This can be done using either `header` or `skiprows`.

# In[21]:

pd.read_excel('GDPC1.xls','GDPC1',header=19)
# Identical in this case
real_gdp = pd.read_excel('GDPC1.xls','GDPC1',skiprows=19)
real_gdp.head()


# Out[21]:

#             DATE   VALUE
#     0 1947-01-01  1932.6
#     1 1947-04-01  1930.4
#     2 1947-07-01  1928.4
#     3 1947-10-01  1958.8
#     4 1948-01-01  1987.6
#     
#     [5 rows x 2 columns]

# `index_col` can also be used to select the index, or the index can be set later by removing the index column and setting it to the DataFrame's `index` attribute.

# In[22]:

# Remove the column Data
date = real_gdp.pop('DATE')
# Use as index
real_gdp.index = date
real_gdp.head()


# Out[22]:

#                  VALUE
#     DATE              
#     1947-01-01  1932.6
#     1947-04-01  1930.4
#     1947-07-01  1928.4
#     1947-10-01  1958.8
#     1948-01-01  1987.6
#     
#     [5 rows x 1 columns]

# Column names can be set using the attribute `columns` which takes a list of column names with the correct number of elements, and `.info()` profiles a useful overview.

# In[23]:

real_gdp.columns = ['RGDP']
real_gdp.info()


# Out[23]:

#     <class 'pandas.core.frame.DataFrame'>
#     DatetimeIndex: 268 entries, 1947-01-01 00:00:00 to 2013-10-01 00:00:00
#     Data columns (total 1 columns):
#     RGDP    268 non-null float64
#     dtypes: float64(1)

### `real_table` and `read_fwf`

# `read_table` and `read_fwf` are both useful for reading text data. `read_table` is for general delimited data (e.g. tab or space delimited) while `read_fwf` is for fixed-width format data.  In many cases, either can be used, and `read_table` is usually recommended. The key input to `read_table` is `sep` for the separator to use.  This can be a regular expression such as `r'\s*` which will (greedily) match spaces.

# In[24]:

real_gdp = pd.read_table('GDPC1.txt',sep=r'\s*',skiprows=19, index_col=['DATE'], parse_dates=['DATE'])
real_gdp.head()


# Out[24]:

#                  VALUE
#     DATE              
#     1947-01-01  1932.6
#     1947-04-01  1930.4
#     1947-07-01  1928.4
#     1947-10-01  1958.8
#     1948-01-01  1987.6
#     
#     [5 rows x 1 columns]

# `colspecs`, which contains start and end points, $(s_i,e_i)$ of colums $(c_i)$ such that column $i$ is contained in $s_i\leq c_i < e_i$, is the key input to `read_fwf`. 

# In[25]:

colspecs = [(0,10),(10,20)]
real_gdp = pd.read_fwf('GDPC1.txt', colspecs=colspecs, skiprows=19, parse_dates=['DATE'], index_col=['DATE'])
real_gdp.head()


# Out[25]:

#                  VALUE
#     DATE              
#     1947-01-01  1932.6
#     1947-04-01  1930.4
#     1947-07-01  1928.4
#     1947-10-01  1958.8
#     1948-01-01  1987.6
#     
#     [5 rows x 1 columns]

# Alternatively, `widths` can be used when there is no gap between columns.  The locations of column $i$ satisfy $\sum_{j<i} w_j \leq c_i < \sum_{j\leq i}w_j $ where the first start point is 0.

# In[26]:

widths = [10,10]
real_gdp = pd.read_fwf('GDPC1.txt',widths=widths,skiprows=19,parse_dates=['DATE'],index_col=['DATE'])
real_gdp.head()


# Out[26]:

#                  VALUE
#     DATE              
#     1947-01-01  1932.6
#     1947-04-01  1930.4
#     1947-07-01  1928.4
#     1947-10-01  1958.8
#     1948-01-01  1987.6
#     
#     [5 rows x 1 columns]

### `read_hdf`

# `read_hdf` allows HDF 5 files to be read.  This function is most useful reading in pandas DataFrames which were previously exported.  It requires two inputs, the file name and the key, which is used when the file is created.

# In[27]:

sp500 = pd.read_hdf('sp500.h5','sp500')
sp500.head()


# Out[27]:

#                    Open     High      Low    Close      Volume  Adj Close
#     Date                                                                 
#     2014-02-07  1776.01  1798.03  1776.01  1797.02  3775990000    1797.02
#     2014-02-06  1752.99  1774.06  1752.99  1773.43  3825410000    1773.43
#     2014-02-05  1753.38  1755.79  1737.92  1751.64  3984290000    1751.64
#     2014-02-04  1743.82  1758.73  1743.82  1755.20  4068410000    1755.20
#     2014-02-03  1782.68  1784.83  1739.66  1741.89  4726040000    1741.89
#     
#     [5 rows x 6 columns]

### `read_pickle`

# `read_pickle` reads _pickled_ pandas  DataFrames (pickling preserves things) produced using `_to_pickle()`.  Pickling is fast and simple for a single variable but is not space efficient.

# In[28]:

sp500 = pd.read_pickle('sp500.pickle')
sp500.head()


# Out[28]:

#                    Open     High      Low    Close      Volume  Adj Close
#     Date                                                                 
#     2014-02-07  1776.01  1798.03  1776.01  1797.02  3775990000    1797.02
#     2014-02-06  1752.99  1774.06  1752.99  1773.43  3825410000    1773.43
#     2014-02-05  1753.38  1755.79  1737.92  1751.64  3984290000    1751.64
#     2014-02-04  1743.82  1758.73  1743.82  1755.20  4068410000    1755.20
#     2014-02-03  1782.68  1784.83  1739.66  1741.89  4726040000    1741.89
#     
#     [5 rows x 6 columns]

### `read_msgpack`

# Message Pack is a dense format that is very fast and is typically smaller than pickling.  It is still experimental, and only available in pandas version 0.13 or higher.

# In[29]:

sp500.to_msgpack('sp_500_export.msgpack')


# `read_msgpack` can load a DataFrame saved to Message Pack.

# In[30]:

pd.read_msgpack('sp_500_export.msgpack').head()


# Out[30]:

#                    Open     High      Low    Close      Volume  Adj Close
#     Date                                                                 
#     2014-02-07  1776.01  1798.03  1776.01  1797.02  3775990000    1797.02
#     2014-02-06  1752.99  1774.06  1752.99  1773.43  3825410000    1773.43
#     2014-02-05  1753.38  1755.79  1737.92  1751.64  3984290000    1751.64
#     2014-02-04  1743.82  1758.73  1743.82  1755.20  4068410000    1755.20
#     2014-02-03  1782.68  1784.83  1739.66  1741.89  4726040000    1741.89
#     
#     [5 rows x 6 columns]

### `read_stata`

# Stats files (.dta) can be directly read using `read_stata`.  There are few input arguments since the file format is well structured for storing data.  This example employs a commonly wage dataset named wage1.dta.


