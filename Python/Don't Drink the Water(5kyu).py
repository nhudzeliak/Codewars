import numpy as np

density = {'H':1.36,
           'W':1.00,
           'A':0.87,
           'O':0.8}

def separate_liquids(glass):
    if len(glass) > 0:
        matrix = np.array(glass)
        flat_list = matrix.flatten().tolist()
        flat = np.array(sorted(flat_list, key=lambda k: density[k]))
        return flat.reshape((len(glass), len(glass[0]))).tolist()
    return glass
