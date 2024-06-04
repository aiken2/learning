# -*- coding: utf-8 -*-
"""env_create

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CwgoS9XK8ZYfzL14O2UUuoi0bCCVqJ3r
"""

import pandas as pd

url = "https://raw.githubusercontent.com/aiken2/learning/main/Salary_Data.csv"
data = pd.read_csv(url)
data
# y = w*x + b
x = data["YearsExperience"]
y = data["Salary"]

w = 10
b = 0
y_pred = w*x + b
cost = (y - y_pred) ** 2
cost.sum() / len(x)

def compute_cost(x, y, w, b):
    y_pred = w*x + b
    cost = (y - y_pred)**2
    cost = cost.sum() / len(x)
    return cost

compute_cost(x, y, 10, 10)

# b=0 w=-100~100 cost 會是多少

costs = []
for w in range(-100, 101):
    cost = compute_cost(x, y, w, 0)
    costs.append(cost)
costs

import matplotlib.pyplot as plt


# plt.scatter(range(-100, 101), costs)
plt.plot(range(-100, 101), costs)
plt.title("cost function b=0 w-100~100")
plt.xlabel("w")
plt.ylabel("cost")
plt.show()

# w=-100~100 b=-100~100 的 cost
import numpy as np

ws = np.arange(-100, 101)
bs = np.arange(-100, 101)
#costs = np.zeros((201, 201))
costs = np.zeros((len(ws), len(bs)))

i = 0
for w in ws:
  j = 0
  for b in bs:
    cost = compute_cost(x, y, w, b)
    costs[i, j] = cost
    #print(i)
    #print(j)
    j = j + 1
  i = i + 1
costs = costs / 1000
costs

!pip install wget
import wget

wget.download("https://raw.githubusercontent.com/aiken2/learning/main/ChineseFont.ttf")

import matplotlib as mpl
from matplotlib.font_manager import fontManager
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

fontManager.addfont("ChineseFont.ttf")
mpl.rc("font",family="ChineseFont")

#fig = plt.figure(figsize=(16, 6))
fig = plt.figure(figsize=(7, 7))

ax = plt.axes(projection="3d")
ax.view_init(45, -100)
ax.xaxis.set_pane_color((1,1,1))
ax.yaxis.set_pane_color((1,1,1))
ax.zaxis.set_pane_color((1,1,1))

#ax.xaxis.set_major_locator(MultipleLocator(2))
#ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))

b_grid, w_grid = np.meshgrid(bs, ws)
# what is meshgrid
# https://wangcyeming.github.io/2018/11/12/numpy_meshgrid/
ax.plot_surface(w_grid, b_grid, costs, cmap="Spectral_r", alpha=0.7) #
ax.plot_wireframe(w_grid, b_grid, costs, color="black",alpha=0.1) #, cmap="Spectral_r"
ax.set_title("w b 對應的 cost")
#ax.set_xlabel("w", fontsize=7, labelpad=3)
#ax.set_ylabel("b", fontsize=7, labelpad=3)
#ax.set_zlabel("cost (K)", fontsize=7, labelpad=5)
ax.set_xlabel("w")
ax.set_ylabel("b")
ax.set_zlabel("cost (K)")
#ax.tick_params(axis='both', which='major', labelsize=6, pad=10)
#plt.tight_layout()

w_index, b_index = np.where(costs == np.min(costs))
ax.scatter(ws[w_index], bs[b_index], costs[w_index,b_index], color="red", s=40)
#print(np.min(costs))
#print(w_index, b_index)
#print(ws[w_index], bs[b_index])
#print(f"當ws{ws[w_index]}, bs{bs[b_index]} 會有最小cost:{costs[w_index,b_index]}")
plt.show()
#formula 1 = Math.pow(y - y_pred, 2)
#         = (y - y_pred) = (y - w*x ) = -2x(y-w*x)
#differential formula above
#keyword : learning rate, Slope, gradient descent
#bigger learning rate  bigger step
# 2*x*(w*x+b-y)