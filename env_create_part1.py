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
y

!pip install wget
import wget

wget.download("https://raw.githubusercontent.com/aiken2/learning/main/ChineseFont.ttf")

import matplotlib.pyplot as plt
import matplotlib as mlp
from matplotlib.font_manager import fontManager

fontManager.addfont("ChineseFont.ttf")
mlp.rc("font",family="ChineseFont")

plt.scatter(x, y, marker="x", color="red")
plt.title("年資 - 薪水")
plt.xlabel("年資")
plt.ylabel("月薪(千)")
plt.show()

w = 0
b = 0

def plot_pred( w, b):
  y_pred = x*w+b
  plt.plot(x, y_pred, color="blue", label="預測線")
  plt.scatter(x, y, marker="x", color="red", label="真實數據")
  plt.title("年資 - 薪水")
  plt.xlabel("年資")
  plt.ylabel("月薪(千)")
  plt.xlim([0, 12])
  plt.ylim([-60, 140])
  plt.legend()
  plt.show()

plot_pred(-10, -30)

from ipywidgets import interact

interact( plot_pred, w=(-100, 100, 1), b=(-100, 100, 1))