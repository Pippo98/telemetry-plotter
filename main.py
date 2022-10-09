#! /usr/bin/env python3

import os
import sys
import matplotlib
from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Alignat, Command, NoEscape
matplotlib.use('Agg')  # Not to use X server. For TravisCI.
import matplotlib.pyplot as plt  # noqa
import pandas as pd

from utils.filepaths import *
from utils.colors import *

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(18.5, 10.5)

geometry_options = {"margin": "0cm"}
doc = Document(geometry_options=geometry_options)

with doc.create(Figure(position="htbp")) as figure:
    figure.add_image(LOGO_LT, width=NoEscape(r'0.7\paperwidth'))

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

ped = pd.read_csv(SESSION_PATH + PEDALS)
plt.plot(ped["_timestamp"], ped["apps"])
plt.grid(True)
plt.legend([
        "throttle " + UNITS[PEDALS]["apps"],
    ])
plot(doc)


doc.generate_pdf('report', clean_tex=False, silent=True)
