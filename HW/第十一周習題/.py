import cmath
import math

def dft(f):
    N = len(f)
    F = []
    for k in range(N):
        total = 0
        for n in range(N):
            total += f[n] * cmath.exp(-2j * cmath.pi * k * n / N)
        F.append(total)
    return F

def idft(F):
    N = len(F)
    f = []
    for n in range(N):
        total = 0
        for k in range(N):
            total += F[k] * cmath.exp(2j * cmath.pi * k * n / N)
        f.append(total / N)
    return f

def verify_signal(f):
    print("Original f[n]:", [round(x, 6) for x in f])
    print("N =", len(f))

    # --- DFT ---
    F = dft(f)
    print("\nDFT F[k] :", [
        complex(round(c.real, 6), round(c.imag, 6)) for c in F
    ])

    # --- IDFT ---
    f_back = idft(F)
    recovered = [round(x.real, 6) for x in f_back]
    print("IDFT f[n]:", [
        complex(round(c.real, 6), round(c.imag, 6)) for c in f_back
    ])

    print("Recovered:", recovered)

    # --- Verification ---
    if all(abs(a - b) < 1e-6 for a, b in zip(f, recovered)):
        print("✔ Verification PASSED\n")
    else:
        print("✘ Verification FAILED\n")

print("Test 1: Constant Signal")
f1 = [5.0, 5.0, 5.0, 5.0]
N = len(f1)
verify_signal(f1)

print("Test 2: Periodic (Cosine) Signal")
N = 8
f2 = [math.cos(2 * math.pi * 1 * n / N) for n in range(N)]
verify_signal(f2)

print("Test 3: Impulse Signal")
f3 = [17.0, 0.0, 0.0, 0.0, 0.0, 0.0]
N = len(f3)
verify_signal(f3)
