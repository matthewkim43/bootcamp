"""
Commonly used packages,functions,etc.
"""

import numpy as py
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

def ecdf(data):
    """Computes and plots ECDF"""

    # Creating x and y values
    x = np.sort(data)
    y = np.arange(1,len(data)+1)/len(data)

    return x, y
