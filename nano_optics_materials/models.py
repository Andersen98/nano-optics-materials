
def epsilon_drude_lorentz(w,wp,gamma):
    """
    Input:
         w=2*pi*f
         wp is plasma angular frequency
         gamma is loss (units s**-1 radians)
    """
    return 1- (wp**2)/(w*(w+1j*gamma))