#%%
import numpy as np

#%%
def entropy(*ensemble: list):
    assert sum(ensemble) == 1
    return (sum(p*np.log2(1/p) for p in ensemble))

#%%
# What is the entropy for a balanced (4) dice
entropy(1/4, 1/4, 1/4, 1/4)

#%%
# What is the entropy for a biased (4) dice
entropy(1/2, 1/8, 1/8, 1/4)

#%%
# What is the entropy of submarine game, 8X8 board, and 1 tile has a submarine
board = 64*[1/64]
entropy(*board)
# %%
