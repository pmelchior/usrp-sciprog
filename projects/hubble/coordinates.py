import numpy as np

def Dec2Deg(dec):
    import numpy as np
    from six import string_types
    try:
        assert not isinstance(dec, string_types)
        coord_deg = np.empty(len(dec))
        for i in range(len(dec)):
            degs, mins, secs = dec[i].decode().split(":")
            coord_deg[i] = float(degs) + float(mins)/60 + float(secs)/3600
        return coord_deg
    except AssertionError:
        return Dec2Deg([dec])[0]

def Ra2Deg(ra):
    return 15*Dec2Deg(ra)