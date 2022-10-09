#! /usr/bin/env python3

import os
import sys
import matplotlib
from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Alignat, Command, NoEscape
matplotlib.use('Agg')  # Not to use X server. For TravisCI.
import matplotlib.pyplot as plt  # noqa
import pandas as pd
from datetime import datetime

from utils.filepaths import *
from utils.colors import *

fig = None
geometry_options = {"margin": "0cm"}
doc = Document(geometry_options=geometry_options)

with doc.create(Figure(position="htbp")) as figure:
    figure.add_image(LOGO_LT, width=NoEscape(r'0.7\paperwidth'))

def new_plot():
    global fig
    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(18*1.1, 10*1.1)
def plot(doc_):
    with doc_.create(Figure(position="htbp")) as plot:
        plot.add_plot(width=NoEscape("\paperwidth"), dpi=300)

doc.append(Command("fontsize", ["50", "60"]))
doc.append(NoEscape("\selectfont"))
doc.append(NoEscape("\centering"))
doc.append("Telemetry Report")

doc.append(Command("fontsize", ["16", "18"]))
doc.append(NoEscape("\selectfont"))


SESSION_PATH = "/home/filippo/logs/2022_09_18/ [] 001/"



def parser(x):
    for i, el in enumerate(x):
        x[i] = datetime.utcfromtimestamp(el/1000000)
    return x
CSVs = {}
max_t = 0
min_t = sys.maxsize
for file in CSV_FILES:
    df = pd.read_csv(SESSION_PATH + file)
    s_ = df["_timestamp"][ 0]
    e_ = df["_timestamp"][df.ndim]
    min_t = min(min_t, e_)
    max_t = min(max_t, s_)
    df["_timestamp"] = parser(df.loc[:, "_timestamp"])
    df = df.set_index("_timestamp")
    df.resample("100L", offset=s_)
    CSVs[file] = df

new_plot()
plt.plot(CSVs[PEDALS].index, CSVs[PEDALS].loc[:, "apps"], CSVs[PEDALS].index,
        CSVs[PEDALS].loc[:, "bse_front"],
        CSVs[PEDALS].index, CSVs[PEDALS].loc[:, "bse_rear"])
plt.grid(True)
plt.legend([
        "throttle [ % ]",
        "bse_front [bar]",
        "bse_rear [bar]"
    ])
plot(doc)
plt.close()

new_plot()

plt.plot(CSVs[PEDALS].index, CSVs[PEDALS].loc[:, "apps"], CSVs[PVT].index,
        CSVs[PVT].loc[:, "gSpeed"]*3.6/1000)
plt.grid(True)
plt.legend([
        "throttle [ % ]",
        "gps_speed [Km/h]"
    ])
plot(doc)
plt.close()


doc.generate_pdf('report', clean_tex=False, silent=True)
