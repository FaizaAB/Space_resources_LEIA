# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 14:02:33 2022
#H2_R2O2 model:    
author: DL

Version 1.0
"""
import matplotlib.pyplot as plt
import numpy
import seaborn as sns
from matplotlib import cm
from matplotlib.colors import LinearSegmentedColormap, ListedColormap

import modules.H2_Reactor_1 as H2_Reactor_1
import modules.Storage as Storage
from modules.beneficiation_placeholder import *
from modules.electrolysis import electrolysis_energy_per_mol_H2O
from modules.excavation import *
from modules.H2_Reactor_1 import *
from modules.liquefaction import liquefaction
from modules.Storage import *
from modules.transportation import *
from calculate_energy import energy_as_func_of_ilmenite

forloops = False


plt.rc('axes', axisbelow=True)

ilmenite_grade_list, energy_list, energy_as_func_of_ilmenite_list, energy = energy_as_func_of_ilmenite()

# used lists and variables for the bar plot
viridis = cm.get_cmap('viridis', 12)
pastel = sns.color_palette(palette="muted", as_cmap=True)

print(energy)
sum_energy = np.sum(energy)
labels = np.round(energy/sum_energy*100, 3)
energy_consumers_full = ["Excavation", "Transportation",
                         "Reactor", "Electrolysis", "Liquefaction", "Storage"]
#colors_bars = ["tab:grey", "black", "tab:red", "tab:green",  "tab:blue", "tab:orange"]
colors_bars = ["orange", "red", viridis(
    0.2), viridis(0.45),  viridis(0.6), viridis(0.95)]
#colors_bars = [pastel[5], pastel[7], pastel[3], pastel[2],  pastel[0], pastel[8]]
# colors_bars = ['#FEB144', pastel[7], '#FF6663', '#FDFD97',  '#9EC1CF', '#9EE09E']
# colors_bars = ['black', '#8197a6', '#f1666a', '#00ae9d',  '#009bdb', '#1e3378']

# used lists and variables for the stackplot
legend_stackplot = ["Storage",  "Liquefaction",
                    "Electrolysis", "Transportation", "Excavation", "Reactor"]
#colors_stackplot = [  "tab:orange",  "tab:blue", "tab:green", "tab:red","black","tab:grey" ]
colors_stackplot = [viridis(0.95),  viridis(
    0.6), viridis(0.45), "red", "orange", viridis(0.2)]
#colors_stackplot = [pastel[8], pastel[0], pastel[2], pastel[3],  pastel[7], pastel[5]]
# colors_stackplot = ['#9EE09E', '#9EC1CF', '#FDFD97', '#FF6663', pastel[7], '#FEB144']
# colors_stackplot = ['#1e3378', '#009bdb', '#00ae9d', '#f1666a', '#8197a6', 'black']

# create figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5),)


# create stackplot
#p2 = ax2.stackplot(ilmenite_grade_list, energy_list, colors = colors_stackplot, labels = legend_stackplot)

barwidth = 12/len(ilmenite_grade_list)
p2 = ax2.bar(ilmenite_grade_list,
             energy_list[0], color=colors_stackplot[0], label=legend_stackplot[0], width=barwidth)
p3 = ax2.bar(ilmenite_grade_list, energy_list[1], bottom=energy_list[0],
             color=colors_stackplot[1], label=legend_stackplot[1], width=barwidth)
p4 = ax2.bar(ilmenite_grade_list, energy_list[2], bottom=energy_list[0]+energy_list[1],
             color=colors_stackplot[2], label=legend_stackplot[2], width=barwidth)
p5 = ax2.bar(ilmenite_grade_list, energy_list[3], bottom=energy_list[0]+energy_list[1] +
             energy_list[2], color=colors_stackplot[3], label=legend_stackplot[3], width=barwidth)
p6 = ax2.bar(ilmenite_grade_list, energy_list[4], bottom=energy_list[0]+energy_list[1]+energy_list[2] +
             energy_list[3], color=colors_stackplot[4], label=legend_stackplot[4], width=barwidth)
p7 = ax2.bar(ilmenite_grade_list, energy_list[5], bottom=energy_list[0]+energy_list[1]+energy_list[2] +
             energy_list[3]+energy_list[4], color=colors_stackplot[5], label=legend_stackplot[5], width=barwidth)

ax2.grid(axis="y")
ax2.set_title("B", loc="left", fontsize=20)
ax2.set_xlabel("Ilmenite %")
ax2.set_ylabel('kWh/kg LOX')
ax2.set_xlim((0.75, 15.25))
ax2.legend()

# create bar plot
p1 = ax1.bar(energy_consumers_full, energy, color=colors_bars)
ax1.grid(axis="y")
ax1.set_title("A", loc="left",  fontsize=20)
ax1.set_ylabel('kWh/kg LOX')

index = -1
for bar in p1:
    index = index+1
    width = bar.get_width()
    height = bar.get_height()
    x, y = bar.get_xy()
    ax1.text(x+width/2,
             y+height*1.01,
             str(labels[index])+'%',
             ha='center',
             weight='bold')

fig.autofmt_xdate()
plt.setp(ax2.xaxis.get_majorticklabels(), rotation=0,
         ha="center", rotation_mode="anchor")
#plt.suptitle('Energy comparison between different process steps')
plt.subplots_adjust(wspace=0.3)
plt.savefig('Result_figure.png', dpi=200, bbox_inches='tight')
plt.show()
plt.close()


# Define fitting function for energy as function of ilmenite %
def func(i, a, c):
    return a/i + c


# use curve_fit from scipy.optimize to fit the fitting function to the data
# outcomes are popt (optimal parameters)
popt, pcov = curve_fit(func, ilmenite_grade_list,
                       energy_as_func_of_ilmenite_list)
# Evaluate and plot function with the optimal parameters
# print(popt[0],popt[1])
funcdata_energy_as_function_of_ilmenite = func(
    ilmenite_grade_list, popt[0], popt[1])
#plt.plot(ilmenite_grade_list,funcdata_energy_as_function_of_ilmenite,label="energy as function of ilmenite %")
# plt.show()


print("\n end")
