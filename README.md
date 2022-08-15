# MobCal-MPI
Parallelization of the commonly used MobCal suite to calculate ion mobilities and collision cross sections (v1.2). For full documentation, see the MobCal-MPI user guide.

# Compiling Mobcal-MPI main program (Fortran) 
Mobcal-MPI can either be compiled directly or using cmake. Please note that Mobcal-MPI requires the Intel OneAPI and the corresponding Fortran compilers
to be installed correctly. Additionally, the executable must be linked against MPI, otherwise the build process will fail.

```bash
FC=$(which mpifort) cmake -G "Unix Makefiles" -B "build" -DCMAKE_BUILD_TYPE=Release .
```

# Running Mobcal-MPI
Use the GUI program to convert Gaussian output files to mfj input files for Mobcal.
Please note that the ESP section must be present, which is only written to the Gaussian output file if 
pop=mk was specified. To run the mfj files with mobcal provide an input file of the following form

```
# mobcal-job.sub
PATH_TO_MFJ_FILE.mfj
PATH_TO_MOUT_FILE.mout
```

Mobcal-MPI will read the first line of the file to extract the corresponding input file and will create a 
corresponding output file by reading the second line. The issuing of the command

```bash
mpirun -np ${N_MPI_PROC} mobcal-mpi mobcal-job.sub
```

will start the Mobcal-MPI run with 4 MPI processes.



## Changes in v1.2 <h2>

This release of MobCal-MPI (v 1.2) is equipped with a Python-based Graphical User Interface (GUI) for:


1.Conversion of Gaussian output files (.log) into MobCal-MPI input files (.mfj)

2.Calculation of Boltzmann weights of isomer populations for the generation of Boltzmann-weighted CCSs

3.Extraction of CCSs from MobCal-MPI output files (.mout)

4.Multiple temperatures can now be specified in a single .mfj  input file

5.The reporting of CCS now occurs at the end of each .mout file in a formatted table 



**Get in touch**

Questions? Comments? Concerns? Email us! 

cieritano@uwaterloo.ca

shopkins@uwaterloo.ca



