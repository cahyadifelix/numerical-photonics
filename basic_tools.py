"""This is a module containing the basic functions needed in photonics calculations"""

# Import another libraries for calculations
import numpy as np

PLANCK_CONST = 6.62607015e-34
SPEED_OF_LIGHT = 299792458
PI = np.pi
VACUUM_PERMITTIVITY = 8.854e-12
VACUUM_PERMEABILITY = 4*PI*1e-7



def lamb2omega(lamb, ref_index = 1.0):
    """ Function to convert wavelength into angular frequency

    Args:
        lamb (float): wavelength
        ref_index (float, optional): The refractive index of the material. Defaults to 1.0

    Returns:
        omega: The angular frequency of light
    """
    return (2*PI*SPEED_OF_LIGHT)/(ref_index*lamb)

def freq2omega(freq):
    """ Convert frequency to angular frequency

    Args:
        freq (float): frequency

    Returns:
        omega: the angular frequency
    """
    return 2*PI*freq



def impedance(epsilon = VACUUM_PERMITTIVITY, mu = VACUUM_PERMEABILITY):
    """Calculate the impedance of a dielectric

    Args:
        epsilon (float, optional): The permittivity of the media. Defaults to VACUUM_PERMITTIVITY.
        mu (float, optional): The permeability of the media. Defaults to VACUUM_PERMEABILITY.

    Returns:
        impedance: optical impedance of the system
    """
    return np.sqrt(mu/epsilon)


    
