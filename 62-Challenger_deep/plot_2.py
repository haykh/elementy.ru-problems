import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

import myplotlib
myplotlib.load(style='fancy')

rc('text.latex',preamble=r'\usepackage[utf8]{inputenc}')
rc('text.latex',preamble=r'\usepackage[russian]{babel}')
import myplotlib.plots as myplt

data = pd.read_csv('data.csv')
cols = data.columns
cols


def plot():
  fig = plt.figure(figsize=(8, 3), dpi=300)
  ax = plt.subplot(131)
  s_to_h = 1 / (3600)
  g = 9.81
  take = slice(None, 800, None)
  depth = data[cols[1]] * 1e4 / (data[cols[4]] * 1000 * g)
  myplt.plot(ax, data[cols[-1]][take], depth[take], padx=0.2, pady=0.2, c='k')
  ax.invert_yaxis()
  ax.set_xlabel('скорость звука [м/с]')
  ax.set_ylabel('глубина [м]')

  ax = plt.subplot(132)
  s_to_h = 1 / (3600)
  g = 9.81
  take = slice(None, 800, None)
  depth = data[cols[1]] * 1e4 / (data[cols[4]] * 1000 * g)
  myplt.plot(ax, data[cols[1]][take], depth[take], padx=0.2, pady=0.2, c='k')
  ax.invert_yaxis()
  ax.set_xlabel('давление [дбар]')
  ax.spines['left'].set_visible(False)
  ax.set_yticklabels([])

  ax = plt.subplot(133)
  s_to_h = 1 / (3600)
  g = 9.81
  take = slice(None, 800, None)
  depth = data[cols[1]] * 1e4 / (data[cols[4]] * 1000 * g)
  # myplt.plot(ax, data[cols[-3]][take], depth[take], padx=0.2, pady=0.2, c='k')
  myplt.plot(ax, data[cols[2]][take], depth[take], padx=0.2, pady=0.2, c='k')
  ax.invert_yaxis()
  ax.set_xlabel('температура [${}^\circ$C]')
  ax.spines['left'].set_visible(False)
  ax.set_yticklabels([])

  plt.tight_layout()

plot()
# myplt.plot(ax, data[cols[0]] * s_to_h, data[cols[4]], padx=0.1, pady=0.2, c='k')
# ax.set_xlabel('время [час]')
# ax.set_ylabel('плотность [г/см${}^3$]')

# ax.text(1, 1500, "погружение", ha='left', size=8)
# ax.text(13, 1500, "всплытие", ha='right', size=8)

# ax.annotate(f"{int(np.max(data[cols[1]]) * 100) / 100} дбар", xytext=(7, 5500), xy=(7, 11000),
            # arrowprops={'arrowstyle': '->'},
            # ha="center", size=8)
# print (np.max(data[cols[1]]))

# plt.show()
plt.savefig('sound_speed.png')
#
