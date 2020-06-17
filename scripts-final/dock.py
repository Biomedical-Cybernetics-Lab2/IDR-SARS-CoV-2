import os
import glob

def run(s):
    os.system(s)


#run("adfr -l ligands/4EK4_random.pdbqt -t target-files/4EK3_rec_FR_10_33.trg --nbRuns 8 --maxEvals 100000 -O -o docking-results/4EK4_random_flexRec")

ligands = glob.glob("./nci-final/*.pdbqt")

l = len(ligands)
print(l)

for i in range(l):
    print("\nThis Is Docking ", i, "\n")

    file_pdbqt = ligands[i][2:]

    s = "adfr -l "
    s = s + file_pdbqt
    s = s + " -t target-files/nsp5.trg --nbRuns 7 --maxEvals 28000 -O -o docking-results/"
    s = s + file_pdbqt[10:-6]

    #run("adfr -l ligands/4EK4_random.pdbqt -t target-files/4EK3_rec_FR_10_33.trg --nbRuns 8 --maxEvals 100000 -O -o docking-results/4EK4_random_flexRec")

    run(s)


#adfr -l nci-final\99925.pdbqt -t target-files/nsp5.trg --nbRuns 7 --maxEvals 28000 -O -o docking-results/99925