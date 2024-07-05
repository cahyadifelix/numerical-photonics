"""Contains the calculations needed for 1D slab waveguide"""

import numpy as np

def transverse_wavevector(k0, ref_index, beta) -> float:
    """Calculate the transverse wavevector kappa

    Args:
        k0 (float): wavevector in vacuum
        ref_index (float): the refractive index of the material
        beta (float): The longitudinal wavevector

    Returns:
        kappa: The transverse wavevector
    """
    if isinstance(beta, float):
        if k0*ref_index<beta:
            raise ValueError("k0*n should not be smaller than beta, see attenuation coefficient.")
    return np.sqrt((k0*ref_index)**2 - beta**2)

def attenuation_coefficient(k0, ref_index, beta) -> float:
    """Calculate the attenuation coefficient gamma

    Args:
        k0 (float): wavevector in vacuum
        ref_index (float): the refractive index of the material
        beta (float): The longitudinal wavevector

    Raises:
        Exception: k0n should be smaller than beta due to the physical definition

    Returns:
        gamma: The attenuation coefficient
    """
    if isinstance(beta, float):
        if k0*ref_index>beta:
            raise ValueError("k0*n should not be larger than beta, see transverse wavevector.")
    return np.sqrt(beta**2 - (k0*ref_index)**2)