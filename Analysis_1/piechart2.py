import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/RashmikaD2001/Python-Bootcamp-Project/refs/heads/main/cleaned_data.csv"
crick_df = pd.read_csv(url)

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd

# Assuming crick_df is already loaded

# Calculate host country counts
host_counts = crick_df['host_country'].value_counts()

# Create the figure and axes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Pie chart on the left (ax1)
wedges, texts, autotexts = ax1.pie(host_counts,
                                  startangle=90,
                                  autopct='%1.1f%%',
                                  textprops={'color': 'w'},
                                  wedgeprops={'linewidth': 1,
                                              'edgecolor': 'black'})
ax1.set_title('Host Country Distribution')

# Create color list with percentages
color_list = []
for i, wedge in enumerate(wedges):
    color = wedge.get_facecolor()
    country = host_counts.index[i]
    percentage = host_counts.iloc[i] / host_counts.sum() * 100
    color_list.append([color, country, percentage])

# Color list on the right (ax2)
ax2.axis('off')  # Hide axes
for i, (color, country, percentage) in enumerate(color_list):
    rect = mpatches.Rectangle((0, 0.9 - i * 0.1),
                              0.2,
                              0.1,
                              facecolor=color,
                              edgecolor='black')
    ax2.add_patch(rect)
    ax2.text(0.25,
             0.9 - i * 0.1 + 0.05,
             f"{country} ({percentage:.1f}%)",
             va='center')
ax2.set_title('Host Countries')

# Adjust spacing between subplots
plt.subplots_adjust(wspace=0.3)

plt.show()