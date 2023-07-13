"""
File: collect_data.py
Author: Chuncheng Zhang
Date: 2023-07-12
Copyright & Email: chuncheng.zhang@ia.ac.cn

Purpose:
    Amazing things

Functions:
    1. Requirements and constants
    2. Function and class
    3. Play ground
    4. Pending
    5. Pending
"""


# %% ---- 2023-07-12 ------------------------
# Requirements and constants
import pandas as pd
import plotly.express as px

from rich import print
from pathlib import Path
from tqdm.auto import tqdm
from IPython.display import display


# %% ---- 2023-07-12 ------------------------
# Function and class

def concat(left, right, copy=False):
    """Concat right to left.
    The left is a list with variable length, and the right is iterable.

    Args:
        left (list): The list to concat at.
        right (iterable): The elements of the right will be appended to the left by the same order.
        copy (bool, optional): Whether copy the left and its raw object will be left unchanged. Defaults to False.

    Returns:
        list: The concatenated list of the left or its clone.
    """

    if copy:
        left = [e for e in left]

    for e in right:
        left.append(e)

    return left


# %% ---- 2023-07-12 ------------------------
# Play ground
folder = Path('./data/xls')

data = []

for path in tqdm([e for e in folder.iterdir() if e.name.endswith('.xls')], 'Read xls'):
    content = pd.read_excel(path, header=[0, 3, 4])
    content.set_index(content.columns[0], inplace=True)
    content.index.name = ''
    content.dropna(inplace=True)
    # display(content.iloc[:8])

    table_name = content.columns[0][0]
    for col in tqdm(content.columns, 'Record {}'.format(table_name)):
        data += [concat([city, value], col)
                 for city, value in content[col].items()]


table = pd.DataFrame(
    data, columns=['city', 'value', 'table', 'subject', 'gender'])
table.to_csv('table.csv', encoding='utf-8')
display(table)


# %% ---- 2023-07-12 ------------------------
# Pending


# %% ---- 2023-07-12 ------------------------
# Pending
content.columns
# %%
for e in content.columns:
    print(e)

# %%
