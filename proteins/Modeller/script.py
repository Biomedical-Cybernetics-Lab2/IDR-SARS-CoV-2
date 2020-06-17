# Loop refinement of an existing model
from modeller import *
from modeller.automodel import *

log.verbose()
env = environ()

# directories for input atom files
env.io.atom_files_directory = './:../atom_files'

# Create a new class based on 'loopmodel' so that we can redefine
# select_loop_atoms (necessary)
class MyLoop(loopmodel):
    # This routine picks the residues to be refined by loop modeling
    def select_loop_atoms(self):
        # 10 residue insertion 
        return selection(self.residue_range('1:A', '6:A'))

m = MyLoop(env,
           inimodel='nsp5.pdb', # initial model of the target
           sequence='nsp5')          # code of the target

m.loop.starting_model= 1           # index of the first loop model 
m.loop.ending_model  = 10          # index of the last loop model
m.loop.md_level = refine.slow # loop refinement method; this yields
                                   # models quickly but of low quality;
                                   # use refine.slow for better models

m.make()
