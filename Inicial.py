import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')
import pandas_datareader
import pandas_datareader.data as web
import datetime
import mplfinance as mpf
import plotly.graph_objects as go
from plotly.subplots import make_subplots


bbas3 = web.get_data_yahoo('BTC-USD', start =datetime.datetime(2021, 1, 1), end = datetime.datetime(2022, 4, 1))

print(bbas3)