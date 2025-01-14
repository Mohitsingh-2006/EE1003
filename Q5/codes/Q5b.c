#include <math.h>
#include <stdio.h>

// Function to compute eigenvalues (roots)
void find_roots(double a, double b, double c, double *root1, double *root2) {
    // Constructing the 2x2 matrix
    double m00 = 0;
    double m01 = -c / a;
    double m10 = 1;
    double m11 = -b / a;

    // Characteristic equation: lambda^2 - (trace)*lambda + determinant = 0
    double trace = m00 + m11;
    double determinant = (m00 * m11) - (m01 * m10);

    // Roots using the quadratic formula
    double discriminant = (trace * trace) - (4 * determinant);
    *root1 = (trace + sqrt(discriminant)) / 2.0;
    *root2 = (trace - sqrt(discriminant)) / 2.0;
}

