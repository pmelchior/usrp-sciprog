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

def draw_schematic(params, t):


    delta, T, t0, tau = params
    plt.plot(t, trapezoid(params, t),lw=3)

    # annotate delta
    plt.axhline(-delta,ls=":",color="k")
    plt.annotate("",xy=(t.min(),0.0),
                xytext=(t.min(),-delta),
                arrowprops=dict(arrowstyle="<->"))
    plt.annotate("delta", (t.min(),-0.5*delta),color="r",fontsize="xx-large")

    # annotate T
    plt.axvline(t0-0.5*T,ls=":",color="k")
    plt.axvline(t0+0.5*T,ls=":",color="k")
    plt.annotate("",xy=(t0-0.5*T,-0.5*delta),
                xytext=(t0+0.5*T,-0.5*delta),
                arrowprops=dict(arrowstyle="<->"))
    plt.annotate("T",(t0,-0.5*delta),color="r",fontsize="xx-large")

    # annotate t0
    plt.axvline(t0,ls=":",color="k")
    plt.annotate("t0",(t0,-0.7*delta),color="r",fontsize="xx-large")

    # annotate tau (ingress)
    plt.axvspan(t0-0.5*T,t0-0.5*T+tau,color="k",alpha=0.2)
    plt.annotate("",xy=(t0-0.5*T,-1.*delta),
                xytext=(t0-0.5*T+tau,-1.*delta),
                arrowprops=dict(arrowstyle="<->"))
    plt.annotate("tau",xy=(t0-0.5*T+0.5*tau,-1.*delta),
                ha="center",va="bottom",color="r",fontsize="large")

    # annotate tau (egress)
    plt.axvspan(t0+0.5*T-tau,t0+0.5*T,color="k",alpha=0.2)
    plt.annotate("",xy=(t0+0.5*T,-1.*delta),
                xytext=(t0+0.5*T-tau,-1.*delta),
                arrowprops=dict(arrowstyle="<->"))
    plt.annotate("tau",xy=(t0+0.5*T-0.5*tau,-1.*delta),
                ha="center",va="bottom",color="r",fontsize="large")

t = np.linspace(-1, 1, 1000)
params = (100, 1, 0.0, 0.2)
draw_schematic(params, t)