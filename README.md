# 📊 Cosmological Parameter Estimation

This repository contains a set of cosmological parameter inference runs using [Cobaya](https://cobaya.readthedocs.io/en/latest/), applied to several cosmological models and data combinations from recent large-scale structure and supernovae surveys, as well as compressed CMB priors.

## 🌌 Cosmological Models Included

- `base`: Standard ΛCDM with six parameters.
- `base_mnu`: ΛCDM with free total neutrino mass (Σmν).
- `base_omegak`: ΛCDM with spatial curvature (Ωₖ ≠ 0).
- `base_w`: wCDM model with a constant dark energy equation of state parameter w.
- `base_w0wa`: Dynamical dark energy model with time-varying equation of state (w₀, wₐ) using the CPL parametrization.
- `base_nnu`: ΛCDM with variable effective number of relativistic species (N_eff).

Additional extensions can be added in the same structure to explore other beyond-ΛCDM scenarios.

## 📦 Likelihoods and Priors Used

This project includes combinations of the following data:

- **BAO**
  - DESI DR2 (either binned or integrated across redshift)
- **Supernovae**
  - Pantheon+
  - DES-Y5
  - Union3
- **BBN**
  - Gaussian prior on Ω_b h² from Big Bang Nucleosynthesis
- **CMB compressed priors**
  - Gaussian priors on derived parameters such as:
    - Acoustic scale (`θ*`)
    - Baryon density (`Ω_b h²`)
    - Cold+baryon density (`Ω_bc h²`)
  - These are implemented as compressed likelihoods to capture the main CMB information without using the full likelihood.

Likelihoods are configured via YAML files. Compressed CMB and BBN information are incorporated as Gaussian priors.

## ⚙️ Requirements

- Python ≥ 3.9
- [Cobaya](https://cobaya.readthedocs.io)
- [CAMB](https://camb.info) as theory code
- (Optional) MPI for parallel runs

