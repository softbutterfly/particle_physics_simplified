import numpy as np
import matplotlib.pylab as plt

import sys

import pps_tools as hep

infile = sys.argv[1]

alldata = hep.get_all_data(infile,verbose=False)
#print(len(collisions), " collisions")

energies = []

nentries = hep.get_number_of_entries(alldata)
print('Number of entries: {0}'.format(nentries))

entry = 5

collision = hep.get_collision(alldata,entry_number=entry,experiment='BaBar')

#plt.figure()
hep.display_collision3D(collision,color_blind=False,experiment='BaBar')

plt.show()
    




