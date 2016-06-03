def Dec2Deg(dec):
    import numpy as np
    try:
        assert not isinstance(dec, basestring)
        coord_deg = np.empty(len(dec))
        for i in xrange(len(dec)):
            degs, mins, secs = dec[i].split(":")
            coord_deg[i] = float(degs) + float(mins)/60 + float(secs)/3600
        return coord_deg
    except AssertionError:
        return Dec2Deg([dec])[0]

def Ra2Deg(ra):
    return 15*Dec2Deg(ra)
