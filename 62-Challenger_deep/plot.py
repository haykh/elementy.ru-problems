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

fig, ax = plt.subplots(figsize=(3.5, 2), dpi=300)

s_to_h = 1 / (3600)

print (cols)
myplt.plot(ax, data[cols[0]] * s_to_h, data[cols[5]], padx=0.1, pady=0.2, c='k')
ax.set_xlabel('время [час]')
# ax.set_ylabel('давление [дбар]')

# ax.text(1, 1500, "погружение", ha='left', size=8)
# ax.text(13, 1500, "всплытие", ha='right', size=8)

# ax.annotate(f"{int(np.max(data[cols[1]]) * 100) / 100} дбар", xytext=(7, 5500), xy=(7, 11000), 
            # arrowprops={'arrowstyle': '->'},
            # ha="center", size=8)
# print (np.max(data[cols[1]]))

plt.tight_layout()
plt.show()
# plt.savefig('foo.png')
