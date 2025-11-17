from numba import vectorize
import numpy as np


@vectorize
def kappadust_gizmo(Trad, T_dust_opacitytable):
    x = 4 * np.log10(Trad) - 8.0
    dx_excess = np.max(np.array([0.0, x - 7.0]))
    x = np.min(np.array([x, 7]))

    if T_dust_opacitytable < 160.0:  # Tdust < 160 K (all dust constituents present)
        kappa = np.exp(
            0.72819004 + 0.75142468 * x - 0.07225763 * x * x - 0.01159257 * x * x * x + 0.00249064 * x * x * x * x
        )
    elif T_dust_opacitytable < 275.0:  # 160 < Tdust < 275 (no ice present)
        kappa = np.exp(
            0.16658241 + 0.70072926 * x - 0.04230367 * x * x - 0.01133852 * x * x * x + 0.0021335 * x * x * x * x
        )
    elif T_dust_opacitytable < 425.0:  # 275 < Tdust < 425 (no ice or volatile organics present)
        kappa = np.exp(
            0.03583845 + 0.68374146 * x - 0.03791989 * x * x - 0.01135789 * x * x * x + 0.00212918 * x * x * x * x
        )
    elif T_dust_opacitytable < 680.0:  # 425 < Tdust < 680 (silicates, iron, & troilite present)
        kappa = np.exp(
            -0.76576135 + 0.57053532 * x - 0.0122809 * x * x - 0.01037311 * x * x * x + 0.00197672 * x * x * x * x
        )
    elif T_dust_opacitytable < 1500:  # 680 < Tdust < 1500 (silicates & iron present)
        kappa = np.exp(
            -2.23863222 + 0.81223269 * x + 0.08010633 * x * x + 0.00862152 * x * x * x - 0.00271909 * x * x * x * x
        )
    else:
        kappa = 1e-37
    if dx_excess > 0:
        kappa *= np.exp(0.57 * dx_excess)
    return kappa
