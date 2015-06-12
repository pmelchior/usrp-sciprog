import astropy.io.fits
import numpy as np

fits = astropy.io.fits.open("HSC_grizy_example.fits")
table = fits[1].data

def getMagnitudes(table, magzero, fluxes):

    """
    returns the magnitudes of the fluxes through each filter of HSC
    """
    fluxarrays = {}

    for k,v in fluxes.items():
        fluxarrays[k] = table[v]

    mask = np.ones(len(table), dtype=bool)

    for k,v in fluxes.items():
        mask = np.logical_and(mask, np.isfinite(table[v]))
        mask = np.logical_and(mask,table[v]>0.0)

    subset = table[mask]

    for k,v in fluxarrays.items():
        fluxarrays[k] = flux_to_mag(subset[v],magzero)
    return fluxarrays


def flux_to_mag(flux,magzero):
    """
    converts a flux to a magnitudes
    """
    return -2.5*np.log10(flux) + magzero

mags = getMagnitudes(table,27.0,{'r':'R_FLUX_KRON','i':'I_FLUX_KRON','g':'G_FLUX_KRON','z':'Z_FLUX_KRON'})

