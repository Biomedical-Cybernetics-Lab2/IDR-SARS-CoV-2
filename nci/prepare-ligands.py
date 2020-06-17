import os
import glob

def run(s):
    os.system(s)


ligands = glob.glob("./*.pdb")

l = len(ligands)
print(l)

for i in range(l):
    file_pdb = ligands[i][2:]
    file_pdbqt = file_pdb + "qt"

    print(i)

    
    s = "prepare_ligand -l "
    s = s + file_pdb
    s = s + " -o nci-final/"
    s = s + file_pdbqt

    run(s)
