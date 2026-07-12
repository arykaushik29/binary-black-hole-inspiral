# Binary black hole inspiral gravitational waveform simulation using post-Newtonian approximation equations (July 2025)

An exercise in modelling the inspiral of two black holes as they spiral toward each other, and in recovering a weak signal from noise the way LIGO/Virgo actually do. This helped me consolidate my understanding of different numerical methods. Written during a 4-week program at ICTS Bangalore, July 2025. 

Each black hole has mass m1 = 10, m2 = 5 solar masses, initial velocity v = 0.3, initial orbital phase phi = 0. From there the equations give:

1. velocity evolution as the orbit loses energy to gravitational radiation
2. orbital phase evolution
3. gravitational-wave polarization signals, h+ (plus) and h× (cross)
4. a second solve of the same system with an adaptive-step Dormand-Prince (dopri5) integrator, to check the fixed-step result against it
5. matched filtering — recovering a weak known signal buried in Gaussian noise, the core technique real detectors use

## Figures

- `fig_velocity_evolution.png` — v(t), rising as the orbit tightens, capped at v = 0.5 where the post-Newtonian approximation stops being valid
- `fig_inspiral_chirp_odeint.png` — h+ / h× polarizations from the fixed-step (odeint) solve, the classic "chirp"
- `fig_inspiral_chirp_dopri5.png` — the same chirp from the adaptive dopri5 solve, as a cross-check
- `fig_matched_filtering.png` — the matched filter output, with a clean peak where the hidden signal actually sits in the noise

Time is scaled by GM/c^3, so the x-axis on the inspiral plots reads in physical time units rather than an arbitrary dimensionless range — worth watching for if you change the masses, since the scaling shifts with them.

## Why two solvers

`inspiral_waveform.py` uses `odeint`, which takes fixed steps. `solve_comparison_dopri5.py` solves the exact same equations with `dopri5`, an adaptive-step method that should be more accurate near merger, where v changes fastest. Running both isn't strictly necessary for the physics, but it's a sanity check: if the two disagree, something's wrong with the fixed step size.

## Setup

```
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install numpy scipy matplotlib
```

## Files

- `matched_filtering.py`
- `velocity_evolution.py`
- `inspiral_waveform.py`
- `solve_comparison_dopri5.py`
- `equations.pdf`
