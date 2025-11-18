"""Generates a .h file with a C implementation of the dust opacity table."""

from meshoid.radiation.dust import dust_mean_opacity
import numpy as np
from os import system

dtype = "double"
N_Trad = 15
Trad = np.logspace(0, 4, N_Trad)
log_Trad = np.log10(Trad)
Tdust_vals = 10, 200, 300, 500, 1000
Tdust_intervals = ((0, 160), (160, 275), (275, 425), (425, 680), (680, 1500))
N_Tdust = len(Tdust_intervals)


with open("dust_opacity_table.h", "w") as F:
    F.write(f"#define N_TRAD {N_Trad} // number of T_rad samples\n")
    F.write("#define N_TDUST 5 // number of T_dust zones\n")
    F.write(f"{dtype} Tdust_zones[N_TDUST] =" + "{160, 275, 425, 680, 1500}; // demarcation of T_dust zones\n")
    F.write(f"{dtype} logTrad_table[N_TRAD] =" + "{" + ",".join([str(logT) for logT in log_Trad]) + "};\n")
    F.write(f"{dtype} log_kappadust_table[N_TDUST][N_TRAD] =" + "{\n")
    for i, (Td1, Td2) in enumerate(Tdust_intervals):
        logkappa = np.log10(dust_mean_opacity(Trad, Td1))
        F.write("{" + ",".join([str(lk) for lk in logkappa]) + "},\n")
    F.write("};")
