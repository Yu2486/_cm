import math
import cmath

a = 1
b = -6
c = 11
d = -6

def root3(a, b, c, d):
    if a == 0:
        return
    a1 = b / a
    a2 = c / a
    a3 = d / a

    p = a2 - a1**2 / 3
    q = 2 * a1**3 / 27 - a1 * a2 / 3 + a3

    Δ = (q / 2)**2 + (p / 3)**3

    print(f"判別式 Δ = {Δ:.4f}")

    if Δ > 0:
        u = (-q / 2 + math.sqrt(Δ))**(1/3)
        v = (-q / 2 - math.sqrt(Δ))**(1/3)
        root1 = u + v - a1 / 3
        root2 = -(u + v)/2 - a1/3 + complex(0, math.sqrt(3)*(u - v)/2)
        root3 = -(u + v)/2 - a1/3 - complex(0, math.sqrt(3)*(u - v)/2)
    elif Δ == 0:
        u = (-q / 2)**(1/3)
        root1 = 2 * u - a1 / 3
        root2 = -u - a1 / 3
        root3 = root2
    else:
        r = math.sqrt(- (p**3) / 27)
        phi = math.acos(-q / (2 * math.sqrt(- (p**3) / 27)))
        m = 2 * math.sqrt(-p / 3)
        root1 = m * math.cos(phi / 3) - a1 / 3
        root2 = m * math.cos((phi + 2*math.pi) / 3) - a1 / 3
        root3 = m * math.cos((phi + 4*math.pi) / 3) - a1 / 3
        print("answer:",(root1, root2, root3))
root3(a, b, c, d)
