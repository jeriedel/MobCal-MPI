project(mobcal-mpi Fortran)
cmake_minimum_required(VERSION 3.16)
set(FFLAGS "-Ofast")

find_package(MPI REQUIRED)

add_executable(mobcal-mpi MobCal_MPI.f)
target_link_libraries(mobcal-mpi ${MPI_Fortran_LIBRARIES})
