import numpy as np

def carte_to_frac(str_file):
    with open(str_file, 'r') as data:
        fl = data.readlines()

        scale_factor = fl[1]
        lattice_matrix = np.array([list(map(float, fl[2:5][i].split()[:3])) for i in range(len(fl[2:5]))]).T
        carte_coord_matrix = np.array([list(map(float, fl[8:][i].split()[:3])) for i in range(len(fl[8:]))]).T
        fractional_coord = np.dot(np.linalg.inv(lattice_matrix), carte_coord_matrix).T

    return fractional_coord

str_file = input('Enter the file name\n')

for i in carte_to_frac(str_file):
    print(i[0], '\t', i[1], '\t', i[2])
