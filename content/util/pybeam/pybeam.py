"""
A collection of utility functions for spatial signal processing
"""

import numpy as np
from numpy.typing import NDArray

def steervec(
    pos_lda: NDArray[np.float64], 
    angle: NDArray[np.float64], 
) -> NDArray[np.float64]:
    
    """
        Computes the steering vector, a.k.a. the array manifold vector of an array
        whose elements are located at positions pos_lda.

        Args:
            pos_lda: A numpy array containing the positions of the array elements, in units of wavelengths.
            angle: A numpy array containing the theta and phi angles for which to compute the steering vector.

        Returns:
            A numpy array containing the steering vectors corresponding to the specified angles.
    """

    return None
