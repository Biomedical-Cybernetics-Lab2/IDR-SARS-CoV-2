import os
import glob
import re
import pandas as pd

results = [[]]
results.append(glob.glob("./docking-modeller-results/nsp5-mod1/*.dlg"))
results.append(glob.glob("./docking-modeller-results/nsp5-mod2/*.dlg"))
results.append(glob.glob("./docking-modeller-results/nsp5-mod3/*.dlg"))
results.append(glob.glob("./docking-modeller-results/nsp5-mod4/*.dlg"))
results.append(glob.glob("./docking-modeller-results/nsp5-mod5/*.dlg"))

l = len(results[1])

data = []

for i in range(l):
    ligand_index = results[1][i][37:-12]
    cur_ligand = [ligand_index]
    for j in range(1, 6):
        #print(ligand_index)

        # this will instead read the file into a python list. 
        f = open(results[j][i], 'r').readlines()
        nums = re.findall("[-]?\d+\.\d+", f[33])
        cur_ligand.append(float(nums[0]))
        #print(results[i], ":", nums[0])
    data.append(cur_ligand)


#print("Valid: ", valid)
df = pd.DataFrame(data, columns=['Molecule','Affinity1', 'Affinity2', 'Affinity3', 'Affinity4', 'Affinity5'])

df_min = df
#df_min["Best Affinity"] = min((df['Affinity1']) & (df['Affinity2']) & (df['Affinity3']) & (df['Affinity4']) & (df['Affinity5']))
df_min["Best Affinity"] = df_min[['Affinity1', 'Affinity2', 'Affinity3', 'Affinity4', 'Affinity5']].min(axis = 1) 

df_min = df_min.sort_values(by=['Best Affinity'])
df_min.to_csv(r'./docking-summary/modeller-best.csv', index = False, header=True)

df['Avg. Affinity'] = (df['Affinity1'] + df['Affinity2'] + df['Affinity3'] + df['Affinity4'] + df['Affinity5']) / 5
df = df.sort_values(by=['Avg. Affinity'])

df.to_csv(r'./docking-summary/modeller-avg.csv', index = False, header=True)

'''
df1 = df.sort_values(by=['Affinity1'])
df2 = df.sort_values(by=['Affinity2'])
df3 = df.sort_values(by=['Affinity3'])
df4 = df.sort_values(by=['Affinity4'])
df5 = df.sort_values(by=['Affinity5'])

df1.to_csv(r'./docking-summary/modeller1.csv', index = False, header=True)
df2.to_csv(r'./docking-summary/modeller2.csv', index = False, header=True)
df3.to_csv(r'./docking-summary/modeller3.csv', index = False, header=True)
df4.to_csv(r'./docking-summary/modeller4.csv', index = False, header=True)
df5.to_csv(r'./docking-summary/modeller5.csv', index = False, header=True)
'''