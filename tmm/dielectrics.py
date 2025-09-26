import numpy as np
from scipy.interpolate import interp1d


def kk_transform(kk_inv):
    """kramers kronig via discrete hilbert transform
    https://en.wikipedia.org/wiki/Hilbert_transform#Discrete_Hilbert_transform
    """
    n = np.arange(kk_inv.size) - kk_inv.size // 2
    n[::2] = np.inf
    kernel = -2 / (np.pi * n)
    # kernel[::2] = 0
    
    kk = np.convolve(kk_inv, kernel, mode='same')
    return kk


def from_refractiveindex_info(url, **kwargs) -> object:
    arr = np.genfromtxt(url, **kwargs, unpack=True)
    eV = 1e4 / arr[0] / 8065.5
    func = interp1d(eV, arr[1] + 1j * arr[2], kind='quadratic')
    return func


rp_n2 = from_refractiveindex_info(
    pathlib.Path(__file__).resolve().parent / pathlib.Path(r"refractiveindex.info\database\data\other\perovskite\2D%20HOIP\nk\Song-RP2.yml"),
    skip_headers=15, skip_footers=2
)


def insulator(n:float):
    """define a layer function with fixed refractive index"""
    def nk(w):
        if isinstance(w, float) or isinstance(w, int):
            return n
        return n*np.ones(w.shape, dtype=complex)
    return nk

n_air = insulator(n=1.)
n_fused_silica = insulator(n=1.46)

