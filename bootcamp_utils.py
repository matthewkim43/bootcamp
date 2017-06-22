"""
Commonly used packages,functions,etc.
"""

def ecdf(data):
    """Computes and plots ECDF"""

    # Creating x and y values
    x = np.sort(data)
    y = np.arange(1,len(data)+1)/len(data)

    return x, y

# Computes bootstrap replicates
def bs_replicate(data, func = np.mean):
    """Compute a bootstrap replicate from data"""
    bs_sample = np.random.choice(data, replace = True, size = len(bd_2012))
    return func(bs_sample)

# Draws bootstrap data from 1d data
def draw_bs_reps(data, func = np.mean, size = 10000):
    """Draw bootstrap replicates from 1d data"""
    bs_reps = [bs_replicate(data, func = func) for _ in range(size)]
    return np.array(bs_reps)
