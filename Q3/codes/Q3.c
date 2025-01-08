#include <math.h>
#include <stdio.h>

double f(double x) {
    return exp(x) * sin(x);
}

double trapezoidal_rule(double a, double b, int n) {
    double h = (b - a) / n;
    double integral = 0.0;

    for (int i = 0; i <= n; i++) {
        double x = a + i * h;
        if (i == 0 || i == n) {
            integral += f(x); // First and last terms
        } else {
            integral += 2 * f(x); // Middle terms
        }
    }

    integral *= (h / 2);
    return integral;
}

