from data_source import * 
from data_processor import *

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-whitegrid')

xs = np.array([1, 2, 3, 4, 5, 6])
ys = np.array([get_max_value(contributions), get_min_value(contributions),
			   get_max_value(predictions), get_min_value(predictions),
			   get_max_value(rates), get_min_value(rates)])

plt.annotate("Max value contributions", (1, get_max_value(contributions)))
plt.annotate("Min value contributions", (2, get_min_value(contributions)))
plt.annotate("Max value predictions", (3, get_max_value(predictions)))
plt.annotate("Min value predictions", (4, get_min_value(predictions)))
plt.annotate("Max value rates", (5, get_max_value(rates)))
plt.annotate("Min value rates", (6, get_min_value(rates)))

plt.plot(xs, ys, 'o')

plt.show()