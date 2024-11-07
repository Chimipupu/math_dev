from matplotlib import pyplot as plt
from math import e, pi, sin, cos

# ラジアン単位で角度を指定し、複素数のリストを作成
L1 = [e**(1j * theta * (pi / 180)) for theta in range(0, 360)]
L2 = [cos(theta * (pi / 180)) + 1j * sin(theta * (pi / 180)) for theta in range(0, 360)]

# 実部と虚部をそれぞれ取り出す
L1_real = [z.real for z in L1]
L1_imag = [z.imag for z in L1]
L2_real = [z.real for z in L2]
L2_imag = [z.imag for z in L2]

# プロット
plt.figure(figsize=(6, 6))
plt.plot(L1_real, L1_imag, 'bo', markersize=2, label=r"$L1: e^{i\theta}$")
plt.plot(L2_real, L2_imag, 'ro', markersize=2, label=r"$L2: \cos(\theta) + i\sin(\theta)$")
plt.xlabel("Real Part")
plt.ylabel("Imaginary Part")
plt.title("Euler's formula for the complex plane")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()