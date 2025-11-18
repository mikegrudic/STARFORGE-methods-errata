#include "./dust_opacity.c"
#include "math.h"
#include "stdio.h"

int main() {
  double Tdust_toplot[5] = {10, 200, 300, 500, 1000};
  for (int i = 0; i < 5; i++) {
    FILE *fptr;
    char filename[sizeof "kappa0.dat"];
    sprintf(filename, "kappa%01d.dat", i);
    fptr = fopen(filename, "w");
    double Tdust = Tdust_toplot[i];
    for (int j = 0; j < 101; j++) {
      double Trad = pow(10., j * 6. / 100 - 1.);
      fprintf(fptr, "%g %g\n", Trad, dust_planck_mean_opacity(Trad, Tdust));
    }
  }
}
