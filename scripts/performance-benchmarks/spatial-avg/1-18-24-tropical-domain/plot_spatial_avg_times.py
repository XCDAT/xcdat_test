# %%
import os
import time

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# %% Get the CSV data into DataFrames.
ROOT_PATH = "./scripts/performance-benchmarks/spatial-avg/spatial-avg-domain"
xcdat_csv_path = os.path.join(ROOT_PATH, "20240117-140947-xcdat-runtimes_serial.csv")
cdat_csv_path = os.path.join(ROOT_PATH, "20240118-125814-cdat-runtimes.csv")


df_xcdat = pd.read_csv(xcdat_csv_path)
df_cdat = pd.read_csv(cdat_csv_path)

# %% Get x / y series.
bar_width = 0.25
y_cdat = df_cdat["runtime_serial"].values
x_cdat = np.arange(len(y_cdat))
y_xcdats = df_xcdat["runtime_serial"].values
x_xcdats = x_cdat + bar_width


# %% Plot the data.
# Set up the bar plot objects.
plt.bar(
    x_cdat, y_cdat, width=bar_width, facecolor="firebrick", edgecolor=None, label="CDAT"
)
plt.bar(
    x_xcdats,
    y_xcdats,
    width=bar_width,
    facecolor="darkseagreen",
    edgecolor=None,
    label="xCDAT Serial",
)

# Add plot labels.
plt.legend(loc="upper left", frameon=False)
plt.title("Spatial Average Runtime Comparison")
plt.ylabel("Runtime [s]")
plt.xlabel("Filesize [GB]")
plt.xticks(x_xcdats, labels=df_cdat["gb"])

# Update the spines.
ax = plt.gca()

# Move left and bottom spines outward by 10 points.
ax.spines.left.set_position(("outward", 10))

# Hide the right and top spines.
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)

# Only show ticks on the left and bottom spines.
ax.yaxis.set_ticks_position("left")
ax.xaxis.set_ticks_position("bottom")

# The base bar label configuration passed to axis containers to add
# the floating point labels above the bars.
BAR_LABEL_CONFIG = {
    "label_type": "edge",
    "padding": 2,
    "fontsize": 10,
}
for cont in ax.containers:
    labels = ["{:10.0f}".format(v) if v > 0.00 else "" for v in cont.datavalues]
    ax.bar_label(cont, **BAR_LABEL_CONFIG, labels=labels)

# %% Save the figure
TIME_STR = time.strftime("%Y%m%d-%H%M%S")
png_path = os.path.join(ROOT_PATH, f"{TIME_STR}-spatial-avg-runtimes.png")

plt.savefig(png_path)
plt.show()
