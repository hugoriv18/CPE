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
