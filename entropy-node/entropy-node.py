import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    # d = {int(i):0 for i in np.unique(y)}
    # tot = len(y)
    # for i in d.keys():
    #     for num in y:
    #         if i == num:
    #             d[i] += 1
    #     h_s = np.array([(i/j)*np.log2(i) for i,j in d.items()]).sum()
    h_s = np.unique(y,return_counts=True)
    tot = len(y)
    entrpy = []
    for i,j in zip(h_s[0],h_s[1]):
        p_i = j/tot
        print(p_i)
        entrpy.append(p_i*np.log2(p_i))
    entrpy = -1 * np.array(entrpy).sum()
    return entrpy