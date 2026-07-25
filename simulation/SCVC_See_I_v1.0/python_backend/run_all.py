# -*- coding: utf-8 -*-
'''SCVC物理计算后端 — 为Godot可视化生成数据
运行: python run_all.py  生成 data/*.json + data/*.csv
'''
import numpy as np
import json, os, sys
from scipy.integrate import solve_ivp
from scipy.optimize import root_scalar
import io

# Force UTF-8 output on Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

OUT = os.path.join(os.path.dirname(__file__), '..', 'data')
os.makedirs(OUT, exist_ok=True)

def compute_vortex_profile():
    def gp_ode(r, y):
        f, fp = y
        if r < 1e-12:
            return [fp, 0.0]
        fpp = -fp/r + f/r**2 + f**3 - f
        return [fp, fpp]

    def shoot(c1):
        r0, rmax = 1e-6, 20.0
        c3 = -c1/8
        f0 = c1*r0 + c3*r0**3
        fp0 = c1 + 3*c3*r0**2
        sol = solve_ivp(gp_ode, [r0, rmax], [f0, fp0], max_step=0.05, rtol=1e-8)
        return sol.y[0,-1] - 1.0

    c1 = root_scalar(shoot, bracket=[0.5, 2.0], method='brentq').root

    r_samples = np.linspace(0, 8, 256)
    profile = np.zeros(256)
    for i, r in enumerate(r_samples):
        if r < 1e-6:
            profile[i] = 0.0
        else:
            r0 = 1e-6
            c3 = -c1/8
            f0 = c1*r0 + c3*r0**3
            fp0 = c1 + 3*c3*r0**2
            sol = solve_ivp(gp_ode, [r0, max(r, r0+0.01)], [f0, fp0], max_step=0.05, rtol=1e-8)
            profile[i] = sol.y[0,-1]

    table = np.column_stack([r_samples, profile])
    np.savetxt(os.path.join(OUT, 'vortex_profile.csv'), table,
               delimiter=',', header='r,psi', comments='')

    xi_eff = r_samples[np.argmax(profile > 0.632)]
    result = {
        'c1': float(c1),
        'xi_effective': float(xi_eff),
        'profile_r': r_samples.tolist(),
        'profile_psi': profile.tolist(),
    }
    with open(os.path.join(OUT, 'vortex_profile.json'), 'w') as f:
        json.dump(result, f, indent=2)
    print(f'[OK] vortex_profile: c1={c1:.6f}, xi={xi_eff:.4f}')
    return result

def compute_dh_fixed_points():
    pi = np.pi
    data = {
        'F1': {
            'name': 'F1: Ring collapses to point (R=0)',
            'ring_radius': 0.0,
            'ring_normal': [0, 1, 0],
            'contribution': '4*pi^3',
            'value': float(4 * pi**3),
            'dimension': 'Isolated fixed point (dim=0)',
            'color': [1.0, 0.4, 0.2],
            'display_radius': 0.15,
        },
        'C2': {
            'name': 'C2: Equilibrium ring (R=R_eq)',
            'ring_radius': 1.5,
            'ring_normal': [0, 1, 0],
            'contribution': 'pi^2',
            'value': float(pi**2),
            'dimension': 'CP1 fixed submanifold (dim=1)',
            'color': [0.2, 0.8, 1.0],
            'display_radius': 0.08,
        },
        'F3': {
            'name': 'F3: Maximum ring (R=R_max)',
            'ring_radius': 3.0,
            'ring_normal': [0, 1, 0],
            'contribution': 'pi',
            'value': float(pi),
            'dimension': 'Surface fixed submanifold (dim=2)',
            'color': [0.2, 1.0, 0.4],
            'display_radius': 0.06,
        },
        'dh_sum': {
            'formula': '4*pi^3 + pi^2 + pi',
            'value': float(4*pi**3 + pi**2 + pi),
            'alpha_inverse_experiment': 137.035999084,
            'deviation_ppm': 2.22,
        }
    }
    with open(os.path.join(OUT, 'dh_fixed_points.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f'[OK] dh_fixed_points: alpha^-1={data["dh_sum"]["value"]:.6f}')
    return data

def compute_cp2_weights():
    w = [
        [1/np.sqrt(2), 1/np.sqrt(6)],
        [-1/np.sqrt(2), 1/np.sqrt(6)],
        [0, -np.sqrt(2/3)],
    ]
    labels = ['w1 (up)', 'w2 (up-left)', 'w3 (down)']
    colors = [[1.0, 0.3, 0.3], [0.3, 0.6, 1.0], [0.3, 1.0, 0.3]]

    vectors = []
    for i in range(3):
        vectors.append({
            'label': labels[i],
            'x': float(w[i][0]),
            'y': float(w[i][1]),
            'r': float(np.sqrt(w[i][0]**2 + w[i][1]**2)),
            'color': colors[i],
        })

    m_e, m_mu, m_tau = 0.510998950, 105.6583755, 1776.86
    sqrt_m = np.array([np.sqrt(m_e), np.sqrt(m_mu), np.sqrt(m_tau)])
    K_exp = float(np.sum([m_e, m_mu, m_tau]) / np.sum(sqrt_m)**2)

    data = {
        'vectors': vectors,
        'r_squared': float(2/3),
        'angles': [120.0, 120.0, 120.0],
        'koide': {
            'K_experiment': K_exp,
            'K_theory': float(2/3),
            'deviation': float(K_exp - 2/3),
        },
        'identity': 'sum(n * w_hat_i)^2 = 3/2 for all n',
    }
    with open(os.path.join(OUT, 'cp2_weights.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f'[OK] cp2_weights: K={K_exp:.8f} vs 2/3')
    return data

def compute_moduli_scan():
    pi = np.pi
    r_values = np.linspace(0, 4, 200)
    scan = []
    for R in r_values:
        if R < 0.01:
            euler_contrib = 4 * pi**3
            ftype = 'F1'
        elif R < 1.2:
            t = R / 1.5
            euler_contrib = 4*pi**3 * (1-t) + pi**2 * t
            ftype = 'F1->C2'
        elif R < 2.2:
            euler_contrib = pi**2
            ftype = 'C2'
        elif R < 3.0:
            t = (R - 2.2) / 0.8
            euler_contrib = pi**2 * (1-t) + pi * t
            ftype = 'C2->F3'
        else:
            euler_contrib = pi
            ftype = 'F3'
        scan.append({'R': float(R), 'euler': float(euler_contrib), 'type': ftype})

    with open(os.path.join(OUT, 'moduli_scan.json'), 'w') as f:
        json.dump(scan, f, indent=2)
    print(f'[OK] moduli_scan: {len(scan)} points from R=0 to R=4')
    return scan

if __name__ == '__main__':
    print('=== SCVC Physics Backend ===')
    compute_vortex_profile()
    compute_dh_fixed_points()
    compute_cp2_weights()
    compute_moduli_scan()
    print(f'All data written to {OUT}/')
