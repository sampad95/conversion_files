import numpy as np

str_file = input("Enter the structure file in POSCAR format:\n")
 
with open(str_file, 'r') as data:
    fl = data.readlines()
    
scale_factor = float(fl[1])


lm = scale_factor*np.array([list(map(float, fl[2:5][i].split())) for i in range(len(fl[2:5]))])

a_v=lm[0]
b_v=lm[1]
c_v=lm[2]

a = np.sqrt(a_v[0]**2+a_v[1]**2+a_v[2]**2)
b = np.sqrt(b_v[0]**2+b_v[1]**2+b_v[2]**2)
c = np.sqrt(c_v[0]**2+c_v[1]**2+c_v[2]**2)

alpha = np.arccos(np.dot(a_v, b_v)/(a*b))*180/np.pi
beta  = np.arccos(np.dot(b_v, c_v)/(b*c))*180/np.pi
gamma = np.arccos(np.dot(c_v, a_v)/(c*a))*180/np.pi

volume = abs(np.dot(a_v, np.cross(b_v,c_v)))

print("\nCell parameters"+ "\n a = {:.10f}".format(a)+"\n b = {:.10f}".format(b)+"\n c = {:.10f}".format(c))
print("\n alpha\t= {:.5f}".format(alpha)+"\n beta\t= {:.5f}".format(beta)+"\n gamma\t= {:.5f}".format(gamma))
