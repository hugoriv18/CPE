import numpy as np
from cobaya.conventions import Const
from cobaya.likelihood import Likelihood
from typing import List

class CMB_compressed(Likelihood):
    type = "CMB_compressed"
    means: np.ndarray
    covs: np.ndarray
    compression_type: str
    observables: List[str]

    def initialize(self):
        # Load data
        self.means = np.array([float(x) for x in self.means[0]])
        self.covs = np.array(self.covs, dtype=float)
        # Select the corresponding block of the covariance matrix and mean values given the observables used
        if self.compression_type == 'standard':
            all_parameters = ['thetastar', 'ombh2', 'ombch2']
        elif self.compression_type == 'shift_parameters':
            all_parameters = ['R', 'lA', 'ombh2', 'omch2']
        self.means, self.covs = self.select_means_and_covs(self.means, self.covs, all_parameters, self.observables)
        # Inflate covariance matrix (to account for extensions to LCDM)
        if self.inflate_cov is True:
            factor = 1.7096774193548387
            self.covs = self.covs * (factor**2)
        # Invert covariance matrix
        self.invcov = np.linalg.inv(np.atleast_2d(self.covs))

    def get_requirements(self):
        if self.compression_type == 'standard':
            return {"thetastar": None, "ombh2": None, "omch2": None}
        elif self.compression_type == 'shift_parameters':
            return {"DAstar": None, "rstar": None, "omegam": None, "H0": None, "ombh2": None}
        
    def select_means_and_covs(self, means, covs, all_parameters, observables):
        # Find the indices of the desired observables
        indices = [all_parameters.index(param) for param in observables]
        # Select the corresponding means
        selected_means = np.array(means)[indices]
        # Select the corresponding rows and columns from the covariance matrix
        selected_covs = np.array(covs)[np.ix_(indices, indices)]
        return selected_means, selected_covs

    def get_theory(self, observable):
        # Get density parameters and H0
        if observable == "ombh2":
            return self.provider.get_param("ombh2")
        elif observable == "omch2":
            return self.provider.get_param("omch2")
        elif observable == "ombch2":
            return self.provider.get_param("ombh2") + self.provider.get_param("omch2")
        # Get distances
        elif observable == "thetastar":
            return self.provider.get_param("thetastar")/100
        elif observable == "R":
            omegam = self.provider.get_param("omegam")
            H0 = self.provider.get_param("H0")
            DAstar = self.provider.get_param("DAstar")
            R = np.sqrt((omegam) * H0**2) * DAstar*(1000.0)/Const.c_km_s
            return R
        elif observable == "lA":
            rstar = self.provider.get_param("rstar")
            DAstar = self.provider.get_param("DAstar")
            lA = (1000.0)*np.pi * DAstar/rstar
        return lA

    def logp(self, **params_values):
        # Get theory
        DV = np.array([self.get_theory(obs) for obs in self.observables])
        # Calculate difference between theory and data
        diff = DV - self.means
        # Estimate likelihood
        return -0.5 * np.dot(diff.T, np.dot(self.invcov, diff))