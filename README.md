# 📊 Cosmological Parameter Estimation

This repository contains a set of cosmological parameter inference runs using [Cobaya](https://cobaya.readthedocs.io/en/latest/), applied to several cosmological models and data combinations from recent large-scale structure and supernovae surveys, as well as compressed CMB priors.

## 🌌 Objective

The goal is to explore how different extensions to the standard ΛCDM model affect parameter inference when combining current cosmological datasets, including:

- Baryon Acoustic Oscillations (BAO) from **DESI DR2**
- Type Ia supernovae from **Pantheon+**, **DES-Y5**, and **Union3**
- Compressed **CMB** priors in the form of Gaussian constraints

## 📁 Repository Structure

runs/
camb/ # Runs using the CAMB theory code
base/ # Standard ΛCDM
run.yaml # Cobaya configuration file
chains/ # Output MCMC chains
base_mnu/ # ΛCDM + neutrino mass
base_w0wa/ # w₀wₐCDM: dynamical dark energy
...


Each subdirectory in `runs/camb/` corresponds to a different cosmological model.

## 🧪 Cosmological Models Included

- `base`: Standard ΛCDM
- `base_mnu`: ΛCDM with free total neutrino mass (Σmν)
- `base_w0wa`: Dynamical dark energy model with parameters (w₀, wₐ)
- More extensions can be added similarly.

## 📦 Likelihoods Used

This project includes combinations of the following data:

- **BAO**
  - DESI DR2 (either binned or integrated across redshift)
- **Supernovae**
  - Pantheon+
  - DES-Y5
  - Union3
- **CMB compressed priors**
  - Gaussian priors on parameters like `θ_s`, `r_s/D_V`, etc.

Likelihoods are configured via YAML files and CMB compressed information is implemented as Gaussian priors.

## 🚀 Requirements

- Python ≥ 3.9
- [Cobaya](https://cobaya.readthedocs.io)
- [CAMB](https://camb.info) as theory code
- (Optional) MPI for parallel runs

Example setup:

```bash
conda create -n cobaya_env python=3.10
conda activate cobaya_env
pip install cobaya
pip install camb
