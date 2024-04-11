# %%
# -*- coding: utf-8 -*-
"""
@author: hkaneko
"""

import pandas as pd

dataset = pd.read_csv("./sample_data/iris.csv", index_col=0)
dataset.to_csv("./sample_data/iris_new.csv")  # csv ファイルとして保存

# %%
