import numpy as np

def axis_swap(str_file):
    with open(str_file, 'r') as data:
        fl = data.readlines()
        
        
        i = np.array([1, 0, 0])
        j = np.array([0, 1, 0])
        k = np.array([0, 0, 1])
        
        axis1 = input("Enter the 1st axis in capital: X or Y or Z\n")
        axis2 = input("Enter the 2nd axis in capital: X or Y or Z\n")
        
        if axis1 == "X" and axis2 == "Y":
            ax1 = 0
            ax2 = 1
        elif axis1 == "Y" and axis2 == "Z":
            ax1 = 1
            ax2 = 2
        elif axis1 == "X" and axis2 == "Z":
            ax1 = 0
            ax2 = 2
        else:
            print("Type error")
        
        I = np.array([i,j,k])
        trans_matrix = I.copy()
        trans_matrix[:, [ax1, ax2]] = trans_matrix[:, [ax2, ax1]]
        
        scale_factor = float(fl[1])
        
        lattice_vectors = scale_factor*np.array([list(map(float, i.split())) for i in fl[2:5]])
        new_lattice_vectors = np.dot(trans_matrix, lattice_vectors)

        
        coord_mat = np.array([list(map(float, j.split()[:3])) for j in fl[8:]]).T
        new_coord = np.dot(trans_matrix, coord_mat).T
        
        with open('POSCAR_swap', 'w') as output:
            output.write("generated by sampad's python code" +'\n')
            output.write("1.0" + '\n')
            
            for lv in new_lattice_vectors:
                output.write('\t'+"{:.16f}".format(lv[0])+'\t'+"{:.16f}".format(lv[1])+'\t'+"{:.16f}".format(lv[2])+'\n')
            
            output.writelines(fl[5:8])
            for nc in new_coord:
                output.write('\t'+"{:.16f}".format(nc[0])+'\t'+"{:.16f}".format(nc[1])+'\t'+"{:.16f}".format(nc[2])+'\n')
    
    print("POSCAR_swap is written")            
    return new_lattice_vectors, new_coord



structure_file = input("Enter the structure file in POSCAR format \n")

axis_swap(structure_file)
