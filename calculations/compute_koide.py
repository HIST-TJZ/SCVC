# Koide公式在CP2框架中的数值计算
# 可复现脚本 - 2026-07-21

import numpy as np

print('='*60)
print('1. SU(3) 3-Representation Weight Vectors')
print('='*60)

w = [
    np.array([1/np.sqrt(2), 1/np.sqrt(6)]),
    np.array([-1/np.sqrt(2), 1/np.sqrt(6)]),
    np.array([0, -np.sqrt(2/3)]),
]

R_sq = np.dot(w[0], w[0])
R = np.sqrt(R_sq)
labels = ['w1','w2','w3']

print(f'R^2 = {R_sq:.8f} = 2/3')
for i in range(3):
    for j in range(i+1, 3):
        cos_theta = np.dot(w[i], w[j]) / R_sq
        theta = np.arccos(cos_theta) * 180 / np.pi
        print(f'  {labels[i]} . {labels[j]}: cos={cos_theta:.1f}, angle={theta:.6f} deg')
    print(f'  |{labels[i]}|^2 = {np.dot(w[i],w[i]):.8f}')

w_hat = [wi/R for wi in w]
print(f'\nNormalized: w1_hat={w_hat[0]}, w2_hat={w_hat[1]}, w3_hat={w_hat[2]}')

# Verify key identity for many angles
print('\n--- Key identity: sum (n.w_hat_i)^2 = 3/2 for any n ---')
for phi in np.linspace(0, np.pi, 7):
    n = np.array([np.cos(phi), np.sin(phi)])
    s = sum(np.dot(n, wh)**2 for wh in w_hat)
    print(f'  phi={phi:6.3f}: sum={s:.10f}')

print()
print('='*60)
print('2. Charged Lepton Mass Fitting')
print('='*60)

m_e, m_mu, m_tau = 0.510998950, 105.6583755, 1776.86
sqrt_m = np.array([np.sqrt(m_e), np.sqrt(m_mu), np.sqrt(m_tau)])
masses = np.array([m_e, m_mu, m_tau])

S1 = np.sum(sqrt_m)
S2 = np.sum(masses)
K_exp = S2 / S1**2

print(f'm_e  = {m_e:.6f}  MeV')
print(f'm_mu = {m_mu:.6f}  MeV')
print(f'm_tau = {m_tau:.2f}  MeV')
print(f'K_exp = {K_exp:.10f}')
print(f'K_exp - 2/3 = {K_exp - 2/3:.2e}')

# Fit: sqrt(m_i) = c0 + A*w_hat_x + B*w_hat_y
A = (sqrt_m[0] - sqrt_m[1]) / np.sqrt(3)
B = (sqrt_m[0] + sqrt_m[1] - 2*sqrt_m[2]) / 3
c0 = sqrt_m[0] - A*np.sqrt(3)/2 - B/2
c1R = np.sqrt(A**2 + B**2)
phi_deg = np.arctan2(B, A) * 180 / np.pi

print(f'\nFitted: c0={c0:.6f}, c1R={c1R:.6f}, phi={phi_deg:.4f} deg')
print(f'c1R/c0 = {c1R/c0:.6f}  (cf sqrt(2) = {np.sqrt(2):.6f})')
print(f'Difference: {abs(c1R/c0 - np.sqrt(2)):.2e}')

print()
print('='*60)
print('3. Derivation of Koide Relation')
print('='*60)
print('Ansatz:  sqrt(m_i) = c0 + c1 * n_hat . w_i')
print()
print('S1 = sum sqrt(m_i) = 3*c0            [since sum w_i = 0]')
print('S2 = sum (sqrt(m_i))^2 = 3*c0^2 + c1^2 * sum(n.w_i)^2')
print('sum(n.w_i)^2 = R^2 * sum(n.w_hat_i)^2 = (2/3)*(3/2) = 1')
print('=> S2 = 3*c0^2 + c1^2')
print()
print('K = S2/S1^2 = (3c0^2 + c1^2)/(9c0^2) = 1/3 + c1^2/(9c0^2)')
print()
print('For K = 2/3: c1/c0 = sqrt(3)')
print('=> c1*R/c0 = sqrt(3)*sqrt(2/3) = sqrt(2)')
print()

print('='*60)
print('4. Quark Masses (Running at M_Z)')
print('='*60)

# Up-type at MZ
m_up = np.array([0.00127, 0.619, 171.7])
sqrt_up = np.sqrt(m_up)
K_up = np.sum(m_up) / np.sum(sqrt_up)**2
print(f'Up-type:   K={K_up:.6f}, delta={K_up-2/3:+.6f}')

# Down-type at MZ
m_down = np.array([0.00267, 0.053, 2.85])
sqrt_down = np.sqrt(m_down)
K_down = np.sum(m_down) / np.sum(sqrt_down)**2
print(f'Down-type: K={K_down:.6f}, delta={K_down-2/3:+.6f}')

# Fit projection
for name, sq in [('up', sqrt_up), ('down', sqrt_down)]:
    A = (sq[0] - sq[1])/np.sqrt(3)
    B = (sq[0] + sq[1] - 2*sq[2])/3
    c0 = sq[0] - A*np.sqrt(3)/2 - B/2
    c1R = np.sqrt(A**2+B**2)
    phi = np.arctan2(B,A)*180/np.pi
    print(f'  {name}: c0={c0:.4f}, c1R/c0={c1R/c0:.4f}, phi={phi:.2f} deg')

print()
print('='*60)
print('5. Neutrino Masses (speculative)')
print('='*60)

dm21_sq = 7.42e-5
dm31_sq = 2.51e-3

# Search for m1 such that K=2/3
best, best_m1 = float('inf'), 0
for m1 in np.linspace(0, 0.5, 50001):
    m2 = np.sqrt(dm21_sq + m1**2)
    m3 = np.sqrt(dm31_sq + m1**2)
    K = (m1+m2+m3) / (np.sqrt(m1)+np.sqrt(m2)+np.sqrt(m3))**2
    diff = abs(K - 2/3)
    if diff < best:
        best, best_m1 = diff, m1
        if diff < 1e-12:
            break

m1 = best_m1
m2 = np.sqrt(dm21_sq + m1**2)
m3 = np.sqrt(dm31_sq + m1**2)
print(f'm1={m1:.6f}, m2={m2:.6f}, m3={m3:.6f} eV')
print(f'Sum = {m1+m2+m3:.6f} eV')
print(f'K = {(m1+m2+m3)/(np.sqrt(m1)+np.sqrt(m2)+np.sqrt(m3))**2:.10f}')
print(f'(If Dirac neutrinos follow Koide, this predicts absolute mass scale)')
