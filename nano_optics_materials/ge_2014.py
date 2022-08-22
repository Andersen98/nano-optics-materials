
import meep as mp
import numpy as np
from scipy import constants
#from Ge, Rong-Chun, Philip Trøst Kristensen, Jeff F Young, and Stephen Hughes. “Quasinormal Mode Approach to Modelling Light-Emission and Propagation in Nanoplasmonics.” New Journal of Physics 16, no. 11 (November 19, 2014): 113048. https://doi.org/10.1088/1367-2630/16/11/113048.
Metal_1_bibliography = """
Ge, Rong-Chun, Philip Trøst Kristensen, Jeff F Young, and Stephen Hughes. “Quasinormal Mode Approach to Modelling Light-Emission and Propagation in Nanoplasmonics.” New Journal of Physics 16, no. 11 (November 19, 2014): 113048. https://doi.org/10.1088/1367-2630/16/11/113048.
"""
Metal_1_wp =  1.26e+16
Metal_1_gamma = 7.0e+13

meep_unit_length_si = constants.micro
meep_unit_time_si = meep_unit_length_si/constants.c

Metal_1_wp_meep = Metal_1_wp*meep_unit_time_si
Metal_1_gamma_meep = Metal_1_gamma*meep_unit_time_si
Metal_1_Valid_Freq_Range = mp.FreqRange(min=1.25,max = 2.5)

Metal_1_Susc = [mp.DrudeSusceptibility(Metal_1_wp_meep/(2.0*np.pi),Metal_1_gamma_meep/(2.0*np.pi),sigma=1.0)]
Metal_1 = mp.Medium(epsilon=1.0,E_susceptibilities=Metal_1_Susc,valid_freq_range=Metal_1_Valid_Freq_Range)