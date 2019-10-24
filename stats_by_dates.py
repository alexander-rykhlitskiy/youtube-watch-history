# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.2.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
from bs4 import BeautifulSoup as bs
import dateparser
import pandas as pd

doc = bs(open('youtube_watch_history.html', 'r').read(), 'lxml')
dates = [dateparser.parse(cell.contents[-1]) for cell in doc.select('.content-cell:has(a)')]

# %%
months = [date.strftime('%Y-%m') for date in dates]

data = {'date': dates, 'month': months}
grouped_dates = pd.DataFrame(data)
grouped_dates

# %%
# makes svg format possible
# # %matplotlib inline
# # %config InlineBackend.figure_format = 'svg'

# # %matplotlib notebook

# import matplotlib.pyplot as plt
# plt.rcParams.update({'font.size': 4})
# plt.rcParams.update({'figure.dpi': 160})
# plt.locator_params(nbins=20)

import plotly.plotly as py
import cufflinks as cf

cf.go_offline()

grouped_dates.groupby(by='month')['date'].size().iplot()

# %%
