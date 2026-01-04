import math

a = 8.0
b = 10.0
c = 15.0

def root(a, b, c):
    judge = b ** 2 - 4 * a * c
    if judge > 0:
        ans1 = (-b + math.sqrt(judge)) / (2 * a)
        ans2 = (-b - math.sqrt(judge)) / (2 * a)
        print("answer: ", ans1, ans2)
    elif judge == 0:
        ans = -b / (2 * a)
        print("answer:", ans)
    else:
        real = -b / (2 * a)
        imag = math.sqrt(-judge) / (2 * a)
        print("answer: ", f"{real}+{imag}i", f"{real}-{imag}i")

root(a, b, c)
