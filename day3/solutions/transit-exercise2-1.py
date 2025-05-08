def trapezoid(params, t):
    
    if not np.isscalar(t):
        return np.array([trapezoid(params, t_) for t_ in t])
    
    delta, T, t0, tau = params
    t_ = t - t0
    if t_ < -T/2:
        return 0
    elif t_ < min(-T/2 + tau,0):
        slope = -delta / tau
        return slope * (t_ + T/2)
    elif t_ < max(0, T/2 - tau):
        return -delta
    elif t_ < T/2:
        slope = delta / tau
        return slope * (t_ - T/2)
    else:
        return 0
