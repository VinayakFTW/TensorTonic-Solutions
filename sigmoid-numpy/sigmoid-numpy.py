import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    x = np.array(x)
    sig_x = 1/(1+(np.exp(-x)))
    return sig_x