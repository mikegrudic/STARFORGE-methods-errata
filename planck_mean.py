from meshoid.radiation.dust import dust_mean_opacity
import numpy as np
from matplotlib import pyplot as plt

Trad = np.logspace(0, 4, 10**4)
Tdust_vals = 10, 200, 300, 500, 1000
Tdust_intervals = ((0, 160), (160, 275), (275, 425), (425, 680), (680, 1500))
colors = plt.get_cmap("inferno")(np.linspace(0.2, 0.8, len(Tdust_vals)))

opacities = []
for i, (Td1, Td2) in enumerate(Tdust_intervals):
    kappa = dust_mean_opacity(Trad, Td1)
    opacities.append(kappa)
    fit = np.polyfit(np.log10(Trad), np.log10(kappa), 9)
    plt.loglog(Trad, kappa, label=r"$T_{\rm d }\in (%g,%g) \rm K$" % (Td1, Td2), color=colors[i])

kappa_LTE = dust_mean_opacity(Trad, Trad)
plt.loglog(Trad, kappa_LTE, label=r"$T_{\rm rad}=T_{\rm d}$", color="black", ls="dashed")

opacities.append(kappa_LTE)

header = "Planck-mean dust opacity in cm^2/g computed for the Semenov 2003 porous 5-layered \
sphere model as a function of radiation temperature (rows) and dust temperature (columns) \
COLUMNS:\n \
(0) T_rad\n \
(1) T_dust=0-160K\n \
(2) T_dust=160-275K\n \
(3) T_dust=275-425K\n \
(4) T_dust=425-680K\n \
(5) T_dust=680-1500K\n \
(6) T_dust=T_rad\n \
"

np.savetxt("planck_mean_opacity.dat", np.c_[Trad, *opacities], header=header)

plt.xlim(2.73, 1e4)
plt.ylim(1e-3, 100)
plt.ylabel(r"$\kappa_{\rm P} \,\left(\rm cm^{2}\,g^{-1}\right)$")
plt.xlabel(r"$T_{\rm rad} \,\left(\rm K\right)$")
plt.title("Planck mean")
legend_args = {"frameon": True, "labelspacing": 0}
plt.legend(**legend_args)
plt.savefig("Trad_vs_kappa_planck.pdf", bbox_inches="tight")


plt.clf()
Trad = np.logspace(0, 4, 10**4)
opacities = []
for i, (Td1, Td2) in enumerate(Tdust_intervals):
    kappa = dust_mean_opacity(Trad, Td1, which="rosseland")
    opacities.append(kappa)
    plt.loglog(Trad, kappa, label=r"$T_{\rm d }\in (%g,%g) \rm K$" % (Td1, Td2), color=colors[i])

kappa_LTE = dust_mean_opacity(Trad, Trad, which="rosseland")
opacities.append(kappa_LTE)
plt.xlim(2.73, 1e4)
plt.ylim(1e-3, 100)
plt.title("Rosseland mean")
plt.loglog(Trad, kappa_LTE, label=r"$T_{\rm rad}=T_{\rm d}$", color="black", ls="dashed")
plt.ylabel(r"$\kappa_{\rm R} \,\left(\rm cm^{2}\,g^{-1}\right)$")
plt.xlabel(r"$T_{\rm rad} \,\left(\rm K\right)$")
plt.legend(**legend_args)
plt.savefig("Trad_vs_kappa_rosseland.pdf", bbox_inches="tight")
plt.clf()

np.savetxt("rosseland_mean_opacity.dat", np.c_[Trad, *opacities], header=header.replace("Planck", "Rosseland"))
