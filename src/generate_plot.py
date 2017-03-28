import glob
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

inp_file = '/home/dubeya/dlcity/data/dense_safety_30'

csv_list = glob.glob(inp_file+'/*.csv')
mats = [np.genfromtxt(x) for x in csv_list]

means = [np.mean(x[:,2]) for x in mats]
sigmas = [np.std(x[:,2]) for x in mats]
citynames = [os.path.basename(x).replace('.csv','') for x in csv_list]

data = sorted([(m,s,c) for m,s,c in zip(means,sigmas,citynames)])

sm = [x[0] for x in data]
ss = [x[1] for x in data]
sc = [x[2] for x in data]

plt.figure()
plt.errorbar(range(len(sm)), sm, yerr=ss)
plt.xticks(range(len(sm)), sc, rotation='vertical')
plt.savefig('output.png', dpi=600)