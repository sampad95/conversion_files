import numpy as np

def slab_width(str_file):
    with open(str_file, 'r') as data:
        fl = data.readlines()
            
        Coord_mat = np.array([list(map(float, fl[8:][i].split())) for i in range(len(fl[8:]))]).T
    
        axis=input("Enter the axis of non-periodicity\n")
    
    
        if axis=="X" or axis=="x":
            n=0
        elif axis=="Y" or axis=="y":
            n=1
        elif axis=="Z" or axis=="z":
            n=2
        else:
            print("Type error")
            
        surface_width = max(Coord_mat[n]) - min(Coord_mat[n])
    
    return surface_width

structure_file = input("Enter the structure file in POSCAR format with cartesian coordinates\n")
print(slab_width(structure_file))
