import os
import glob
import re
import pandas as pd

results = glob.glob("./docking-results/*.dlg")

l = len(results)

valid = 0
data = []

for i in range(l):
    ligand_index = results[i][18:-12]

    # this will instead read the file into a python list. 
    f = open(results[i], 'r').readlines()
    if (len(f) > 33):
        nums = re.findall("[-]?\d+\.\d+", f[33])
        data.append([ligand_index, float(nums[0])])
        #print(results[i], ":", nums[0])
        valid += 1

#print("Valid: ", valid)
df = pd.DataFrame(data,columns=['Molecule','Affinity'])
df = df.sort_values(by=['Affinity'])

df.to_csv (r'./docking-summary/simple.csv', index = False, header=True)