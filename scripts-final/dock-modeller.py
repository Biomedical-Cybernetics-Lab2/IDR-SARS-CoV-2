import os
import glob
import pandas as pd

def run(s):
    os.system(s)

df = pd.read_csv('./docking-summary/simple.csv')
ligands = []

for i in range(725):
    ligands.append(df['Molecule'][i])

# print(ligands)

k = len(ligands)

for i in range(k):
    print("\nThis Is Docking ", i, "\n")

    for j in range(1, 6):

        s = "adfr -l ./nci-final/{ligand}.pdbqt -t target-files/nsp5_mod{index}.trg --nbRuns 7 --maxEvals 28000 -O -o docking-modeller-results/nsp5-mod{index}/{ligand}".format(ligand = ligands[i], index = j)

        # print(s)
        run(s)