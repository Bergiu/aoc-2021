import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
inp = [list(map(int, x)) for x in open("input").read().splitlines()]

#plt.imshow(inp, cmap='hot', interpolation='nearest')
sns.heatmap(inp, linewidth=0, square=True, xticklabels=False, yticklabels=False)
plt.show()
