#include <iostream>
#include <vector>
#include <cmath>
#include <random>
#include <chrono>
#include <thread>
#include <fftw3.h>
#include "matplotlibcpp.h"

namespace plt = matplotlibcpp;

int main() {
    // Number of sample points
    const int N = 6000;
    // Sample spacing
    const double T = 1.0 / 800.0;

    std::vector<double> x(N), y(N);
    std::vector<double> xf(N / 2), yf_abs(N / 2);

    // Random generator for frequency
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> freq_dist(40, 160);

    // Generate x values
    for (int i = 0; i < N; i++) {
        x[i] = i * T;
    }

    // FFTW setup
    fftw_complex *in = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * N);
    fftw_complex *out = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * N);
    fftw_plan p = fftw_plan_dft_1d(N, in, out, FFTW_FORWARD, FFTW_ESTIMATE);

    while (true) {
        // Generate signal: sin(random_freq * 2πx) + 0.5 * sin(80 * 2πx)
        int rand_freq = freq_dist(gen);
        for (int i = 0; i < N; i++) {
            y[i] = sin(rand_freq * 2.0 * M_PI * x[i]) + 0.5 * sin(80.0 * 2.0 * M_PI * x[i]);
            in[i][0] = y[i];  // real part
            in[i][1] = 0.0;   // imag part
        }

        // Execute FFT
        fftw_execute(p);

        // Compute frequency bins
        for (int i = 0; i < N / 2; i++) {
            xf[i] = i / (N * T);
            yf_abs[i] = (2.0 / N) * sqrt(out[i][0]*out[i][0] + out[i][1]*out[i][1]);
        }

        // Plot
        plt::clf();
        plt::plot(xf, yf_abs, "b-");
        plt::xlabel("Frequency (Hz)");
        plt::ylabel("Amplitude");
        plt::pause(1.0);
    }

    // Cleanup
    fftw_destroy_plan(p);
    fftw_free(in);
    fftw_free(out);

    return 0;
}
